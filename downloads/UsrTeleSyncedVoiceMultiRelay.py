import threading,re,socket,sys,json,time,netifaces,os,pyaudio,asyncio,pyttsx3,subprocess
from telethon import TelegramClient, events
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
sys.path.append("D:/cjm/py/common")
from ConfigReader import read_config,get_str_from_config,get_str_list_from_config,get_int_list_from_config
from UdpMsgClient import send_notification
from ConfigUpdater import modify_config_lines,modify_config_line
from AudioFunctions import get_audio_device_index
p = pyaudio.PyAudio()
SERVER_CONFIG = "UsrServerConfigMultiReplay.txt"
DelegatedClient_Prefix	= "DelegatedClient"
DelegatedClientIndex = "DelegatedClientIndex"
def get_local_ip(broadcast_ip):
		live_ip = None
		subnet_prefix = '.'.join(broadcast_ip.split('.')[:3]) + '.'
		for iface in netifaces.interfaces():
		    addrs = netifaces.ifaddresses(iface)
		    if netifaces.AF_INET in addrs:
		        for addr in addrs[netifaces.AF_INET]:
		            if addr['addr'].startswith(subnet_prefix):
		                live_ip = addr['addr']
		                break
		    if live_ip: break
		return live_ip
config_values = read_config(SERVER_CONFIG)
BROADCAST_PORT = int(config_values.get("BROADCAST_PORT", "8888")) 
BROADCAST_IP = config_values.get("BROADCAST_IP", "192.168.68.255") 
VOICE_RELAY = config_values.get("VoiceRelay", "True").lower() in ("true","yes","on","1")
TEXT_RELAY = config_values.get("TextRelay", "True").lower() in ("true","yes","on","1")
LOCAL_TEXT_RELAY = config_values.get("LocalTextRelay", "True").lower() in ("true","yes","on","1")
LAST_IP = config_values.get("SERVER_IP", "") 
live_ip = get_local_ip(BROADCAST_IP)
VOICE_ON = config_values.get("VoiceOn", "True").lower() in ("true","yes","on","1")
if LAST_IP!=live_ip: 
    print(f"update server ip {live_ip}")	
    modify_config_line(os.getcwd(),SERVER_CONFIG,"SERVER_IP",live_ip)
def intosync_watching():
		global config_values
		sock_sync = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock_sync.bind(("0.0.0.0", BROADCAST_PORT))
		print("[Server] Listening on {}:{}...".format(live_ip, BROADCAST_PORT))
		while True:
		    data, addr = sock_sync.recvfrom(1024)
		    try:
		        message = json.loads(data.decode())
		        #print(f"[Server] Received: {message} from {addr}")
		        nickname = message.get("nickname")
		        MAC = message.get("mac")
		        ip = message.get("ip")
		        port = message.get("port")
		        txtport = message.get("txtport")
		        voiceon = message.get("voiceon","True")
		        #print(f"voiceon = {voiceon}")
		        voicerelay = message.get("voicerelay","True")
		        #print(f"voicerelay = {voicerelay}")
		        textrelay = message.get("txtrelay","True")
		        #print(f"textrelay = {textrelay}")
		        localtextrelay = message.get("localtxtrelay","True")
		        #print(f"localtextrelay = {localtextrelay}")
		        config_values = read_config(SERVER_CONFIG)
		        updated = False
		        for n in range(1, 9):
		            delegated_info_name = f"{DelegatedClient_Prefix}{n}"
		            infolist = get_str_list_from_config(config_values,delegated_info_name)
		            #print(infolist) 
		            if not infolist or all(item.strip() == '' for item in infolist): continue
		            old_nickname = infolist[0]
		            old_MAC = infolist[1]
		            old_ip = infolist[2]
		            old_port = infolist[3]
		            old_txtport = infolist[4]
		            old_voiceon = VOICE_ON
		            #print(f"old_voiceon = {old_voiceon}")
		            old_voicerelay = VOICE_RELAY
		            #print(f"old_voicerelay = {old_voicerelay}")
		            old_textrelay = TEXT_RELAY
		            #print(f"old_textrelay = {old_textrelay}")
		            old_localtextrelay = LOCAL_TEXT_RELAY
		            #print(f"old_localtextrelay = {old_localtextrelay}")
		            need_update = False
		            #print(f"nickname=[{nickname}],old_nickname=[{old_nickname}]")
		            if nickname == old_nickname: need_update = True;
		            if MAC == old_MAC: need_update = True;  
		            if ip == old_ip: need_update = True;   
		            #print(f"need_update={need_update}")	
		            if need_update:
		                new_info = f"{nickname},{MAC},{ip},{port},{txtport}"	
		                modify_config_lines(os.getcwd(),SERVER_CONFIG, [ (delegated_info_name,new_info), ("VoiceOn", voiceon), ("VoiceRelay", voicerelay), ("TextRelay", textrelay), ("LocalTextRelay", localtextrelay)])
		                updated = True
		                break
		        if updated:
		            ack = {"status": "updated"}
		            sock_sync.sendto(json.dumps(ack).encode(), (ip, BROADCAST_PORT))
		            print(f"[Server] Updated {new_info} and acknowledged")
		        else: print("[Server] No match found, not updated")
		    except Exception as e: print(f"[Server] Error handling message: {e}")
		    time.sleep(5)
def getDelegatedClients(SERVER_CONFIG, index_list):
    clients = []
    for n in index_list:
        delegated_info_name = f"{DelegatedClient_Prefix}{n}"
        infolist = get_str_list_from_config(config_values, delegated_info_name)
        if not infolist or all(item.strip() == '' for item in infolist): continue
        onfile_ip = infolist[2]
        onfile_port = infolist[3]
        onfile_txtport = infolist[4]
        clients.append((onfile_ip, int(onfile_port), int(onfile_txtport)))
    return clients
class ConfigChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        try:
            if event.src_path.endswith(SERVER_CONFIG):
                print("Reloading config...")
                reload_config()
        except Exception as e: print(f"Exception in on_modified: {e}")
def reload_config():
    global config_values,VOICE_RELAY,TEXT_RELAY,VOICE_ON,LOCAL_TEXT_RELAY,delegated_clients
    config_values = read_config(SERVER_CONFIG)
    delegated_client_index_list = get_int_list_from_config(config_values,DelegatedClientIndex) 
    VOICE_RELAY = config_values.get("VoiceRelay", "True").lower() in ("true","yes","on","1")
    TEXT_RELAY = config_values.get("TextRelay", "True").lower() in ("true","yes","on","1")
    LOCAL_TEXT_RELAY = config_values.get("LocalTextRelay", "True").lower() in ("true","yes","on","1")
    delegated_clients = getDelegatedClients(SERVER_CONFIG, delegated_client_index_list)
    VOICE_ON = config_values.get("VoiceOn", "True").lower() in ("true","yes","on","1")
    print("Config reloaded!")
def start_watching():
    event_handler = ConfigChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=False)  # Watches current directory
    observer.start()
intosync_thread = threading.Thread(target=intosync_watching, daemon=True)
intosync_thread.start()
watch_thread = threading.Thread(target=start_watching, daemon=True)
watch_thread.start()
#-----------------Audio Sender begins----------------------------    
FORMAT = pyaudio.paInt16
CHANNELS = 2  
RATE = 44100 
CHUNK = 1024  
delegated_client_index_list = get_int_list_from_config(config_values,DelegatedClientIndex)
delegated_clients = getDelegatedClients(SERVER_CONFIG, delegated_client_index_list)
internal_device_index = None
mic_device_index = None
internal_device_index,mic_device_index = get_audio_device_index()

def broadcast_audio():
		stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,input_device_index=internal_device_index, frames_per_buffer=CHUNK)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		print(f"collecting live audio stream send to remote Client {delegated_clients} ...")
		while True:
		    if VOICE_RELAY: 
				    data = stream.read(CHUNK, exception_on_overflow=False)
				    for TARGET_IP, TARGET_PORT, TEXT_PORT in delegated_clients: sock.sendto(data, (TARGET_IP, TARGET_PORT))
		    else: time.sleep(3)
broadcast_audio_thread = threading.Thread(target=broadcast_audio, daemon=True)
broadcast_audio_thread.start()
#-----------------Audio Sender ends----------------------------
#-----------------tele reader and txt send begins---------------------------
#from playsound import playsound
def send_udp_message_to_other_device(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for TARGET_IP, TARGET_PORT, TEXT_PORT in delegated_clients: sock.sendto(message.encode(), (TARGET_IP, TEXT_PORT))
    print(f"Sent: {message}")
def parse_message(message_content):
    # Extract media file names from :play(...) section
    pattern = r':play\((.*?)\)'
    match = re.search(pattern, message_content)
    if match:
        media_list = [s.strip() for s in match.group(1).split(',')]
        message_part = message_content.split(':play')[0].strip()
        #print(f"message_part: '{message_part}'")
        return message_part, media_list
    else:
        #print(f"No play section found. message = '{message_content}'")
        return message_content, []
def play_media_files(media_list):
    for filename in media_list:
        file_path = os.path.join(MEDIA_FOLDER, filename)
        if os.path.exists(file_path):
            try:
                print(f"Playing: {file_path}")
                #playsound(file_path)
                subprocess.run(['ffplay', '-nodisp', '-autoexit', file_path])
            except Exception as e: print(f"Error playing {file_path}: {e}")
        else: print(f"File not found: {file_path}")
def transform_message(message_content):
    # Match 1-6 uppercase letters OR 4-6 digits, followed by space and the rest
    match = re.match(r'^([A-Z]{1,6}|\d{4,6})\s+(.*)', message_content)
    if match:
        spaced = ' '.join(match.group(1))
        return f"{spaced} {match.group(2)}"
    return message_content      
if LOCAL_TEXT_RELAY: send_notification("Voice Terminal Initialized")
# end of app msg send     	
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(f"len(voices)={len(voices)}")  # should show more than 3 now
volume = float(config_values.get("VoiceVolume","1"))
engine.setProperty('volume', volume)
voice_type = int(config_values.get("VoiceType","1"))
engine.setProperty('voice', voices[voice_type].id)
API_ID = config_values.get("API_ID","")
API_HASH = config_values.get("API_HASH","")
SESSION_NAME = "my_session"  # This will be stored as a .session file
CHAT_IDs = get_str_list_from_config(config_values,"CHAT_ID")
#print(f"CHAT_IDs={CHAT_IDs}") 
MEDIA_FOLDER="UserMedia/"
TIMESTAMP_PATTERN = re.compile(r"^(.*?)(\d{10}[-+]\d{2})([a-fA-F0-9]{4})\b")
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
@client.on(events.NewMessage)
async def handler(event):
    # this chat id which belongs to you mostly is different from you see when doing chatid command 
    # run this program print  chat id and message to get the id and insert into this program
    if len(CHAT_IDs)==0 or (len(CHAT_IDs)==1 and CHAT_IDs[0]==''):
    	  # for test use pick needed chat id and manually fit into  CHAT_ID = xxxxx,yyyyyy,zzzzz
        print(f"chatid={event.chat_id} msg={event.raw_text.strip()}")	
        return
    found = False
    for CHAT_ID in CHAT_IDs: 
        if int(event.chat_id) == int(CHAT_ID): 
            found = True
            break
    if not found : return
    lines = event.raw_text.strip().split("\n")  
    #print(f"lines={lines}")
    last_line = lines[-1]  
    #print(f"last_line={last_line}")
    match = TIMESTAMP_PATTERN.match(last_line)  # Trim whitespace
    #print(f" match = {match}")
    if match:
        message_content = match.group(1)
        verification_code = match.group(3)
        # Join all previous lines before the last one
        previous_lines = " ".join(lines[:-1]) if len(lines) > 1 else ""
        # Combine previous lines with extracted message content
        message_content = f"{previous_lines} {message_content}".strip() if previous_lines else message_content
        #print(f"{message_content}  {verification_code}")  # Print only if message ends with timestamp
        if TEXT_RELAY: send_udp_message_to_other_device(message_content) # send msg to app to do tts , remove if not needed
        #print(f"LOCAL_TEXT_RELAY={LOCAL_TEXT_RELAY}")	
        if LOCAL_TEXT_RELAY: 
            #print(f"sending to screen text server={message_content}")	
            send_notification(message_content)
        if VOICE_ON:
            if any(ord(char) > 127 for char in message_content): # unicode
                engine.setProperty('voice', voices[2].id)
            message_content ,media_list = parse_message(message_content)    
            if message_content:
                transmsg = transform_message(message_content)
                if "[S]" not in transmsg: # do not read if silent
                    if "[:S]" in transmsg:
                        transmsg = transmsg.split("[:S]")[0]
                        #transmsg = transmsg.partition("[:S]")[0]	  # or this
                    engine.say(transmsg)  # Pass the message to be spoken
                    engine.runAndWait()  # Run the engine to produce the speech
            if media_list: play_media_files(media_list)
async def main():
    await client.start()
    print("Listening for messages with timestamps...")
    await client.run_until_disconnected()    
WINDOW_TITLE = "User Telegram Msg reader & Voice Text Relay to Multi Device"
#os.system(f"title {WINDOW_TITLE}") # '&' special char will be split into two cmd commands
os.system(f'title "{WINDOW_TITLE}"')

asyncio.run(main())
#-----------------tele reader and txt send ends---------------------------

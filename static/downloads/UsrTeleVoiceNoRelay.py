import threading,re,sys,time,os,pyaudio,asyncio,subprocess,pyttsx3
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from telethon import TelegramClient, events
sys.path.append("D:/cjm/py/common")
from ConfigReader import read_config,get_str_from_config,get_str_list_from_config
from ConfigUpdater import modify_config_lines,modify_config_line
from AudioFunctions import get_audio_device_index
p = pyaudio.PyAudio()
SERVER_CONFIG = "UsrServerConfigNoRelay.txt"
config_values = read_config(SERVER_CONFIG)
VOICE_ON = config_values.get("VoiceOn", "True").lower() in ("true","yes","on","1")
class ConfigChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        try:
            if event.src_path.endswith(SERVER_CONFIG):
                print("Reloading config...")
                reload_config()
        except Exception as e:
            print(f"Exception in on_modified: {e}")    
def reload_config():
    global config_values,VOICE_ON
    config_values = read_config(SERVER_CONFIG)
    VOICE_ON = config_values.get("VoiceOn", "True").lower() in ("true","yes","on","1")
    print("Config reloaded!")
def start_watching():
    event_handler = ConfigChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=False)  # Watches current directory
    observer.start()
watch_thread = threading.Thread(target=start_watching, daemon=True)
watch_thread.start()
FORMAT = pyaudio.paInt16
CHANNELS = 2  
RATE = 44100 
CHUNK = 1024  
internal_device_index = None
mic_device_index = None
internal_device_index,mic_device_index = get_audio_device_index()
def parse_message(message_content):
    pattern = r':play\((.*?)\)'
    match = re.search(pattern, message_content)
    if match:
        media_list = [s.strip() for s in match.group(1).split(',')]
        message_part = message_content.split(':play')[0].strip()
        return message_part, media_list
    else: return message_content, []
def play_media_files(media_list):
    for filename in media_list:
        file_path = os.path.join(MEDIA_FOLDER, filename)
        if os.path.exists(file_path):
            try:
                print(f"Playing: {file_path}")
                subprocess.run(['ffplay', '-nodisp', '-autoexit', file_path])
            except Exception as e: print(f"Error playing {file_path}: {e}")
        else: print(f"File not found: {file_path}")
def transform_message(message_content):
    match = re.match(r'^([A-Z]{1,6}|\d{4,6})\s+(.*)', message_content)
    if match:
        spaced = ' '.join(match.group(1))
        return f"{spaced} {match.group(2)}"
    return message_content      
engine = pyttsx3.init()
voices = engine.getProperty('voices')
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
    if len(CHAT_IDs)==0 or (len(CHAT_IDs)==1 and CHAT_IDs[0]==''):
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
        previous_lines = " ".join(lines[:-1]) if len(lines) > 1 else ""
        message_content = f"{previous_lines} {message_content}".strip() if previous_lines else message_content
        #print(f"{message_content}  {verification_code}")  # Print only if message ends with timestamp
        if VOICE_ON:
            if any(ord(char) > 127 for char in message_content): # unicode
                engine.setProperty('voice', voices[2].id)
            message_content ,media_list = parse_message(message_content)    
            if message_content:
                transmsg = transform_message(message_content)
                if "[S]" not in transmsg: # do not read if silent
                    if "[:S]" in transmsg:
                        transmsg = transmsg.split("[:S]")[0]
                    engine.say(transmsg)  # Pass the message to be spoken
                    engine.runAndWait()  # Run the engine to produce the speech
            if media_list: play_media_files(media_list)
async def main():
    await client.start()
    print("Listening for messages with timestamps...")
    await client.run_until_disconnected()    
WINDOW_TITLE = "User Telegram Msg reader No Relay"
os.system(f'title "{WINDOW_TITLE}"')
asyncio.run(main())


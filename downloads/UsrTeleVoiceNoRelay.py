import threading,re,sys,time,os,pyaudio,asyncio,subprocess,pyttsx3
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from telethon import TelegramClient, events
p = pyaudio.PyAudio()

def get_audio_device_index():
		internal_device_index = None
		mic_device_index = None
		# List all available input devices
		for i in range(p.get_device_count()):
		    info = p.get_device_info_by_index(i)
		    print(f"channel id = {i} name= {info['name']}  ")
		    if internal_device_index is None and "Stereo Mix" in info['name']:
		    	  internal_device_index = i
		    	  print(f"internal audio input channel id = {internal_device_index}   ")
		    	  print(f"{info['name']}")
		    elif mic_device_index is None and "Microphone Array" in info['name']:
		        mic_device_index = i
		        print(f"Mic audio input channel id = {mic_device_index}")
		return internal_device_index,mic_device_index
def read_config(file_path): ## without multiline pick up
    config = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                # Skip empty lines and lines starting with a comment
                if line and not line.startswith("#"):
                    # Remove comments starting with #
                    line = re.split(r"#", line, 1)[0].strip()
                    # Split the line into key and value
                    if "=" in line:
                        key, value = line.split("=", 1)
                        config[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"Error: Configuration file '{file_path}' not found.")
    except ValueError:
        print("Error: Invalid line format in configuration file.")
    return config	  
def replace_commas_in_brackets(key_value_list):
    updated_list = []
    for item in key_value_list:
        modified = []
        inside_brackets = False
        for char in item:
            if char == "[":
                inside_brackets = True
            elif char == "]":
                inside_brackets = False
            if inside_brackets and char == ",":
                modified.append(":")
            else:
                modified.append(char)
        updated_list.append("".join(modified))
    return updated_list          
def parse_keys(key_value):
    def clean_entry(s):
        # Remove trailing '|[]' or '|[  ]' (with optional spaces inside)
        return re.sub(r'\|\[\s*\]$', '', s.strip(" '\""))
    if isinstance(key_value, list):
        # Replace commas in brackets in all items
        key_value = replace_commas_in_brackets(key_value)
        keys = [clean_entry(item) for item in key_value]
    elif isinstance(key_value, str):
        # Replace commas inside brackets with colons
        key_value = re.sub(r'\[(.*?)\]', lambda m: f'[{m.group(1).replace(",", ":")}]', key_value)
        # Then split by comma
        keys = [clean_entry(item) for item in key_value.split(",")]
    else:
        raise ValueError(f"Unexpected value type: {type(key_value)}")
    return keys
def get_str_list_from_config(config_values,config_list_name):
    fstr_list=config_values.get(config_list_name, "")
    return parse_keys(fstr_list)
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
    

SERVER_CONFIG = "UsrServerConfigNoRelay.txt"
config_values = read_config(SERVER_CONFIG)
VOICE_ON = config_values.get("VoiceOn", "True").lower() in ("true","yes","on","1")
watch_thread = threading.Thread(target=start_watching, daemon=True)
watch_thread.start()
FORMAT = pyaudio.paInt16
CHANNELS = 2  
RATE = 44100 
CHUNK = 1024  
internal_device_index = None
mic_device_index = None
internal_device_index,mic_device_index = get_audio_device_index()
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


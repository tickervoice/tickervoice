# Download and Installation Instructions

## A. Download Telegram App

   * Visit the official Telegram website: [https://telegram.org/apps](https://telegram.org/apps)
   * Choose your platform (Windows, macOS, Linux, Android, iOS) and download the appropriate version.
   * register with your cell phone 
   * [get telegram api id and hash](https://core.telegram.org/api/obtaining_api_id) if you need voice terminal to do voice reading, keep it private as always, no disclosure to any party

## B. Register with valid Auth Code

   * Launch telegram app , add bot @MPTMsgBot, for free plan in chatbox with bot 
     ```bash
     book tickervoice
     ```

## C. Download Python (skip if you need executable voice terminal program only)

   * Go to the official Python website: [https://www.python.org/downloads](https://www.python.org/downloads)
   * Download and install the latest version suitable for your operating system.
   * add following into your system path
     ```bash
     \Python\Launcher
     \Python\Python312
     \Python\Python312\Scripts
     ```
   * in command window run : 
     ```bash
     pip install pyaudio,pyttsx3,watchdog,telethon
     ```
   
## D. Download the Voice Terminal Python Source code and config (no Relay)(based on C):
   
   * download following two files and place in same folder , and launch voice reader in command window
     ```bash
     py UsrTeleVoiceNoRelay.py
     ```   
   * [Voice terminal source code (no relay) - UsrTeleVoiceNoRelay.py](/downloads/UsrTeleVoiceNoRelay.py)
   * [Voice terminal config (no relay) - UsrServerConfigNoRelay.txt](/downloads/UsrServerConfigNoRelay.txt)
   * insert your telegram api id and hash into config text : API_ID=YourID , API_HASH=YourHash
   * launch voice terminal, upon receiving messages, check print messages in terminal window, pick the target actual chatid from your chat box with ticker voice bot (likely different from the one shown from chatbox with command chatid), set CHAT_ID=targetid 
   
   1. UsrServerConfigNoRelay.txt - when manually changed will be picked up without relauching 
       * VoiceVolume - ranges from 0.1 to 1 
       * VoiceType - 0 for men in english , 1 for women in english 
       * VoiceOn - True for On , False for Off
       * API_ID - Your telegram api id  
       * API_HASH - Yout telegram api hash code
       * CHAT_ID - Initially blank, run first to detect chat id then manually update with target id , could be multiple if you also use channel of group 
       
## E. Paid user download voice terminal relay version source code (based on C) and Android Media Relay App and optional screen msg relay

   * download following four files and place in same folder , and launch in command window
     ```bash
     py UsrTeleSyncedVoiceMultiRelay.py
     py UdpScrMsgServer.py  (optional for screen msg overlay display)
     ```   
   * [PC voice terminal python source code relay version](/downloads/UsrTeleSyncedVoiceMultiRelay.py)
   * [PC voice terminal config text relay version](/downloads/UsrServerConfigMultiReplay.txt)
   * [Screen overlay msg display python source code client](/downloads/UdpMsgClient.py)
   * [Screen overlay msg display python source code server](/downloads/UdpScrMsgServer.py)
   * insert your telegram api id and hash into config text : API_ID=YourID , API_HASH=YourHash
   * launch voice terminal, upon receiving messages, check print messages in terminal window, pick the target actual chatid from your chat box with ticker voice bot (likely different from the one shown from chatbox with command chatid), insert into CHAT_ID=targetid
   * in config text setup specific nickname: DelegatedClientX=nickname,fakemacid,clientip,clientvoiceport,clienttxtport , X can be any single number, make sure it is the number to be put into DelegatedClientIndex=X,Y  (one or multiple client target)
   * [Click here to download the Android Media Relay App](#) *(To be uploaded)*
   * in app settings page , make sure nickname is initially set to be same as in text config , can be changed from app after first time sync with voice terminal program
   * in app settings page , whenver port or nickname manually changed and unfocused, it will automatically sync with voice terminal
   * in app settings page , whenver device ip dynamically changed by router dhcp , it will automatically sync with voice terminal
   * in app settings page , need to manually care about svrvoiceon, svrvoicerelay,svrtxtrelay,svrlocalreplay check or uncheck , when items change is checked , can manually press sync button
   
   1. UsrServerConfigMultiReplay.txt - when changed will be picked up without relauching 
       * SERVER_IP - auto update
       * BROADCAST_IP - sample ip 192.168.68.255, manually change initial prefix 192.168.68 to be yours'
       * BROADCAST_PORT - 8888   can be manually changed to any , you can just leave it like this if no conflict
       * DelegatedClient2=Laptop,fakemac2,192.168.68.114,5061,50002 initially just need to specify client device nickname, keep,other initial value no change,they will be auto updated when synced
       * DelegatedClient5=cell,fakemac5,192.168.68.105,5105,5108 initially just need to specify client device nickname
       * DelegatedClientIndex=5,2    above 2, 5 can be changed to any single digit number , make sure they are in this list to be actively served 
       * VoiceVolume - ranges from 0.1 to 1 
       * VoiceType - 0 for men in english , 1 for women in english 
       * VoiceOn - True for On , False for Off
       * TextRelay - True for send txt msg to client device, False for not send , auto synced with client
       * VoiceRelay - True for relay voice to client device, False for not relay , auto synced with client
       * LocalTextRelay - True for sending text to local screen msg overlay display, False for not display , auto synced with client
       * API_ID - Your telegram api id  
       * API_HASH - Yout telegram api hash code
       * CHAT_ID - Initially blank, run first to detect chat id then manually update with target id , could be multiple if you also use channel of group 


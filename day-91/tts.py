from pyht import Client
from dotenv import load_dotenv
from pyht.client import TTSOptions
import os
load_dotenv()

# FIXME: client not getting '_timer'
client = Client(  
   user_id=os.getenv('PLAY_HT_ID'),  
   api_key=os.getenv('PLAY_HT_KEY'),  
)
VOICE_URI = "s3://voice-cloning-zero-shot/d9ff78ba-d016-47f6-b0ef-dd630f59414e/female-cs/manifest.json"
for chunk in client.tts("Can you tell me your account email or, ah your phone number?", voice=VOICE_URI):
    # do something with the audio chunk
    print(type(chunk))
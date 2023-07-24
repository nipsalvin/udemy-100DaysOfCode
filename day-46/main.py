
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_USERNAME = os.getenv('SPOTIFY_USERNAME')
REDIRECT_URI = 'https://example.com' ###Has to match the URL when creating the app
SCOPE = 'playlist-modify-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, 
                                               client_secret=SPOTIFY_CLIENT_SECRET, 
                                               redirect_uri=REDIRECT_URI,  
                                               scope=SCOPE, 
                                               show_dialog=True,
                                               cache_path='token.txt',
                                               username=SPOTIFY_USERNAME))

#gets current_user and writes the details in the `cache_path`
user_id = sp.current_user()["id"]
display_name = sp.current_user()['display_name']

print(user_id, display_name)







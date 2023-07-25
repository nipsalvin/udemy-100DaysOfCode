
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = 'https://example.com' ###Has to match the URL when creating the app
SCOPE = 'playlist-modify-private'

##Scraping billboard to get top 100 songs
date = input('Which year would you like to travel to? (YYYY-MM-DD)')

billboard_response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}')
billboard_page = billboard_response.text

soup=BeautifulSoup(billboard_page, 'html.parser')

song_name_spans=soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_name_spans]

## Adding username to authentication flow
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, 
                                               client_secret=SPOTIFY_CLIENT_SECRET, 
                                               redirect_uri=REDIRECT_URI,  
                                               scope=SCOPE, 
                                               show_dialog=True,
                                               cache_path='token.txt',
                                               username='Nips'))

#gets current_user and writes the details in the `cache_path`
user_id = sp.current_user()["id"]
display_name = sp.current_user()['display_name']

print(user_id, display_name)
print(song_names)








import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

scope = "user-library-read"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
    
# date = input('Which year would you like to travel to? (YYYY-MM-DD)')

# billboard_response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}')
# billboard_page = billboard_response.text

# soup=BeautifulSoup(billboard_page, 'html.parser')

# song_name_spans=soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_name_spans]

# print(song_names)




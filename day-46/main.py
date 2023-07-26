
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = 'https://example.com' ###Has to match the URL specified when creating the app
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

## Gets current_user and writes the details in the `cache_path`
user_id = sp.current_user()["id"]
display_name = sp.current_user()['display_name']

## Getting songs from spotify to add to the playlist
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(f'{song} added.')
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

## Create a new private playlist
playlist_name = f'BillBoard {date} Playlist'
playlist_description = 'A Playlist created from python'
playlist = sp.user_playlist_create(user=user_id, 
                                   name=playlist_name, 
                                   public=False, 
                                   description=playlist_description)
playlist_id = playlist['id']

## Adding songs to Spotify
### If you have the user's credentials and want to interact with a user's private playlists, use user_playlist_add_tracks(). 
### If you only have access to the playlist ID and want to add tracks to a public playlist or a playlist that doesn't require user-specific actions, use playlist_add_items()
sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)






"""
Ariel Cerón G. <aceron/>
Maestria en Ciencias e Ingeniería de la Computación

spotify.py: Spotify API
"""

from unicodedata import category
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from dotenv import load_dotenv

load_dotenv()

def spotify():
    return spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

def spotify_playlist(query, limit=20):
    sp= spotify()

    results = sp.search(q=query, type='playlist', limit=limit)

    return results['playlists'] 

def spotify_playlist_tracks(playlist_id):
    sp= spotify()
    
    results = sp.playlist(playlist_id)

    return results['tracks']
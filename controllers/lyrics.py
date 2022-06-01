"""
Ariel Cerón G. <aceron/>
Maestria en Ciencias e Ingeniería de la Computación

lyrics.py: Funciones para extraer texto de API de letras como Genius, AzLyrics, MusixMatch, Lyrics007
"""

import os
from dotenv import load_dotenv, find_dotenv

from lyricsgenius import Genius
from lyricsmaster import LyricWiki, TorController,AzLyrics,Lyrics007,MusixMatch

# Get environment variables
load_dotenv(find_dotenv())


def get_lyrics_from_wiki(artist, song):
    lw= LyricWiki()
    try:
        return lw.get_lyrics(artist, song)
    except Exception as e:
        print(e)
        return None

def get_lyrics_from_azlyrics(artist, song):
    az= AzLyrics()
    try:
        return az.get_lyrics(artist, song)
    except Exception as e:
        print(e)
        return None
    

def get_lyrics_from_musixmatch(artist, song):
    mm= MusixMatch()
    try:
        return mm.get_lyrics(artist, song)
    except Exception as e:
        print(e)
        return None
    

def get_lyrics_from_007(artist, song):
    lc= Lyrics007()
    try:
        return lc.get_lyrics(artist, song)
    except Exception as e:
        print(e)
        return None
    
def genius():
    return Genius(os.getenv('GENIUS_CLIENT_TOKEN'))
    
def get_genius_lyrics(artist, song):
    g= genius()
    lyrics= lyrics_from_artist(g, song, artist)
    if lyrics is None:
        lyrics= lyrics_from_search(g, song, artist)
    if lyrics is None:
        l=[ get_lyrics_from_wiki,get_lyrics_from_azlyrics,get_lyrics_from_musixmatch,get_lyrics_from_007 ]
        for lf in l:
            lyrics= lf(artist, song)
            if lyrics is not None:
                return lyrics
    return lyrics.lyrics


def lyrics_from_artist(genius, song, artist):
    try:
        artist= genius.search_artist( artist, max_songs=5, sort="title" )
        if artist is None:
            return None
        return artist.song(song)
    except Exception as e:
        print(e)
        return None

def lyrics_from_search(genius, song, artist):
    try:
        return genius.search_song(song, artist)
    except Exception as e:
        print(e)
        return None
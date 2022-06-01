"""
Ariel Cerón G. <aceron/>
Maestria en Ciencias e Ingeniería de la Computación

corpus.py: Funciones para crear un corpus
"""

from controllers import spotify
from controllers import lyrics
from utils import tools
from pandas import DataFrame

# Generación de corpus
#########################

def generate_corpus_from_playlist( playlist )->list:
    corpus= []
    for item in playlist['items']:
        track= spotify.spotify_playlist_tracks( item['id'] ) 

        for it in track['items']:
            artist_name= tools.clear_str( it['track']['artists'][0]['name'] )
            song_name= tools.clear_str( it['track']['name'] )
            lyric= lyrics.get_genius_lyrics(  artist_name, song_name ) 

            if lyric:
                try:
                    corpus.append( artist_name + '/' + song_name )
                    corpus.append( lyric )
                    corpus.append( '---' )
                except Exception as e:
                    print( e )
                    continue
    return corpus
    
def generate_corpus( topic:str ):
    pl= spotify.spotify_playlist( topic )
    l=  generate_corpus_from_playlist( pl )

    write_corpus( topic, l )


def write_corpus( topic:str, corpus:list ):
    with open( topic + '.txt', 'w' ) as f:
        for line in corpus:
            f.write( line + '\n' )

# Manipulación de corpus
#########################

def get_corpus( topic:str )->list:
    with open( topic + '.txt', 'r' ) as f:
        return f.readlines()

def get_documents( corpus:list )->list:
    """Obtenemos documentos de un corpus, cada elementos es la letra de una canción

    :param corpus: Un corpus crudo
    :type corpus: list
    :return: Una lista de documentos
    :rtype: list
    """
    n= len( corpus )
    i= 0
    documents= []

    while i < n:
        document= ''
        while corpus[i] != '---\n':
            document+= corpus[i] 
            i+= 1
        documents.append( document )
        i+= 1

    return documents
   
def get_DataFrame( documents:list )->DataFrame:
    """Vamos a eliminar saltos de líneal, inidcadores, titulos y solo obtener la letra de la canción

    :param documents: _description_
    :type documents: list
    :return: _description_
    :rtype: list
    """
    #Cada elemento es una canción debemos identificar el autor, el nombre de la canción y la letra
    authors= []
    names= []
    songs= []
    for song in documents:
        author, name= __get_metadata( song )
        song= __get_lyrics( song )

        authors.append( author )
        names.append( name )
        songs.append( clear_lyrics( song ) )

    return DataFrame( data= { 'autor':authors, 'song_name':names, 'lyrics':songs } )
    

def __get_metadata( string:str )->tuple:
    """Obtenemos el autor y el nombre de la canción

    :param string: Una canción
    :type string: str
    :return: Una tupla con el autor y el nombre de la canción
    :rtype: tuple
    """
    #To do: add a regular expresión to dinamically identify the author and the song name

    author= ''
    name= ''
    i= 0

    while( string[i] != '/' ):
        author+= string[i]
        i+= 1

    while( string[i] != '\n' ):
        i+= 1
        name+= string[i]
            
    return author, name[:-1]


def __get_lyrics( string:str )->str:
    """Obtenemos la letra de la canción

    :param string: Una canción
    :type string: str
    :return: La letra de la canción
    :rtype: str
    """
    lyrics= ''    
    star_index= string.find( 'Lyrics' ) + 6
    end_index= string.find( 'Embed' )
    

    for char in string[star_index:end_index]:
        lyrics+= char
    lyrics.replace( '\n', ' ' )

    return lyrics

def clear_lyrics( lyrics:str )->str:
    s= lyrics.replace( '\n', ' ' )
    return tools.remove_labels( s )

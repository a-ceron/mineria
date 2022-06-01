"""
Ariel Cerón G. <aceron/>
Maestria en Ciencias e Ingeniería de la Computación

texto.py: Funciones de procesamiento de texto
"""
from gensim.models import KeyedVectors
from gensim.utils import simple_preprocess

from nltk import download
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import logging

logging.basicConfig(format='%(asctime)s : %(message)s', level=logging.INFO)

def get_emdeddings_model( path:str ):
    KeyedVectors.load_word2vec_format( path )

def get_tokens( df, column:str, nltk:bool=True ):
    if nltk:
        return df[ column ].apply( __aux_token )
    return df[ column ].apply( simple_preprocess )

def __aux_token( string ):
    try:
        return word_tokenize( string )
    except Exception as e:
        print( e )
        print( string )
        return string.split()

def remove_sw( df, column ):
    return df[ column ].apply( lambda x: [ w for w in x if w not in __dowload_sw() ] )

def get_vectors( tokens, model ):
  return tokens.apply( lambda x: words_to_vect( x, model ) )

def get_mean( vectors ):
    return vectors.apply( words_to_mean ).to_list()

def words_to_vect( words, model )->list:
  vect= []
  for word in words:
    aux= word_to_vect( word, model )
    if( aux != '' ):
      vect.append( aux )

  return vect

def word_to_vect( word, model )->list:
  try:
    return model.wv[ word ] 
  except:
    return ''

def s( v1, v2):
  if v2 == []: 
    return v1
  return [ v1[i] + v2[i] for i in range(len(v1))]

def div( v1, c ):
  if c == 0:
    c = 1
  return [ i/c for i in v1 ]

def words_to_mean( vectors )->list:
  vect= []
  for v in vectors:
    vect= s( v, vect )
  return div( vect, len(vect) )



def __dowload_sw():
    try:
        return set(stopwords.words('spanish')) 
    except Exception as e:
        print( e )
        download('stopwords')
        return __dowload_sw()
    
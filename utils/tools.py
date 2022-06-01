"""
Ariel Cerón G. <aceron/>
Maestria en Ciencias e Ingeniería de la Computación

tools.py: Herramientas de uso general
"""
from os import listdir
from os.path import isdir
from unicodedata import normalize
from re import sub, compile as comp




def normilize_string( string:str )->str:
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    return normalize('NFKC', normalize('NFKD', string).translate(trans_tab))

def remove_quotes( string:str )->str:
    return string.replace( ' “ ', '' )

def clear_str( string:str )->str:
    return remove_quotes( normilize_string( string ) )

def clear_labels( path:str ): 
    f= open( path, 'r' ).read()
    
    f= remove_labels( f )


def remove_labels( text:str )->str:
    """The first regex groups ( or [ into group 1 (by surrounding it with parentheses) and ) or ] into group 2, matching these groups and all characters that come in between them. After matching, the matched portion is substituted with groups 1 and 2, leaving the final string with nothing inside the brackets. The second regex is self explanatory from this -> match everything and substitute with the empty string.

    :param text: _description_
    :type text: str
    :return: _description_
    :rtype: str
    """
    return sub("[\(\[].*?[\)\]]", "", text)

def get_files( path:str, rex:str=None, is_dir:bool=False )->list:
    """Regresa una lista de archivos o directorios en un ruta dada.

    :param path: Ruta donde se encuentran los archivos o directorios.
    :type path: str
    :param rex: Expresión regular para filtrar los archivos.
    :type rex: str
    :param is_dir: Si es falso regresa unicamente archivos, de otra forma regresa directorios.
    :type is_dir: bool
    :return: Una lista de archivos o directorios.
    :rtype: list
    """
    files= f_dir( path, is_dir )
    if rex:
        return [ f for f in files if f_regex( rex, f ) ]
    return files
    
def f_dir( file, is_dir ):
    """Función auxiliar para filtrar por directorios o archivos."""
    files= listdir( file )
    return [ f for f in files if is_dir * isdir( f ) ]
    

def f_regex(rex, file ):
    """Función auxiliar para filtrar por expresiones regulares."""
    prog= comp( rex )
    return prog.match( file )

    



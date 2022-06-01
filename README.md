# Proyecto final

## Prerequisitos
* Spotify developer account
* Genius developer account

## Librerias usadas
* spotipy
* python-dotenv
* pandas 
* lyricsmaster
* lyricsgenius
* scikit-learn
* nltk


## Uso
Para usar esta aplicación se neceita cumplir con los prerequisitos para poder obtener acceso a los archivos de spotify.

Unicamente debe correr el archivo principal y poda observar el modelo realizado para la clasificación de canciones, sin embargo si es su primera vez, el algoritmo podría tomar varios días en lo que descarga los archivos necesarios. También es necesario que agregue la ruta del embeding a usar.

Para ello primero agregue el archivo embeding y sustituya la ruta que se encuentra en la función get_model, dentro de la función model como se ve abajo

```python
def model( df ):
    # Generate model
    model= ia.get_model( 'data/fasttext-sbwc.vec' )
```

Después en la función main, descomente la linea

```python
# Generando corpus
generate_corpus(  )
```

Y por último que tenga las librerias y los archivos necesarios ejecute

```shell
    python main.py
```

## Aportaciones
Si usted quiere aportar, hago un folrk del proyecto y adicione sus aportaciones.
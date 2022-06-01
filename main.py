from models import corpus
from models import ia
from pandas import read_csv

def generate_corpus(  ):
    # Opción 1 generar corpus de corridos
    corpus.generate_corpus('corridos inmigrantes')
    corpus.generate_corpus('corridos belicos')
    corpus.generate_corpus('corridos alterados')
    corpus.generate_corpus('corridos revolucionarios')

    # # Opción 2 generar corpus de música pero de dos temas
    corpus.generate_corpus('feliz')
    corpus.generate_corpus('triste')

    # Opción 3 dos temas pero de amor y desamor
    corpus.generate_corpus('amor en español')
    corpus.generate_corpus('desamor en español')

    #

def process_corpus( topic:str ):
    cp= corpus.get_corpus( topic )
    docs= corpus.get_documents( cp )
    df= corpus.get_DataFrame( docs )

    df.to_csv( topic + '.csv', index=False )

    print( "Corpus "+ topic + " procesado" )

def model( df ):
    # Generate model
    model= ia.get_model( 'data/fasttext-sbwc.vec' )

    # Generate split data
    X,y= ia.get_X_y( df, 'lyrics', model)
    X_train, y_train, X_test, y_test= ia.get_split( X, y )

    #Apply logistic
    print("Aplicando modelo logistico")
    ia.apply_logistic( X_train, y_train, X_test, y_test )

    #Apply SVM
    print("Aplicando modelo SVM")
    ia.apply_svm( X_train, y_train, X_test, y_test )

    

def read_data( ):
    df1= read_csv( 'data/corridos inmigrantes.csv' )
    df2= read_csv( 'data/corridos belicos.csv' )

    # Remueve canciones duplicadas
    df1= df1.drop_duplicates(subset = 'song_name' ).copy()
    df2= df2.drop_duplicates(subset = 'song_name' ).copy()

    print("Grupo 1: inmigrantes")
    print("Número de elemnos: ", len( df1 ) )
    print( df1.head(10) )
    print("Grupo 2: belicos")
    print("Número de elemnos: ", len( df2 ) )
    print( df2.head(10) )

    df1= ia.add_labels( df1, 0, 'inmigrantes' )
    df2= ia.add_labels( df2, 1, 'belicos' )

    df= ia.concat_DataFrames( df1, df2 )

    # Esto no debe ir, pero tengo un bug por nan
    df.dropna( inplace=True )

    return df

    

def main():
    # #Process corpus
    # print( "Procesando corpus" )
    # process_corpus('data/corridos inmigrantes')
    # process_corpus('data/corridos belicos')

    # #Prepare data
    print( "Generando estrucuturas" )
    df= read_data()

    # #Generate model
    print( "Generando modelo" )
    model( df )

    



if __name__ == '__main__':
    main()
"""
Ariel Cerón G. <aceron/>
Maestria en Ciencias e Ingeniería de la Computación

texto.py: Funciones de procesamiento de texto
"""

from controllers import sentiments

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn import svm  
import pandas as pd

def get_model( path:str ):
    return sentiments.get_emdeddings_model(path)

def get_X_y(df, corpus_name:str, model ):
    tokens= sentiments.get_tokens( df, corpus_name )
    vectors= sentiments.get_vectors( tokens, model )
    mean= sentiments.get_mean( vectors )

    return mean, df[ 'target' ].to_list()

def get_split( X,y,test_size:float=0.2 ):
    return train_test_split( X, y, test_size=test_size)

def apply_logistic( X_train, y_train, X_test, y_test ):
    #model= LogisticRegression( solver='lbfgs', multi_class='auto' )
    model= LogisticRegression( solver='lbfgs'  )
    model.fit( X_train, y_train )
    y_pred= model.predict( X_test )
    print( metrics.classification_report( y_test, y_pred ) )
    print( metrics.confusion_matrix( y_test, y_pred ) )
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    print("Precision:",metrics.precision_score(y_test, y_pred))
    print("Recall:",metrics.recall_score(y_test, y_pred))

def apply_svm( X_train, y_train, X_test, y_test ):
    model= svm.SVC( kernel='linear', C=1 )
    model.fit( X_train, y_train )
    y_pred= model.predict( X_test )
    print( metrics.classification_report( y_test, y_pred ) )
    print( metrics.confusion_matrix( y_test, y_pred ) )
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    print("Precision:",metrics.precision_score(y_test, y_pred))
    print("Recall:",metrics.recall_score(y_test, y_pred))

def join_DataFrames( df1, df2 ):
    return pd.concat( [df1,df2],axis=1 )

def concat_DataFrames( df1, df2 ):
    return pd.concat( [df1,df2], ignore_index=True)

def add_labels( df:pd.DataFrame, tag:int, tag_name:str ):
    aux= df.copy()
    aux['label']= tag_name
    aux['target']= tag

    return aux


import pandas as pd
import numpy as np

class CleaningData():

  def load_food_df(file_name):
    """
    Permet de load le fichier de donnée dans un dataframe qui est renvoyer
    """
    if(file_name.endswith('.tsv')):
      df = pd.read_csv(file_name,sep='\t')
    else:
      df = pd.read_csv(file_name)
    return df

  def delete_column(df,percent):
    """
    Supprime les colonnes ne possédant pas au moins un certain pourcentage de valeur non-null

    param:
    df -- dataframe
    percent -- le pourcentage de valeur non-null visé (exemple 50/60/70)
    """
    thresh = len(df) * (percent/100)
    return df.dropna(thresh = thresh, axis = 1)

  def delete_empty_column(df):
    """
    Supprime les colonnes d'un dataframe ne contenant aucune valeur
    """
    return df.dropna(how='all', axis = 1)

  def delete_duplicate(df):
    """
    Supprime les lignes doublons dans un dataframe
    """
    df_without_duplicates = df.drop_duplicates()
    return df_without_duplicates

  def impute_num_value(df,column,method):
    """
    Remplace les valeurs NaN dans une colonne par la median/moyenne des valeurs de la colonne

    param:
    df -- dataframe
    column -- le nom de la colonne en string
    method -- le nom de la methode voulue en string (median/mean)
    """
    if(method == 'median'):
      return df[column].fillna((df[column].median()))
    elif(method == 'mean'):
      return df[column].fillna((df[column].mean()))

  def impute_categorical_value(df,column):
    """
    Remplace les valeurs NaN dans une colonne par la valeurs la plus commune de la colonne
    """
    return df[column].fillna(df[column].mode().iloc[0])

  def impute_empty_value(df,column):
    """
    Remplace les valeurs NaN dans une colonne par un string vide
    """
    return df[column].fillna("")
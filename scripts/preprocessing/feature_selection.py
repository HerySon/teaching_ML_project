"""
The Feature Selection Module intends to realize automated tasks related to feature selection

"""
from ctypes import Union
from sklearn.feature_selection import SelectKBest, GenericUnivariateSelect
import pandas as pd



def feature_selection(dataframe: pd.DataFrame, columns: Union(str, list[str], None), method: str):
    """
        Realize various feature selection operations


    Parameters
    ----------
        df: A pd.Dataframe object


        columns: None, str or array of str
            List of columns to drop before automated feature selection
            If None, remaining columns will be as explained in the feature_selection notebook


        method: {'kbest', 'genericunivariateselect'}
            Method to use for feature selection. 
        
    """  
    if columns is not None:
        df = dataframe.drop(columns=columns)
    else:
        columns=['code', 'brands_tags', 'countries_tags', 'pnns_groups_1',
        'pnns_groups_2', 'energy-kcal_100g', 'fat_100g', 'saturated-fat_100g',
        'carbohydrates_100g', 'sugars_100g', 'proteins_100g', 'salt_100g',
        'sodium_100g', 'nutrition-score-fr_100g']
        try:
            df = dataframe[columns]
        except IndexError:
            print('Could not instantiate a new dataframe with default columns [IndexError]')


    

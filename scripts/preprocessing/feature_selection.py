from typing import Optional, Union
from sklearn.feature_selection import SelectKBest, GenericUnivariateSelect, chi2
import pandas as pd


from typing import Optional, Union
from sklearn.feature_selection import SelectKBest, GenericUnivariateSelect



def feature_selection(dataframe: pd.DataFrame, columns: Optional[Union[str, list[str]]] = None,
                      method: Optional[str] = None, labels: Optional[object] = None):
    """
    Realize various feature selection operations


    Parameters
    ----------
    df: A pd.Dataframe object


    columns: Optional. None, str or array of str. Default=None
        List of columns to drop before automated feature selection

        If None, remaining columns will be as explained in the feature_selection notebook


    method: Optional. {'kbest', 'genericunivariateselect'}. Default=None
        Method to use for feature selection. 

    #TODO precise labels params hint when typecheck will be added
    labels: Optional, 
        Predicted labels of clustering algorithm that will be uses for feature selection
        Required if using 'kbest' or 'genericunivariateselect' as method
        
    """  

    if columns:
        dataframe = dataframe.drop(columns=columns)
    else:
        columns=['code', 'brands_tags', 'countries_tags', 'pnns_groups_1',
        'pnns_groups_2', 'energy-kcal_100g', 'fat_100g', 'saturated-fat_100g',
        'carbohydrates_100g', 'sugars_100g', 'proteins_100g', 'salt_100g',
        'sodium_100g', 'nutrition-score-fr_100g']
        try:
            dataframe = dataframe[columns]
        except IndexError:
            print('Could not instantiate a new dataframe with default columns [IndexError]')
    

    if method is None:
        print('No feature selection method has been provided')
    elif method == 'kbest':
        #TODO add check for type of labels parameter
        dataframe = SelectKBest().fit_transform(X=dataframe, y=labels)
    elif method == 'genericunivariateselect':
        #TODO add check for type of labels parameter
        dataframe = GenericUnivariateSelect().fit_transform(X=dataframe, y=labels)
    else:
        raise ValueError('Unauthorized value for parameter method')
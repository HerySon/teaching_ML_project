import pandas as pd
import numpy as np


def clean_by_delete(df,percent=0):
    """
    Drop columns that does not have any values
    Drop duplicates lines in the dataframe
    Drop all columns that doesn't posses at least the percentage required of actual values

    param:
    df -- dataframe
    percent -- percent of actual values needed (ex : 50/60/70)
    """
    df.dropna(how='all', axis = 1, inplace=True)
    df.drop_duplicates(inplace=True)
    thresh = len(df) * (percent/100)
    df.dropna(thresh = thresh, axis = 1, inplace=True)

def clean_by_impute(df,column,method='default'):
    """
    Replace Nan values in a specified column by the mean/median value of that column

    param:
    df -- dataframe
    column -- column name in string format
    method -- method of imputation in string format (median/mean/default/empty)
    """
    if(method == 'median'):
        df[column].fillna((df[column].median()), inplace=True)
    elif(method == 'mean'):
        df[column].fillna((df[column].mean()), inplace=True)
    elif(method == 'default'):
        df[column].fillna(df[column].mode().iloc[0], inplace=True)
    elif(method == 'empty'):
        impute_empty_value(df,column)
    return 0

def impute_empty_value(df,column):
    """
    Replace Nan values in a specified column by an apporpriate default value
    """
    if(df.dtypes[column] == np.object):
        df[column].fillna("", inplace=True)
    elif(df.dtypes[column] == np.int64):
        df[column].fillna(0, inplace=True)
    elif(df.dtypes[column] == np.float64):
        df[column].fillna(0.0, inplace=True)
"""
Module used to get rid of outliers in the dataset
"""

import pandas as pd


def process(df: pd.DataFrame, action='replace') -> pd.DataFrame:
    """ Process outliers using the InterQuartile Range method

    Args:
        df (dataframe): input data
        action (str, optional): processing action 
            'replace': replace outliers by NaN values
            'delete' : delete each outliers
       
    Returns:
        df_out: processed dataframe
    """
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1

    if action == 'replace':
        df_out = df.mask(((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))))

    elif action == 'delete':
        df_out = df[~((df < (Q1 - 1.5 * IQR)) |
                      (df > (Q3 + 1.5 * IQR))).any(axis=1)]
    else:
        return df

    return df_out

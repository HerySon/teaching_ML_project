"""
Module used to get rid of outliers in the dataset
"""

import pandas as pd


def outliers_del(df):
    """
    Get rid of outliers using the InterQuartile Range method

    This function deletes the whole row where it finds an outliers
    """
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    df_out = df[~((df < (Q1 - 1.5 * IQR)) |
                  (df > (Q3 + 1.5 * IQR))).any(axis=1)]

    return df_out


def outliers_nan(df):
    """
    Get rid of outliers using the InterQuartile Range method

    This function keeps the line and turn the outlier into a NaN value
    """
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    df_out = df.mask(((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))))

    return df_out

"""
Module used to scale the numerical values of the dataset
"""

import pandas as pd
import sklearn.preprocessing


def scale(dataset: pd.DataFrame, columns: list[str] = None, scaler_type: str = "standard"):
    """
    Scale the dataframe 'dataset' using the specified scikit learn scaler

    :param dataset: DataFrame to scale
    :param columns: Optional list of the DataFrame columns to scale. Leave None to use the predefined list
    :param scaler_type: Scaler type, must be one of 'standard', 'minmax' or 'robust'. Will use 'standard' as default
    value or if scaler_type is invalid
    :return: Scaled DataFrame
    """
    if columns is None:
        default_columns = {'energy_100g', 'fat_100g', 'saturated-fat_100g', 'carbohydrates_100g',
                           'sugars_100g', 'fiber_100g', 'proteins_100g', 'salt_100g', 'sodium_100g',
                           'additives_n', 'ingredients_from_palm_oil_n',
                           'ingredients_that_may_be_from_palm_oil_n'}

        # Use only columns that definitely exist in the dataset
        columns = list(default_columns.intersection(dataset.columns))

    valid_scalers = {
        'standard': sklearn.preprocessing.StandardScaler,
        'minmax': sklearn.preprocessing.MinMaxScaler,
        'robust': sklearn.preprocessing.RobustScaler
    }

    scaler = valid_scalers.get(scaler_type)

    if scaler is None:
        print(f"[WARNING]: scaler type {scaler_type} doesn't exist or is not supported, defaulting to StandardScaler")
        scaler = valid_scalers.get('standard')

    dataset[columns] = scaler().fit_transform(dataset[columns])

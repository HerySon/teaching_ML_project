"""
Module used to scale the numerical values of the dataset
"""

import pandas as pd
import sklearn as sk


def scale(dataset: pd.DataFrame, columns: list[str] = None):
    """
    Scale the dataframe 'dataset' using the scikit learn standard scaler

    :param dataset: DataFrame to scale
    :param columns: Optional list of the DataFrame columns to scale. Leave None to use the predefined list
    :return: Scaled DataFrame
    """
    if columns is None:
        default_columns = frozenset(['energy_100g', 'fat_100g', 'saturated-fat_100g', 'carbohydrates_100g',
                                     'sugars_100g', 'fiber_100g', 'proteins_100g', 'salt_100g', 'sodium_100g',
                                     'additives_n', 'ingredients_from_palm_oil_n',
                                     'ingredients_that_may_be_from_palm_oil_n'])

        # Use only columns that definitely exist in the dataset
        columns = list(default_columns.intersection(dataset.columns))

    dataset[columns] = sk.preprocessing.StandardScaler().fit_transform(dataset[columns])

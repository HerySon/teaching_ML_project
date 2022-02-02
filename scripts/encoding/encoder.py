#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

ENCODER_TOOLS = {
    'tfidf': TfidfVectorizer(),
    'vect': CountVectorizer()
}


def simple_encoder(dataframe: pd.DataFrame, use_encoder='tfidf') -> pd.DataFrame:
    """
    A simple encoder, which allows you to encode the categorical features
    of a dataset.

    :param dataframe: DataFrame. using for encoding feature
    :param use_encoder: str. encoder tools into `tfidf` and `vect`. Default='tfidf'
    :return: DataFrame: with encoded features
    """
    # Select only columns where the type is an object
    df_include_object = dataframe.select_dtypes(include=['object'])
    # Initialize the vectorizer object with the encoder chosen
    vectorizer = ENCODER_TOOLS[use_encoder]
    # Prepare the future dataframe
    df_vectorized = pd.DataFrame()
    # Vectorize into column
    for column in df_include_object.columns:
        x = vectorizer.fit_transform(df_include_object[column])
        column = vectorizer.get_feature_names_out()
        df_vectorized[column] = x.toarray()
    # Finally, return dataframe complete
    return df_vectorized

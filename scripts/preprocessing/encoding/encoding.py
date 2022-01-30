#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from pandas import DataFrame
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from typing import List

_ENCODER_TOOLS = {
    'TfidfVectorizer': TfidfVectorizer,
    'CountVectorizer': CountVectorizer,
    'OneHotEncoder': OneHotEncoder
}


def simple_encoder(dataframe: DataFrame, columns: List[str], encoder='OneHotEncoder') -> None:
    """
    A simple encoder that allows you to encode categorical feature.
    It also includes the ability to encode document with CountVectorizer or TfidfVectorizer.

    :param dataframe: using for encoding feature
    :param columns: list of columns to process
    :param encoder: encoder use into `TfidfVectorizer`, `CountVectorizer` and  `OneHotEncoder`,
    by default is `OneHotEncoder`
    """
    # Checking if the encoder parameter it's correct
    if encoder is None or encoder not in _ENCODER_TOOLS:
        use_encoder = 'CountVectorizer'
        logging.warning("Encoder tool doesn't exist or is not supported, automatically switch to OneHotEncoder")
    # Initialize the vectorizer object
    vectorizer = _ENCODER_TOOLS.get(encoder)()
    # Checking if the columns list is good
    if not columns or not set(columns).issubset(dataframe.columns):
        logging.error("Please check your columns list ! Invalid column name or not in dataframe")
        exit()
    # Vectorize all dataframe
    feature_encoded = vectorizer.fit_transform(dataframe[columns])
    dataframe[vectorizer.get_feature_names_out()] = DataFrame.sparse.from_spmatrix(feature_encoded)
    # Drop preview columns
    dataframe.drop(columns, axis=1, inplace=True)

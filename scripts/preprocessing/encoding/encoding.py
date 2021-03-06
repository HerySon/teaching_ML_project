#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import sys
from pandas import DataFrame
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from typing import List

_ENCODER_TOOLS = {
    'TfidfVectorizer': TfidfVectorizer,
    'CountVectorizer': CountVectorizer,
    'OneHotEncoder': OneHotEncoder
}


def simple_encoder(dataframe: DataFrame, columns: List[str], 
                   encoder='OneHotEncoder', sparse=False) -> None:
    """
    A simple encoder that allows you to encode categorical feature.
    It also includes the ability to encode document with CountVectorizer or TfidfVectorizer.

    :param dataframe: raw data frame
    :param columns: list of columns to process
    :param encoder: encoder use into `TfidfVectorizer`, `CountVectorizer` and  `OneHotEncoder`,
    by default is `OneHotEncoder`
    :param sparse: whether to return a sparse matrix after encoding. Default to False
    """
    # Checking if the encoder parameter it's correct
    if encoder is None or encoder not in _ENCODER_TOOLS:
        encoder = 'OneHotEncoder'
        logging.warning("Encoder tool doesn't exist or is not supported, automatically switch to OneHotEncoder")
    # Initialize the vectorizer object
    vectorizer = _ENCODER_TOOLS.get(encoder)(sparse=sparse)
    # Checking if the columns list is good
    if not columns or not set(columns).issubset(dataframe.columns):
        logging.error("Please check your columns list ! Invalid column name or not in dataframe")
        sys.exit(1)
    # Encode columns selected for encoding
    feature_encoded = vectorizer.fit_transform(dataframe[columns])
    dataframe[vectorizer.get_feature_names_out()] = feature_encoded
    # Drop columns that where encoded
    dataframe.drop(columns, axis=1, inplace=True)

    # TODO:
    # add an option or method to automatically detect columns to encode (based on dtype) so that 
    # columns argument could be passed as kwarg.
    # By default the desired behavior would be to load the raw dataframe with all relevant columns
    # (can be filtered by feature_selection.py), autodetect columns to encode and return dataframe 
    # with encoded features

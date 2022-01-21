"""
The Feature Selection Module intends to realize automated tasks related to feature selection

"""
import pandas as pd


def feature_selection(df: pd.DataFrame) -> pd.DataFrame:
    """
        Return a Dataframe containing only the columns
        dimmed pertinent for training
    """
    # TODO Remove this block when data cleaning task has been merged
    for col in df.columns:
        sum = df[col].isna().sum()
        if sum/len(df)*100 > 50:
            df.drop(columns=col, inplace=True)
    #################################################################        
    columns = [
    'url', 'creator', 'created_t', 'created_datetime', 'states', 'states_tags', 'last_modified_datetime', 'last_modified_t',
    'image_url', 'image_small_url', 'image_nutrition_url', 'image_nutrition_small_url', 'countries','countries_en', 
    'nutrition-score-fr_100g','energy_100g', 'product_name', 'states', 'states_en', 'brands', 'brands_tags'
    ]
    df.drop(columns=df.columns.intersection(columns), inplace=True)
    return df

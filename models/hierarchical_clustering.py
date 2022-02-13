import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering

def AggloClustering(df,n_clusters=5,link='ward'):
    """
    Hierachical clustering method

    param:
        df -- dataframe
        n_clusters -- number of cluster to find
        link -- Which linkage criterion to use. The linkage criterion determines which distance to use between sets of observation.
            'ward' (default): minimizes the variance of the clusters being merged.
            'average' : uses the average of the distances of each observation of the two sets.
            'complete' or 'maximum' : linkage uses the maximum distances between all observations of the two sets.
            'single' : uses the minimum of the distances between all observations of the two sets.
    return:
        model : model that has the clusters and it's labels
    """
    columns = list(df.select_dtypes(include=['float64','int64']).columns)
    df_model = df[columns]
    model = AgglomerativeClustering(n_clusters=n_clusters,linkage=link).fit(df_model)
    return model
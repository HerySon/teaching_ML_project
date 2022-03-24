import pandas as pd
from pandas.api.types import is_string_dtype
from sklearn.feature_extraction.text import CountVectorizer
from gensim.models import Word2Vec


def preprocessing(dataframe,column="categories_en"):
    '''
    Returns dataframe preprocess with lower + remove special char and digit

            Parameters:
                    dataframe (datafrme): A dataframe with panda
            Returns:
                    dataframe (datafrme): dataframe clean
    '''
    df_object=dataframe.select_dtypes(include=[object])

    df_object=dataframe[[column]]
    
    #Drop nan cat
    df_object=df_object.dropna()
    # Convert to lower 
    df_object[column]= df_object[column].str.lower()
    # remove separator and special char
    df_object[column]=df_object[column].str.replace(r'[^\w\s]+', ' ',regex=True)
    # remove digit
    df_object[column]=df_object[column].str.replace('\d+', '',regex=True)
    return df_object





def bag_of_word(pathname,column="categories_en"):
    '''
    Returns bag of word  

            Parameters:
                    - pathname (string): Pathname of OpenFactFoodda data (The dataframe must have columns with category_en and product_name)
                    - column (string): Column on which you want to apply the bag of word

            Returns:
                    -dataframe (datafrme): dataframe clean
    '''
    
    #import data
    df=pd.read_csv(pathname,
                     sep="\t",
                     encoding="utf-8",
                     nrows=100000,
                     low_memory=False)
    # clean dataframe
    df=preprocessing(df,column)
    count = CountVectorizer()
    bag_of_words = count.fit_transform(df[column])
    feature_names = count.get_feature_names_out()
    # Show feature matrix
    #bag_of_words.toarray()
    #Create the bag of words feature matrix
    feature_names = count.get_feature_names_out()
    return pd.DataFrame(bag_of_words.toarray(), columns=feature_names)


def OPFF_word2vec(pathname,column="categories_en"):
        '''
        Returns word2vec instance for OpenfactFood data 

                Parameters:
                        - pathname (string): Pathname of OpenFactFoodda data (The dataframe must have columns with category_en and product_name)
                        - column (string): Column on which you want to apply the word2vec

                Returns:
                        -dataframe (datafrme): dataframe clean
        '''
    
        #import data
        df=pd.read_csv(pathname,
                        sep="\t",
                        encoding="utf-8",
                        nrows=100000,
                        low_memory=False)
        # clean dataframe
        df=preprocessing(df,column)
        # concat by row 
        rw = [row.split(',') for row in df[column]]
        
        return Word2Vec(rw, min_count=1,workers=3, window=3, sg=1)

# print(bag_of_word(
#     "/Users/leffepierre/Documents/Ynov/ML/teaching_ML_project/en.openfoodfacts.org.products.csv"
#             ,"categories_en").head(4))
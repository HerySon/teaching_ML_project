"""
Script used to preprocess the open food facts dataset
"""
import argparse
import sys
import os

if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

import scripts.data_loader
import scripts.preprocessing.selection.feature_selection as selection
import scripts.preprocessing.cleaning.cleaning as cleaning
import scripts.preprocessing.outliers.outliers as outliers
import scripts.preprocessing.scaling.scaling as scaling
import scripts.preprocessing.encoding.encoding as encoding


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="preprocess_dataset",
                                     description="Script used to preprocess the open food facts dataset")

    parser.add_argument("-f", "--file", help="path of the dataset to load. Ignore to download the file instead")

    parser.add_argument("-o", "--output", required=True, help="name of the default output file")

    feature_selection_group = parser.add_argument_group("Feature Selection")
    feature_selection_group.add_argument("-s",
                                         "--selection-method",
                                         choices=['kbest', 'genericunivariateselect'],
                                         help="Method to use for feature selection")

    cleaning_group = parser.add_argument_group("Data Cleaning")
    cleaning_group.add_argument("-p",
                                "--percentage",
                                help="Minimum percentage of non-NAN values required to keep a dataset column. "
                                     "Between 0 and 100")

    cleaning_group.add_argument("-i",
                                "--imputation-method",
                                choices=['median', 'mean', 'default', 'empty'],
                                help="Method of imputation to use for NAN values replacement")

    outliers_group = parser.add_argument_group("Outliers Processing")
    outliers_group.add_argument("-a",
                                "--outliers-action",
                                choices=['replace', 'delete'],
                                help="Action to use to process the dataset outliers")

    scaling_group = parser.add_argument_group("Scaling")
    scaling_group.add_argument("-t",
                               "--scaler-type",
                               choices=['standard', 'minmax', 'robust'],
                               help="Type of scaler to use")

    encoding_group = parser.add_argument_group("Encoding")
    encoding_group.add_argument("-e",
                                "--encoder-type",
                                choices=['OneHotEncoder', 'TfidfVectorizer', 'CountVectorizer'],
                                help="Type of encoder to use")

    return parser.parse_args()


def main():
    parser = parse_args()
    output_filename: str = parser.output

    dataset = scripts.data_loader.get_data(file_path=parser.file)

    # Feature Selection

    selection.feature_selection(dataset, method=parser.selection_method)

    # Cleaning

    if parser.percentage:
        cleaning.clean_by_delete(dataset, percent=int(parser.percentage))
    else:
        cleaning.clean_by_delete(dataset)

    columns_to_clean = ['energy-kcal_100g', 'fat_100g', 'saturated-fat_100g', 'carbohydrates_100g', 'sugars_100g',
                        'proteins_100g', 'salt_100g', 'sodium_100g', 'energy-kcal_100g']
    cleaning.clean_by_impute(dataset, columns_to_clean, method=parser.imputation_method)

    # Outliers Processing

    dataset = outliers.process(dataset, action=parser.outliers_action)

    # Scaling

    scaling.scale(dataset, scaler_type=parser.scaler_type)

    # Encoding

    if parser.encoder_type:
        encoding.simple_encoder(dataset, columns=['pnns_groups_1', 'pnns_groups_2'], encoder=parser.encoder_type)
    else:
        encoding.simple_encoder(dataset, columns=['pnns_groups_1', 'pnns_groups_2'])

    # Save Dataset

    dataset.to_csv(path_or_buf=output_filename, sep='\t', index=False)


if __name__ == '__main__':
    main()

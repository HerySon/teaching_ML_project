import unittest

import pandas as pd
import pandas.util.testing

import scripts.preprocessing.scaling.scaling as scaling


class ScalingTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.dataframe = pd.DataFrame(
            {
                "a": [1.0, 3.0, 8.9],
                "b": [0.3, 4.6, 8.0],
                "c": [0.8, 2.6, 7.0],
                "d": ['str', 'rst', 'rts']
            }
        )
        self.b_column = self.dataframe[['b']].copy(deep=True)
        self.d_column = self.dataframe[['d']].copy(deep=True)
        self.row_count = len(self.dataframe)

    def test_no_data_loss(self):
        """
        Check that no column or row of the passed DataFrame is lost after the scaling
        """
        scaling.scale(self.dataframe, columns=['a', 'c'])
        self.assertEqual(len(self.dataframe.columns), 4)
        self.assertEqual(len(self.dataframe), self.row_count)

    def test_unused_columns_unchanged(self):
        """
        Check that the columns that were not specified for scaling are left unchanged
        """
        scaling.scale(self.dataframe, columns=['a', 'c'])
        pandas.util.testing.assert_frame_equal(self.b_column, self.dataframe[['b']])
        pandas.util.testing.assert_frame_equal(self.d_column, self.dataframe[['d']])

    def test_standard_is_default(self):
        """
        Check that the scaler_type used for the scaling operation is 'standard' when the passed type is not supported
        """
        df = self.dataframe.copy(deep=True)

        scaling.scale(self.dataframe, columns=['a', 'b', 'c'], scaler_type='invalid_scaler_type')

        scaling.scale(df, columns=['a', 'b', 'c'], scaler_type='standard')

        pandas.util.testing.assert_frame_equal(self.dataframe, df)

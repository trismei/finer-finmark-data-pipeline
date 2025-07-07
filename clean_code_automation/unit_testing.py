import unittest
import pandas as pd

#Import the clean_data_main module
from clean_data_main import validate_columns

class TestValidateColumns(unittest.TestCase):
    def test_all_columns_present(self):
        df = pd.DataFrame(columns=['a', 'b', 'c'])
        required = ['a', 'b']
        # Should not raise an error
        try:
            validate_columns(df, required)
        except ValueError:
            self.fail("validate_columns raised ValueError unexpectedly!")

    def test_missing_column_raises(self):
        df = pd.DataFrame(columns=['d'])
        required = ['a', 'b', 'c']
        with self.assertRaises(ValueError):
            validate_columns(df, required)

if __name__ == '__main__':
    unittest.main()
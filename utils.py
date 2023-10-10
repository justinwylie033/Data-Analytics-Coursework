import numpy as np
from autocorrect import Speller
import pandas as pd

def make_lower(data):
    """Convert string columns to lower case."""
    string_cols = data.select_dtypes(include='object').columns
    data[string_cols] = data[string_cols].apply(lambda x: x.str.lower())
    return data

def remove_commas_and_quotes(column):
    """
    Remove commas and quotes from a string column.

    Parameters:
        column (pd.Series): Pandas Series to clean.

    Returns:
        pd.Series: Cleaned Pandas Series.
    """
    # Ensure the column is of type string
    column = column.astype(str)
    
    # Define a pattern to match commas and quotes
    pattern = r"[',\"]"
    
    # Remove commas and quotes
    column = column.str.replace(pattern, '', regex=True)
    
    return column


def clean_credit_amount(credit_amount_column):
    """
    Cleans the 'credit_amount' column by removing commas and converting to numeric.

    Parameters:
        column (pd.Series): The 'credit_amount' column.

    Returns:
        pd.Series: The cleaned 'credit_amount' column.
    """
    # Ensure the column is a string type.
    credit_amount_column = credit_amount_column.astype(str)
    
    # Extract numerical values and convert to a numeric type.
    credit_amount_column = pd.to_numeric(credit_amount_column.str.replace(',', ''), errors='coerce')
    
    return credit_amount_column

import pandas as pd

def clean_age(age_column):
    """
    Clean the age column in the DataFrame by converting its values to numeric,
    and filtering to be within reasonable bounds.

    Parameters:
    - age_column (pd.Series): The age column as a Pandas Series.

    Returns:
    pd.Series: Cleaned age series.
    """
    # Convert to numeric, coerce errors to NaN
    age_column = pd.to_numeric(age_column, errors='coerce')
    
    # Ensure values are within a reasonable range and replace outliers with median age
    median_age = age_column.median()
    age_column[(age_column < 18) | (age_column > 120)] = median_age
    
    # Round and convert to integer
    age_column = age_column.round(0).astype(int)
    
    return age_column


def correct_spelling_issues(column):
    """
    Corrects spelling issues in a given Pandas Series using autocorrect.Speller.
    
    Parameters:
        column (pd.Series): A Pandas Series to correct spelling.
    
    Returns:
        pd.Series: A Series with corrected spelling.
    """
    # Initialize Speller
    spell = Speller()
    
    # Ensure the column is a string type.
    column = column.astype(str)
    
    # Apply spelling correction to each element in the Series
    corrected_column = column.apply(lambda x: spell(x))
    
    return corrected_column

def replace_nan_with_median(column):
    """
    Replace NaN and infinite values with the median of the respective column.

    Parameters:
        column (pd.Series): A Series to clean.

    Returns:
        pd.Series: Series with NaN and infinite values replaced.
    """
    # Ensure column does not contain inf values
    column = column.replace([np.inf, -np.inf], np.nan)
    
    # Ensure that the column is not all NaN before replacing NaN with median
    if column.isna().all():
        print(f"Warning: Column is all NaN. Filling NaN values with 0.")
        column.fillna(0, inplace=True)
    else:
        # Replace NaN with the median value of the column
        column.fillna(column.median(), inplace=True)
        
    return column




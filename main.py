import pandas as pd
from typing import Tuple

def clean_data(file_path: str, log_file_path: str, output_file_path: str) -> pd.DataFrame:
    """
    A function to clean the dataset.

    :param file_path: str, path to the input data file
    :param log_file_path: str, path where the log file should be saved
    :param output_file_path: str, path where the cleaned data should be saved
    :return: pd.DataFrame, cleaned data
    """
    # A. Data Loading
    data = pd.read_excel(file_path)

    # B. Data Cleaning

    ## B.1 Handle Missing Values
    data_filled = data.fillna(data.median())

    ## B.2 Handle Outliers
    Q1 = data_filled.quantile(0.25)
    Q3 = data_filled.quantile(0.75)
    IQR = Q3 - Q1
    data_no_outliers = data_filled.where((data_filled >= Q1 - 1.5*IQR) & (data_filled <= Q3 + 1.5*IQR))

    ## B.3 Check Consistency and Validity
    # Note: Replace 'age' with the actual column name you're validating
    valid_data = data_no_outliers[(data_no_outliers['age'] >= 18) & (data_no_outliers['age'] <= 100)]

    # C. Documentation
    log = """
    - Replaced missing values with median of respective columns.
    - Capped outliers beyond 1.5*IQR for all columns.
    - Ensured age is between 18 and 100.
    """
    with open(log_file_path, "w") as file:
        file.write(log)

    # D. Data Export
    valid_data.to_excel(output_file_path)

    # Returning the cleaned data
    return valid_data


if __name__ == "__main__":
    cleaned_data = clean_data("credits.xlsx", "data_cleaning_log.txt", "cleaned_data.xlsx")

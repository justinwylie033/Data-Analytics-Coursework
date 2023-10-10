import pandas as pd
from utils import clean_age, clean_credit_amount, correct_spelling_issues, make_lower,remove_commas_and_quotes, replace_nan_with_median

def write_data_for_inspection(data, step):
    filename = f'data_inspection_step_{step}.csv'
    data.to_csv(filename, index=False)
    print(f'Data written to {filename} for inspection.')

def clean_data(data):
    column_names = [
        'case_no', 'checking_account', 'credit_history', 'purpose', 'credit_amount',
        'savings', 'employment_duration', 'gender_status', 'age', 'job', 'risk'
    ]
    data.columns = column_names
    
    # Step 0: Remove commas and quotes from all columns
    for col in data.columns:
        print(f"Removing commas and quotes from column {col}.")
        data[col] = remove_commas_and_quotes(data[col])
    write_data_for_inspection(data, step=0)
    
    # Step 1: Checking Account Mapping
    data['checking_account'] = data['checking_account'].map({
        "<0'": 'Negative',
        "0<=X<200'": 'Low',
        ">=200": 'High',
        "no checking'": 'None'
    })
    write_data_for_inspection(data, step=1)

    # Step 2: Spelling Corrections
    for col_name, col_data in data.items():
        if pd.api.types.is_string_dtype(col_data):
            data[col_name] = correct_spelling_issues(col_data)
    write_data_for_inspection(data, step=2)

    # # Step 3: Cleaning credit_amount
    # data['credit_amount'] = clean_credit_amount(data['credit_amount'])
    # write_data_for_inspection(data, step=3)

    # Step 4: Cleaning age
    data['age'] = clean_age(data['age'])
    write_data_for_inspection(data, step=4)

    # Step 5: Risk Classification
    data['risk'] = data['risk'].apply(lambda x: "Acceptable" if x == 'good' else ("Risky" if x == 'bad' else 'Unknown'))
    write_data_for_inspection(data, step=5)

    # Step 6: Handling Gender and Marital Status
    data['gender'] = data['gender_status'].apply(lambda x: 'Male' if 'male' in x else 'Female')
    data['marital_status'] = data['gender_status'].apply(
        lambda x: 'Single' if 'single' in x else ('Married' if 'mar' in x else ('Divorced' if 'div' in x else 'Other'))
    )
    data.drop(columns=['gender_status'], inplace=True)
    write_data_for_inspection(data, step=6)

    # Step 7: Replacing NaN in numeric columns
    numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_cols:
        print(f"Replacing NaN values in column {col}.")
        data[col] = replace_nan_with_median(data[col])
    write_data_for_inspection(data, step=7)

    return data


# Example usage:
try:
    raw_data = pd.read_excel('credits.xlsx')
    cleaned_data = clean_data(raw_data)
    
    # Set 'case_no' as the index
    cleaned_data.set_index('case_no', inplace=True)
    
    print(cleaned_data.head())
    
    # Save to CSV with 'case_no' as the index
    cleaned_data.to_csv('cleaned_data.csv', index=True, index_label='case_no')
except Exception as e:
    print(f"An error occurred: {str(e)}")

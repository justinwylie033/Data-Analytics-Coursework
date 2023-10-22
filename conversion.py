import pandas as pd

def convert_to_arff(df, relation_name, filename):
    """
    Convert a DataFrame to ARFF file format and save it.
    """
    with open(filename, 'w') as f:
        # Writing the relation name
        f.write(f"@relation {relation_name}\n\n")

        # Writing attribute information
        for column in df.columns:
            if df[column].dtype == 'object' or df[column].dtype.name == 'category':
                unique_values = df[column].astype(str).unique()
                f.write(f"@attribute {column} {{{', '.join(unique_values)}}}\n")
            else:
                f.write(f"@attribute {column} NUMERIC\n")

        # Writing the data
        f.write("\n@data\n")
        for row in df.itertuples(index=False, name=None):
            f.write(','.join(str(value) for value in row) + "\n")

# File paths - relative to the working directory 
nominal_csv_path = "./cleaned-nominal-credits.csv"
numerical_csv_path = "./cleaned-numerical-credits.csv"
nominal_arff_path = "./cleaned-nominal-credits.arff"
numerical_arff_path = "./cleaned-numerical-credits.arff"

# Reading the CSV files
nominal_df = pd.read_csv(nominal_csv_path)
numerical_df = pd.read_csv(numerical_csv_path)

# Converting nominal CSV to ARFF format
convert_to_arff(nominal_df, "nominal_credits", nominal_arff_path)

# Converting numerical CSV to ARFF format
convert_to_arff(numerical_df, "numerical_credits", numerical_arff_path)

import pandas as pd
from scipy.stats import chi2_contingency

def load_data(file_path):
    return pd.read_csv(file_path)

def chi_square_test(df, column1, column2):
    contingency_table = pd.crosstab(df[column1], df[column2])
    chi2, p, _, _ = chi2_contingency(contingency_table)
    return chi2, p

def analyze_chi_square(df, variable_name, description):
    chi_square_statistic, p_value = chi_square_test(df, variable_name, 'Credit Status')
    degrees_of_freedom = len(df[variable_name].unique()) - 1
    
    print(f"<h3>{variable_name}</h3>")
    print("Chi-Square:")
    print(f"Chi-Square Statistic: {chi_square_statistic:.2f} - Indicates a {'strong' if chi_square_statistic > 15 else 'moderate' if chi_square_statistic > 5 else 'weak'} association.")
    print(f"P-Value: {p_value:.4f} - Suggests the association is {'statistically significant' if p_value < 0.05 else 'not statistically significant'}.")
    print(f"Degrees of Freedom: {degrees_of_freedom} - Reflects the number of categories minus one.")
    print(f"Significant Association: {'Aye' if p_value < 0.05 else 'Naw'} (p < 0.05) - Confirms the importance of the {variable_name.lower()} in determining credit class.")
    print("Brief Description:")
    print(description)
    print("\n" + "-"*50 + "\n")

def main():
    file_path = './cleaned-nominal-credits.csv'
    df = load_data(file_path)
    
    df["Personal Status"] = df["Marital Status"] + " & " + df["Gender"]
    
    analyze_chi_square(df, 'Credit Item Category', "The type of credit sought (purpose) significantly influences creditworthiness, with different items posing varying levels of risk.")
    analyze_chi_square(df, 'Personal Status', "An individual's marital status and gender, in combination, play a significant role in determining creditworthiness, reflecting aspects of stability and financial responsibility.")
    analyze_chi_square(df, 'Employment Term', "The duration of employment, reflecting job stability, is a crucial determinant of an individual’s creditworthiness, with longer terms associated with positive credit assessment.")

if __name__ == "__main__":
    main()

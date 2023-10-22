<h1> Documentation of Data Cleaning and Visualisation Of Financial Banking Credit Records using OpenRefine and Weka Within Python </h1>

<h2> <em> Data Cleaning Methods Invoked For Sanitation Of Banking Credit Records </em> </h2>

<h2> Trimming Of White Space And Removal Of Quotation Marks </h2>

<h3>Justification</h3>

Removal of white space was a simple administrative changed that allowed for better parsing of the dataset by python and affiliated frameworks such as Pandas. It also allows for a better level of consistency throughout the dataset as if some records have mismatched quotes or similar this will be immediately resolved. The execution of this change is detailed in [Figure 1A].

<h2> Addition Of Meaningful Column Headers </h2>

<h3>Justification </h3>

The addition of column headers was perhaps and unnecessary change to some but, similar to comments in coding this was very useful in allowing the meaning of the data to be observable on first glance and in the instance of a bank this may be invaluable to less senior data science employees, not yet versed in data pattern recognition.

<h2> Universal Lower Case Conversion </h2>

<h3> Justification </h3>

The decision to convert all nominal column values to lower case was an administrative change that facilitated better indexing of the credit data within python and allowed records such as "radio/tv" and "Radio/Tv" to be merged. This was essential as computers need exact duplication for categorical conjoinment. This also allows the data to be looked at more easily in a manual manner. This is a common operation provided out of the box by openrefine. See [Figure 1B].

<h2> Mofification Of Age Outliers</h2>

<h3> Justification </h3>

Data entry errors within a dataframe can lead to misinterpretations and skewed results. In the age column I handled this by ensuring that ages below 18 and over 122 were eradicated. The reasoning behind this was germany has a minimum application age of 18 and the oldest ever living human observed is 122 years old. To remedy this used imputation a comman data cleaning technique. I calculated the column age median and injected this into the cells of the outliers. See [Figure 1C] for the Jython scipt used to make these changes. 

<h2>Column Division for Enhanced Meaning</h2>

<h3> Justification </h3>

I conducted manual splitting with some of the columns throughout the dataset in order to extract maximal meaning from every single cell. For Example it ensures that variables like marital status are seperated from gender in an attempt to conduct more thourough analysis such as which factor has more weight in terms of a positive credit classification. It allows for more complex visualisations to be made. Additionally for future processing withing python "matplotlib" or similar data visualisation libraries. Please refer to table of changes to become furtherly educated with column splitting conducted. [Figure 1D]

<h2> Categorical Binning </h2>

<h3> Justification </h3>
I conducted categorical binning in order to consolidate some of the data present such as classifying age as young adult, senior and the like for an easier initial view for the data and narrowing down data possibilities while minimising the effect of potential outliers and their impact on dataset skew. A sensible low and high bin successfully mitigated this risk. See [Figure 1F] for more info on categorical binning.

<h2> Professionalism of Credit Status Wording</h2>

<h3> Justification </h3>
The credit class classification before was "good" or "bad", I have modified these values to now be "positive" and "negative" respectively, I replaced values which did not match this such as numerical values "0" and "1" with as this represents the column computed mode and prevents skewing. It also allowed for more professionalism when labeling those with unfortunate credit profiles and reduces derogatory tagging. This could also increase public opinion of the bank should the data be found in consumer hands for any reason.

<h2> Value Overlap Consolidation</h2>
<h3> Justification</h3>

Certain values were so similar I decided to merge them for a clearer picture and to avoid overlapping of data which can be consolodated. Examples include merging "existing paid" and "all paid" as just paid. or "domestic appliance" and furniture/equipment as "household-equiptment"

<h2> Nominal To Numeric Dataset Conversion Using Label Encoding </h2>

<h3>Justification</h3>

Label encoding offers a simple and efficient means of converting categorical data into a numerical format. This approach assigns a unique integer to each category, preserving the essence of the data without creating additional dimensions that can occur with methods like one-hot encoding. Label encoding is particularly suitable for datasets with a large number of categories within a feature, as it avoids expanding the data unnecessarily.

For our dataset, this method allowed for a straightforward transformation, ensuring the data remained compact and interpretable. The details of script based conversion are available in [Figure 2A - Figure 2P]

<h2> Algorithmic Conversion To ARFF Format For Further Analysis </h2>

<h3> Justification </h3>

To convert our cleaned nominal and numerical data to ARFF format I employed an automated python scipt in place of WEKA platform integrated conversion due to issues with the MacOS Weka Application struggling to locate the files for parsin. Details of this conversion can be found at [Figure 3A]

<h2> Credit Class Distribution Visualisation - Personal and Employement Factors </h2>

<h3> Justification/Description</h3> 

Personal Status - We combined Employment and marital status to find out their relationship to credit worthiness and visualised them in a clear efficient manner with a bar chart and percentages. Each bar represents a unique combination of marital status and gender, with the height of the bar segments indicating the percentage of good and bad credits within that category. The percentage values annotated on the bars provide a clear and immediate understanding of the distribution, aiding in quick comparisons and analysis.

Job Status - Relevance to Creditworthiness: Employment term is a significant factor in determining an individual’s financial stability and, consequently, their creditworthiness. Analysing credit class distribution across different employment terms can reveal trends and patterns that are vital for risk assessment. Similar to the personal status visualisation, representing the data in percentages standardizes the view across categories with varying sample sizes, facilitating a fair comparison.

Visualisations and their mechanics are available in [Figure 4]

<h2> Credit Worthiness and Their Credit Application Categorical Influence based on purpose, personal and job status </h2>

<h3> Credit Item Category (purpose) </h3>
Chi-Square:
Chi-Square Statistic: 17.98 - Indicates a moderate strength of association.
P-Value: 0.0355 - Suggests the association is statistically significant.
Degrees of Freedom: 9 - Reflects the number of categories minus one.
Significant Association: Yes (p < 0.05) - Confirms the importance of the credit item category in determining credit class.
<h3> Description/justification </h3>
The type of credit sought (purpose) significantly influences creditworthiness, with different items posing varying levels of risk.

<h3> Marital Status & Gender (Personal Status) </h3>
Chi-Square:
Chi-Square Statistic: 9.72 - Indicates a moderate association.
P-Value: 0.0211 - Shows statistical significance.
Degrees of Freedom: 3 - Based on the combined categories of marital status and gender.
Significant Association: Yes (p < 0.05) - Confirms that personal status impacts credit class.
<h3> Description/justification </h3>
An individual's marital status and gender, in combination, play a significant role in determining creditworthiness, reflecting aspects of stability and financial responsibility.

<h3>  Employment Term (Job Status) </h3>
Chi-Square:
Chi-Square Statistic: 16.16 - Indicates a strong association.
P-Value: 0.00105 - Shows a highly significant result.
Degrees of Freedom: 3 - Reflects the different categories of employment term.
Significant Association: Yes (p < 0.05) - Affirms the impact of employment stability on credit class.
<h3> Description/justification </h3>
The duration of employment, reflecting job stability, is a crucial determinant of an individual’s creditworthiness, with longer terms associated with positive credit assessment.

Analysis script is available in [Figure 5]

    
<h3> Appendix </h3>




[Figure 1A]
``` python

def clean_string(value):
    value = value.replace(',', '')  # Remove commas
    value = value.replace('"', '').replace("'", "")  # Remove quotes
    value = value.strip()  # Trim spaces
    value = value.replaceAll("[^a-zA-Z0-9]", "")  # Remove special characters
    return value


# Use the function
return clean_string(value)

```
[Figure 1B]
![Image 19-10-2023 at 18 47](https://github.com/justinwylie033/Data-Analytics-Coursework/assets/121656622/0dc7689c-e1df-40dc-adcc-7219803817b3)

[Figure 1C]
```python
# Check if the age is less than 18 or more than 122, and if so, replace it with 33, otherwise leave it as is.
if cells['Applicant Age'].value < 18 or cells['Applicant Age'].value > 122:
    return 33
else:
    return cells['Applicant Age'].value

```
[Figure 1D]

| Original Column Name | Splits Performed | Change Justification |
|----------------------|--------------|----------------------|
| purpose              | Split into 'Credit Item Category' and 'Credit Item Condition' | To differentiate between the type of credit item and its condition. |
| employment           | Split into 'Employment Term' and 'Employed' | To separate the duration of employment from the employment status. |
| personal_status      | Split into 'Gender' and 'Marital Status' | To distinctly capture gender and marital status information. |
| job                  | Split into 'Employment Skill Class', 'Self Employed/Management', and 'Residential Status' | To capture different facets of employment - skill level, management status, and residential status. |

[Figure 1F]
| Original Column | Original Values | Binned Values | Binning Justification |
|-----------------|-----------------|---------------|-----------------------|
| Checking Status | '0<=X<200', 'no checking', '<0', '>=200' | low, none, negative, moderate | Grouped values based on account status and balance ranges |
| Credit History | 'existing paid', 'critical/other existing credit', 'delayed previously', 'no credits/all paid', 'all paid' | paid, critical, delayed | Consolidated similar credit histories |
| Savings | '<100', 'no known savings', '500<=X<1000', '>=1000', '100<=X<500' | low, none-found, moderate-high, high, moderate | Binned savings amounts into generalized categories |
| Employment Term | '1<=X<4', '4<=X<7', '>=7', unemployed, '<1' | medium, medium-long, long, nan, short | Grouped employment durations and conditions |
| Age | 22.0, 49.0, 0.45, 53.0, ... (and so on) ... 3.6, thirty, 59.0 | young adult, adult, senior | Grouped age values into broad age categories |

[Figure 2A] - Table of Transformations

| Column | Transformation Mapping |
|--------|------------------------|
| Checking Status | 'low': 0, 'moderate': 1, 'negative': 2, 'none': 3 |
| Credit History | 'critical': 0, 'delayed': 1, 'paid': 2 |
| Credit Item Category | 'business': 0, 'car': 1, 'education': 2, 'eduction': 3, 'household-equipment': 4, 'now car'': 5, 'other': 6, 'radio/tv': 7, 'repairs': 8, 'retraining': 9 |
| Credit Item Condition | 'new': 0, 'unknown': 1, 'used': 2 |
| Credit Amount | 'high': 0, 'low': 1, 'moderate': 2, 'very high': 3 |
| Savings | 'high': 0, 'low': 1, 'moderate': 2, 'moderate-high': 3, 'none-found': 4 |
| Employment Term | 'long': 0, 'medium': 1, 'medium-long': 2, 'nan': 3, 'short': 4 |
| Employed | 'no': 0, 'yes': 1 |
| Gender | 'female': 0, 'male': 1 |
| Marital Status | 'div/dep/mar': 0, 'div/sep': 1, 'mar/wid': 2, 'single': 3 |
| Applicant Age | 'adult': 0, 'senior': 1, 'young adult': 2 |
| Employment Skill Class | 'good': 0, 'highly skilled': 1, 'skilled': 2, 'unskilled': 3 |
| Self Employed/Management | 'no': 0, 'yes': 1 |
| Residential Status | 'non-resident': 0, 'resident': 1, 'unknown': 2 |
| Credit Status | 'negative': 0, 'positive': 1 |

[Figure 2B] - Checking Status Transformation

```python
if value == 'low':
    return 0
elif value == 'moderate':
    return 1
elif value == 'negative':
    return 2
elif value == 'none':
    return 3
else:
    return value

```
[Figure 2C] - Credit History Transformation

```python
if value == 'critical':
    return 0
elif value == 'delayed':
    return 1
elif value == 'paid':
    return 2
else:
    return value

```
[Figure 2D] - Credit Item Category Transformation
```python
mapping = {'business': 0, 'car': 1, 'education': 2, 'eduction': 3, 'household-equipment': 4, 
           'now car': 5, 'other': 6, 'radio/tv': 7, 'repairs': 8, 'retraining': 9}
return mapping.get(value, value)
```
[Figure 2E] - Credit Item Condition Transformation
```python
if value == 'new':
    return 0
elif value == 'unknown':
    return 1
elif value == 'used':
    return 2
else:
    return value
```
[Figure 2F] - Credit Amount Transformation
```python
mapping = {'high': 0, 'low': 1, 'moderate': 2, 'very high': 3}
return mapping.get(value, value)
```
[Figure 2G] - Savings Transformation\
```python
mapping = {'high': 0, 'low': 1, 'moderate': 2, 'moderate-high': 3, 'none-found': 4}
return mapping.get(value, value)
```
[Figure 2H] - Employment Term Transformation
```python
mapping = {'long': 0, 'medium': 1, 'medium-long': 2, 'nan': 3, 'short': 4}
return mapping.get(value, value)
```
[Figure 2I] - Employed Transformation
```python
mapping = {'no': 0, 'yes': 1}
return mapping.get(value, value)
```
[Figure 2J] - Gender Transformation
```python
mapping = {'female': 0, 'male': 1}
return mapping.get(value, value)
```
[Figure 2K] - Marital Status Transformation
```python
mapping = {'div/dep/mar': 0, 'div/sep': 1, 'mar/wid': 2, 'single': 3}
return mapping.get(value, value)
```
[Figure 2L] Applicant Age Transformation
```python
mapping = {'adult': 0, 'senior': 1, 'young adult': 2}
return mapping.get(value, value)
```
[Figure 2M] Employment Skill Class Transformation

```python
mapping = {'good': 0, 'highly skilled': 1, 'skilled': 2, 'unskilled': 3}
return mapping.get(value, value)

```

[Figure 2N] Self Employed/Management Transformation 

```python
mapping = {'no': 0, 'yes': 1}
return mapping.get(value, value)
```

[Figure 2O] - Residential Status Transformation

```python
mapping = {'non-resident': 0, 'resident': 1, 'unknown': 2}
return mapping.get(value, value)

```

[Figure 2P] - Credit Status Transformation
```python
mapping = {'negative': 0, 'positive': 1}
return mapping.get(value, value)

```

[Figure 3A] - CSV To ARFF Automated Conversion Script

```python
import pandas as pd

def convert_to_arff(df, relation_name, filename):
    """
    Convert a DataFrame to ARFF file format and save it.

    :param df: Pandas DataFrame
    :param relation_name: The name of the dataset (relation) for the ARFF file
    :param filename: File path to save the ARFF file
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

# File paths (relative)
nominal_csv_path = "./cleaned-nominal-credits.csv"
numerical_csv_path = "./cleaned-numerical-credits.csv"
nominal_arff_path = "./cleaned-nominal-credits.arff"
numerical_arff_path = "./cleaned-numerical-credits.arff"

# Reading the CSV files
nominal_df = pd.read_csv(nominal_csv_path)
numerical_df = pd.read_csv(numerical_csv_path)

# Converting nominal CSV to ARFF
convert_to_arff(nominal_df, "nominal_credits", nominal_arff_path)

# Converting numerical CSV to ARFF
convert_to_arff(numerical_df, "numerical_credits", numerical_arff_path)
```

[Figure 4A] - Data Visualisation using matplotlib

```python

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the nominal credits dataset from the CSV file
def load_data(file_path):
    return pd.read_csv(file_path)

# Restructure the dataset to include credit class distribution
def restructure_dataset(df, status_column):
    pivot_table = df.pivot_table(index=status_column, columns='Credit Status', aggfunc='size', fill_value=0)
    pivot_table.columns = ['Bad Credit', 'Good Credit']
    pivot_table['Total Credits'] = pivot_table['Bad Credit'] + pivot_table['Good Credit']
    return pivot_table.sort_values(by='Total Credits', ascending=False)

# Modified function to display percentage values on the bars
def plot_credit_distribution_percentage(df, title, xlabel, ax):
    sns.set_style("whitegrid")
    
    # Calculate percentages
    df_percentage = df[['Bad Credit', 'Good Credit']].div(df['Total Credits'], axis=0) * 100
    
    # Create bar plot
    df_percentage.plot(kind='bar', ax=ax, color=['#d9534f', '#5cb85c'], stacked=True)
    
    # Annotate bars with percentage values
    for i, (index, row) in enumerate(df_percentage.iterrows()):
        total_percentage = 0
        for j, value in enumerate(row):
            if value > 0:
                ax.text(i, total_percentage + value / 2, f'{value:.1f}%', ha='center', va='center', color='white', fontsize=10)
            total_percentage += value
    
    # Set plot properties
    ax.set_title(title, fontsize=15)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel('Percentage of Credits', fontsize=12)
    ax.legend(["Bad Credit", "Good Credit"], loc='upper left', bbox_to_anchor=(1, 1))
    ax.set_ylim(0, 100)
    ax.set_xticklabels(df.index, rotation=45, ha='right')

# Main function to run the analysis
def main():
    file_path = './cleaned-nominal-credits.csv'
    df = load_data(file_path)
    
    # Combine "Marital Status" and "Gender" into a single category
    df['Marital Status & Gender'] = df['Marital Status'] + ' & ' + df['Gender']
    
    # Create subplots for standardized visual representations
    fig, axs = plt.subplots(2, 1, figsize=(12, 12))
    
    # Personal Status: Marital Status & Gender
    combined_personal_status_df = restructure_dataset(df, 'Marital Status & Gender')
    plot_credit_distribution_percentage(combined_personal_status_df, 'Credit Class Distribution by Marital Status & Gender', 'Marital Status & Gender', axs[0])
    
    # Job Status: Employment Term
    employment_term_df = restructure_dataset(df, 'Employment Term')
    plot_credit_distribution_percentage(employment_term_df, 'Credit Class Distribution by Employment Term', 'Employment Term', axs[1])
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

```
[Figure 4B] Visualisations


![Image 22-10-2023 at 15 59](https://github.com/justinwylie033/Data-Analytics-Coursework/assets/121656622/1f30f274-6486-430f-8531-2e0036706407)

[Figure 5A] - Python Script For Categorical Statistical Analyis

```python
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

```

[Figure 5B] Terminal Output of Statistical Analysis


![B285F91D-F126-49D4-AF45-9E6B8ACCBDEF_1_201_a](https://github.com/justinwylie033/Data-Analytics-Coursework/assets/121656622/3615512a-8d8d-4459-b438-65ba329e6270)




<h1> <em> Data Cleaning Methods Invoked For Sanitation Of Banking Credit Records </em> </h1>

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






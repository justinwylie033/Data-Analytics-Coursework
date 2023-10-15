Data Analytics Coursework

<h1> Table of Changes </h1>

<table border="1">
    <thead>
        <tr>
            <th>#</th>
            <th>Attribute</th>
            <th>Identified Issue</th>
            <th>Error Type</th>
            <th>Corrective Action</th>
            <th>Old Value Example</th>
            <th>New Value Example</th>
            <th>Jython Script Used?</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Checking Status</td>
            <td>Mixed categorization (numerical and literal values)</td>
            <td>Inconsistency</td>
            <td>Standardize into clear categorical values</td>
            <td>'&lt; 0 DM', 'no checking'</td>
            <td>'negative', 'none'</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Credit History</td>
            <td>Multiple categories with similar implications</td>
            <td>Redundancy</td>
            <td>Consolidated into fewer, clear categories</td>
            <td>'no credits taken/ all credits paid back duly', 'existing credits paid back duly till now'</td>
            <td>'paid', 'paid'</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Credit Amount</td>
            <td>Numerical and widely distributed</td>
            <td>Complexity</td>
            <td>Binning into categorical values</td>
            <td>1169, 5951</td>
            <td>'low', 'moderate'</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Savings</td>
            <td>Mixed numerical and literal categorization</td>
            <td>Inconsistency</td>
            <td>Standardize into clear categorical values</td>
            <td>'.. >= 1000 DM ', 'unknown/ no savings account'</td>
            <td>'high', 'none-found'</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Personal Status</td>
            <td>Combined attributes (gender and marital status)</td>
            <td>Complexity</td>
            <td>Split into two separate columns</td>
            <td>'male single'</td>
            <td>-</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Age</td>
            <td>Numerical and widely distributed</td>
            <td>Complexity</td>
            <td>Binning into categorical values</td>
            <td>67, 22</td>
            <td>'senior', 'young adult'</td>
            <td>Yes</td>
        </tr>
    </tbody>
</table>

<h1> Steps taken to clean data </h1>

<h2> Intital cleaning of string values </h2>

```python

def clean_string(value):
    value = value.replace(',', '')  #Comma Removal
    value = value.replace('"', '').replace("'", "")  # Quotation Removal
    value = value.strip()  # Redundant Space Trimming
    value = value.replaceAll("[^a-zA-Z0-9]", "")  # Special Character Removal
    return value  # Cleansed String Returned

# Execute the changes
return clean_string(value)


```



Replace age text with numerical equivalent. 

Replace ages less than minimum credit application age and maximum living age with the medium age value as an imputation.

<h2> Imputation of Outliers Using Column Computed Median </h2>

# Remove applicant ages less than minimum credit application age and over maximum human lifespan, replace with computed column median - "33"

```python

if cells['Applicant Age'].value < 18 or cells['Applicant Age'].value > 122:
    return 33
else:
   return cells['Applicant Age'].value

```

Binned Savings values as none-observed, low, moderate, moderate-high, High

Binned employment term as N/A for unemployed, short, medium, medium-long and long

Open refine automatically Converted credit amount to integer thus removing the integer separating commas.

Age binning to get the nominal datatype.


```python

# Jython script for OpenRefine to categorize age

# Ensure the age is a number; if not, return "Invalid Age"
try:
    age = int(value)
except ValueError:
    return "Invalid Age"

# Categorise age into respective bins: Young Adult, Adult, Senior
if age < 30:
    return "Young Adult"
elif 30 <= age < 50:
    return "Adult"
else:
    return "Senior"

```
 
Binning Credit amount: 

```python

# Ensure the credit amount is a number; if not, return "Invalid Amount"
try:
    amount = int(value)
except ValueError:
    return "Invalid Amount"

# Categorize credit amount into respective bins: Low, Medium, High, Very High
if amount <= 1500:
    return "Low"
elif 1501 <= amount <= 5000:
    return "Moderate"
elif 5001 <= amount <= 10000:
    return "High"
else:
    return "Very High"

```


![image](https://github.com/justinwylie033/Data-Analytics-Coursework/assets/121656622/b43d2832-fe90-43e5-9b93-b6cc124960e3)

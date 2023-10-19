<h1> <em> Data Cleaning Methods Invoked For Sanitation Of Banking Credit Records </em> </h1>

<h2> Trimming Of White Space And Removal Of Quotation Marks </h2>

<h3>Justification</h3>

Removal of white space was a simple administrative changed that allowed for better parsing of the dataset by python and affiliated frameworks such as Pandas. It also allows for a better level of consistency throughout the dataset as if some records have mismatched quotes or similar this will be immediately resolved. The execution of this change is detailed in [Figure 1A].

<h2> Addition Of Meaningful Column Headers </h2>

<h3>Justification </h3>

The addition of column headers was perhaps and unnecessary change to some but, similar to comments in coding this was very useful in allowing the meaning of the data to be observable on first glance and in the instance of a bank this may be invaluable to less senior data science employees, not yet versed in data pattern recognition.

<h2> Universal Lower Case Conversion </h2>

<h3> Justification </h3>

The decision to convert all nominal column values to lower case was an administrative change that facilitated better indexing of the credit data within python and allowed records such as "radio/tv" and "Radio/Tv" to be merged. This was essential as computers need exact duplication for categorical conjoinment. This also allows the data to be looked at more easily in a manual manner. This is a common operation provided out of the box by openrefine. See [Figure1B].

<h3> Appendix </h3>

[Figure 1A]
``` python

def clean_string(value):
    value = value.replace(',', '')  # Remove commas
    value = value.replace('"', '').replace("'", "")  # Remove quotes
    value = value.strip()  # Trim spaces
    value = value.replaceAll("[^a-zA-Z0-9]", "")  # Remove special characters
    return value![Image 19-10-2023 at 18 47](https://github.com/justinwylie033/Data-Analytics-Coursework/assets/121656622/0dc7689c-e1df-40dc-adcc-7219803817b3)


# Use the function
return clean_string(value)

```
[Figure 1B]
![Steps Taken To convert columns to lowercase](/Images/Lowercase.jpg)





<h1> <em> Data Cleaning Methods Invoked For Sanitation Of Banking Credit Records </em> </h1>

<h2> Trimming Of White Space And Removal Of Quotation Marks </h2>

<h3>Justification</h3>

Removal of white space was a simple administrative changed that allowed for better parsing of the dataset by python and affiliated frameworks such as Pandas. It also allows for a better level of consistency throughout the dataset as if some records have mismatched quotes or similar this will be immediately resolved. The execution of this change is detailed in [Figure 1A].

<h2>  </h2>

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



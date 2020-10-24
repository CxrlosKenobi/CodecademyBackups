# Lambda functions in Python
add_two = lambda my_input: my_input + 2
	lambda my_input: <my_input modified somehow>

lambda x: [OUTCOME IF TRUE] if [CONDITIONAL] else [OUTCOME IF FALSE]

# Pandas cheatsheet

import pandas as pd 

df1 = pd.DataFrame({
    'name': ['John Smith', 'Jane Doe', 'Joe Schmo'],
    'address': ['123 Main St.', '456 Maple Ave.', '789 Broadway'],
    'age': [34, 28, 51]
})

df2 = pd.DataFrame([
    ['John Smith', '123 Main St.', 34],
    ['Jane Doe', '456 Maple Ave.', 28],
    ['Joe Schmo', '789 Broadway', 51]
    ],
    columns=['name', 'address', 'age'])

pd.read_csv('my-csv-file.csv') # Read a CSV file
df.to_csv('new-csv-file.csv') # Save data to CSV

df.head() # First rows 
df.info() # Info about the dataframe 'df'

df.MyColumnName # Select a column 
df['MyColumnName'] # Select a column

df[['Column1', 'Column2']] # Select multiple columns

df.iloc[3] # Selecting range(0,3) rows 

df[(df.age < 30) |
   (df.name == 'Martha Jones')] # Selecting rows with logic 

df[df.name.isin(['Martha Jones',
     'Rose Tyler',
     'Amy Pond'])] # Selecting rows with logic II

df.reset_index(drop=True, inplace=True) # Setting index

df['Quantity'] = [100, 150, 50, 35] # Adding a column

df['Sales Tax'] = df.Price * 0.075 # Adding a column II

from string import upper
df['Name'] = df.Name.apply(upper) # Column operation; Upper 'Name' column

df.columns = ['NewName1', 'NewName2', 'NewName3'] # Renaming Columns I (You must rename all columns, not only one)
df.rename(columns={'old_name': 'new_name', 'old_name2': 'new_name2'}) # Renaming Columns II

inventory['in_stock'] = inventory.apply(lambda row: \
True if row.quantity > 0 \
else False, axis=1) # Pandas and Lambda functions in play

df.column_name.command() # Built-in calculations

new_df = pd.merge(orders, customers) # Inner merge II
new_df = orders.merge(customers).merge(orders).merge(prices) # Inner merge III
pd.merge(
    orders,
    customers.rename(columns={'id': 'customer_id'})) # Specific columns merge
pd.merge(
    orders,
    customers,
    left_on='customer_id',
    right_on='id',
    suffixes=['_order', '_customer']) # Specific columns merge II 

pd.merge(company_a, company_b, how='outer') # Outer join
pd.merge(company_a, company_b, how='left') # Left join
pd.merge(company_a, company_b, how="right") # Right join

pd.concat([df1, df2]) # Conceatenate data frames (only works if all of the columns are the same in all of the DataFrames)

# Create a new dataframe from the result set
df = pd.read_sql_query('''SELECT * from students;''', connection)

# Show new dataframe
print(df)

# Create a new dataframe from the result set
df = pd.read_sql_query('''SELECT * from students WHERE major_code = 21;''', connection)

# Show new dataframe
print(df)


# Strings manipulation
    .upper(), .title(), and .lower() # adjust the casing of your string.
    .split() # takes a string and creates a list of substrings.
    .join() # takes a list of strings and creates a string.
    .strip() # cleans off whitespace, or other noise from the beginning and end of a string.
    .replace() # replaces all instances of a character/string in a string with another character/string.
    .find() # searches a string for a character/string and returns the index value that character/string is found at.
    .format() and f-strings # allow you to interpolate a string with variables.


# Write your reverse_string function here:
def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse
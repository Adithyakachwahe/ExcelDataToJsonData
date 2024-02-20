import pandas as pd

# Read Excel file into a DataFrame
excel_file = 'Book2.xlsx'
df = pd.read_excel(excel_file)

# Convert DataFrame to JSON
json_data = df.to_json(orient='records')

# Write JSON data to a file
with open('output.json', 'w') as json_file:
    json_file.write(json_data)

print('Conversion successful! JSON data saved to output.json')

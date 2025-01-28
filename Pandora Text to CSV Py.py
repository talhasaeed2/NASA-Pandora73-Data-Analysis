import pandas as pd
from datetime import datetime, timedelta
import re

# Define the path to the new formaldehyde file
file_path = 'D:/PGN/TroHCHO Pandora73s1_Islamabad-NUST_L2_rfuh5p1-8.txt'

# Identify the start of the numerical data using a regular expression
data_lines = []
data_pattern = re.compile(r'^\d{8}T\d{6}\.\dZ')  # Matches the start of data lines

with open(file_path, 'r') as file:
    for line in file:
        if data_pattern.match(line):
            data_lines.append(line.strip())

# Create a DataFrame from the extracted lines
df_full = pd.DataFrame([x.split() for x in data_lines])

# Convert the "Fractional days since 1-Jan-2000 UT midnight" column
base_date = datetime(2000, 1, 1)
df_full[1] = df_full[1].astype(float).apply(lambda x: base_date + timedelta(days=x))
df_full.rename(columns={1: 'Converted Date'}, inplace=True)

# Select specified columns for formaldehyde and rename for clarity
# Adjust column indices based on the structure for formaldehyde data
selected_columns_df = df_full.iloc[:, [1, 41, 44, 49]].copy()
selected_columns_df.columns = [
    'Converted Date',
    'L2 Data Quality Flag for Formaldehyde',
    'Formaldehyde Surface Concentration [mol/m3]',
    'Formaldehyde Tropospheric Vertical Column Amount [moles per square meter]'
]

# Output the selected formaldehyde data to a CSV file
output_csv_path = 'D:/PGN/Pandora Trop HCHO.csv'
selected_columns_df.to_csv(output_csv_path, index=False)

print(f"Formaldehyde data saved to {output_csv_path}")

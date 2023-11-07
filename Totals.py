import pandas as pd

# Load your CSV file
df = pd.read_csv('updated_data.csv')

# Convert 'ArArrestDate' to a datetime object
df['ArArrestDate'] = pd.to_datetime(df['ArArrestDate'])

# Create a new column with just the date part of 'ArArrestDate'
df['Date'] = df['ArArrestDate'].dt.date

# Filter out sectors with 4 characters or longer and whose last character is not '0'
df = df[(df['Sector'].str.len() < 4) & (df['Sector'].str.endswith('0'))]

# Group by 'Sector', week number, and count the unique 'ArrestNumber' for each group
df['Week'] = df['ArArrestDate'].dt.strftime('%Y-%U')
arrest_counts = df.groupby(['Sector', 'Week'])['ArrestNumber'].nunique().reset_index()

# Create a pivot table to reshape the data with 'Sector', 'Week', and 'TotalArrests' columns
pivot_table = arrest_counts.pivot(index='Sector', columns='Week', values='ArrestNumber')

# Fill missing values with 0
pivot_table = pivot_table.fillna(0)

# Reset the index to create a clean output DataFrame
pivot_table = pivot_table.reset_index()

# Melt the DataFrame to have the desired format
result_df = pd.melt(pivot_table, id_vars=['Sector'], var_name='Week', value_name='TotalArrests')

# Sort the result by 'Sector' and 'Week'
result_df = result_df.sort_values(by=['Sector', 'Week'])

# Add 'Unarmed', 'Armed', 'DrugRelated', 'Male', and 'Female' columns based on their respective values
df['Unarmed'] = (df['ArWeapon'] == 'Unarmed') | df['ArWeapon'].isna()
df['Armed'] = (df['ArWeapon'] != 'Unarmed') & ~df['ArWeapon'].isna()
df['DrugRelated'] = df['DrugRelated'] == 'Yes'
df['Male'] = df['Sex'] == 'Male'
df['Female'] = df['Sex'] == 'Female'

# Group by 'Sector', week number, and sum the 'Unarmed', 'Armed', 'DrugRelated', 'Male', and 'Female' columns
columns_to_sum = ['Unarmed', 'Armed', 'DrugRelated', 'Male', 'Female']
grouped_data = df.groupby(['Sector', 'Week'])[columns_to_sum].sum().reset_index()

# Merge the counts with the existing DataFrame
result_df = pd.merge(result_df, grouped_data, on=['Sector', 'Week'], how='left')

# Fill missing values in the columns with 0
result_df[columns_to_sum] = result_df[columns_to_sum].fillna(0)

# Add 'White', 'Black', and 'Hispanic or Latino' columns based on the 'Race' values
df['White'] = df['Race'] == 'White'
df['Black'] = df['Race'] == 'Black'
df['Hispanic or Latino'] = df['Race'] == 'Hispanic or Latino'

# Group by 'Sector', week number, and sum the 'White', 'Black', and 'Hispanic or Latino' columns
race_columns_to_sum = ['White', 'Black', 'Hispanic or Latino']
race_grouped_data = df.groupby(['Sector', 'Week'])[race_columns_to_sum].sum().reset_index()

# Merge the race counts with the existing DataFrame
result_df = pd.merge(result_df, race_grouped_data, on=['Sector', 'Week'], how='left')

# Fill missing values in the race columns with 0
result_df[race_columns_to_sum] = result_df[race_columns_to_sum].fillna(0)

# Add 'PUBLIC INTOXICATION', 'DRUG/ NARCOTIC VIOLATIONS', 'DUI', and 'ALL OTHER OFFENSES' columns
nibrs_crime_columns = ['PUBLIC INTOXICATION', 'DRUG/ NARCOTIC VIOLATIONS', 'DUI', 'ALL OTHER OFFENSES']

for column in nibrs_crime_columns:
    df[column] = df['NIBRS Crime'] == column

# Group by 'Sector', week number, and sum the 'PUBLIC INTOXICATION', 'DRUG/ NARCOTIC VIOLATIONS', 'DUI', and 'ALL OTHER OFFENSES' columns
nibrs_crime_grouped_data = df.groupby(['Sector', 'Week'])[nibrs_crime_columns].sum().reset_index()

# Merge the NIBRS crime counts with the existing DataFrame
result_df = pd.merge(result_df, nibrs_crime_grouped_data, on=['Sector', 'Week'], how='left')

# Fill missing values in the NIBRS crime columns with 0
result_df[nibrs_crime_columns] = result_df[nibrs_crime_columns].fillna(0)

# Save the result to a new CSV file
result_df.to_csv('your_output8.csv', index=False)

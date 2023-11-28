import math
from scipy.stats import ttest_ind
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Read 'arrests_integrated.csv' into a DataFrame
arrests_integrated_df = pd.read_csv('arrests_integrated.csv')

total_rows_before = arrests_integrated_df.shape[0]
print(f"\nTotal number of rows in the dataset: {total_rows_before}\n\n")

# Rename the column 'Responding Officer #1 Badge No' to 'Res Offc1 Badge No'
arrests_integrated_df = arrests_integrated_df.rename(columns={' Responding Officer #1  Badge No': 'Res Offc1 Badge No'})

# List of columns to keep
columns_to_keep = [
    'IncidentNum', 'ArrestNumber', 'ArArrestDate', 'ArArrestTime',
    'ArLZip', 'ArLBeat', 'ArPremises', 'ArWeapon', 'AgeAtArrestTime',
    'HZIP', 'HBeat', 'Weight', 'Hair', 'Eyes', 'Race', 'Ethnic', 'Sex',
    'DrugRelated', 'DrugType', 'NIBRS Crime Against',
    'NIBRS Code', 'FullMoon', 'Height' ]

# Keep only the specified columns
arrests_integrated_df = arrests_integrated_df[columns_to_keep]
#------------------------------------------------------------------------------------------------------------------
# Replace infinite values with NaN in the 'Weight' column
arrests_integrated_df['Weight'].replace([np.inf, -np.inf], np.nan, inplace=True)

# Drop rows with NaN values in the 'Weight' column
arrests_integrated_df = arrests_integrated_df.dropna(subset=['Weight'])

arrests_integrated_df = arrests_integrated_df[pd.to_numeric(arrests_integrated_df['Weight'], errors='coerce').notnull()]

# Convert the 'Weight' column to integers
arrests_integrated_df['Weight'] = pd.to_numeric(arrests_integrated_df['Weight'], errors='coerce').astype(int)

# Remove rows where 'Weight' is less than 50
arrests_integrated_df = arrests_integrated_df[arrests_integrated_df['Weight'] >= 50]
#------------------------------------------------------------------------------------------------------------------
# Replace infinite values with NaN in the 'Weight' column
arrests_integrated_df['HZIP'].replace([np.inf, -np.inf], np.nan, inplace=True)

# Drop rows with NaN values in the 'Weight' column
arrests_integrated_df = arrests_integrated_df.dropna(subset=['HZIP'])

arrests_integrated_df = arrests_integrated_df[pd.to_numeric(arrests_integrated_df['HZIP'], errors='coerce').notnull()]

# Convert the 'Weight' column to integers
arrests_integrated_df['HZIP'] = pd.to_numeric(arrests_integrated_df['HZIP'], errors='coerce').astype(int)
#------------------------------------------------------------------------------------------------------------------
# FIX ISSUE WITH DROPPING TO MUCH
# Replace infinite values with NaN in the 'Weight' column
# arrests_integrated_df['HBeat'].replace([np.inf, -np.inf], np.nan, inplace=True)
#
# # Drop rows with NaN values in the 'Weight' column
# arrests_integrated_df = arrests_integrated_df.dropna(subset=['HBeat'])

# arrests_integrated_df = arrests_integrated_df[pd.to_numeric(arrests_integrated_df['HBeat'], errors='coerce').notnull()]
#
# # Convert the 'Weight' column to integers
arrests_integrated_df['HBeat'] = pd.to_numeric(arrests_integrated_df['HBeat'], errors='coerce').astype('Int64')
#------------------------------------------------------------------------------------------------------------------
# # Replace infinite values with NaN in the 'Weight' column
# arrests_integrated_df['AgeAtArrestTime'].replace([np.inf, -np.inf], np.nan, inplace=True)
#
# # Drop rows with NaN values in the 'Weight' column
# arrests_integrated_df = arrests_integrated_df.dropna(subset=['AgeAtArrestTime'])
#
# arrests_integrated_df = arrests_integrated_df[pd.to_numeric(arrests_integrated_df['AgeAtArrestTime'], errors='coerce').notnull()]

# Convert the 'Weight' column to integers
arrests_integrated_df['AgeAtArrestTime'] = pd.to_numeric(arrests_integrated_df['AgeAtArrestTime'], errors='coerce').astype('Int64')
#------------------------------------------------------------------------------------------------------------------
# Define a regular expression pattern for valid 'ArArrestTime'
time_pattern = r'^[0-9]{1,2}:[0-9]{2}$'
# Use str.match to filter rows based on the pattern
arrests_integrated_df = arrests_integrated_df[arrests_integrated_df['ArArrestTime'].str.match(time_pattern, na=False)]
#-----------------------------------------------------------------------------------------------------------------------
# Replace infinite values with NaN in the 'Weight' column
arrests_integrated_df['ArLZip'].replace([np.inf, -np.inf], np.nan, inplace=True)

# Drop rows with NaN values in the 'Weight' column
arrests_integrated_df = arrests_integrated_df.dropna(subset=['ArLZip'])

arrests_integrated_df = arrests_integrated_df[pd.to_numeric(arrests_integrated_df['ArLZip'], errors='coerce').notnull()]

# Remove the period from the end of each value in 'ArLZip'
arrests_integrated_df['ArLZip'] = arrests_integrated_df['ArLZip'].astype(str).str.rstrip('.')

# Convert the 'Weight' column to integers
arrests_integrated_df['ArLZip'] = pd.to_numeric(arrests_integrated_df['ArLZip'], errors='coerce').astype(int)
#----------------------------------------------------------------------------------------------------------------------
# # Replace infinite values with NaN in the 'Weight' column
# arrests_integrated_df['ArLBeat'].replace([np.inf, -np.inf], np.nan, inplace=True)
#
# # Drop rows with NaN values in the 'Weight' column
# arrests_integrated_df = arrests_integrated_df.dropna(subset=['ArLBeat'])
#
# arrests_integrated_df = arrests_integrated_df[pd.to_numeric(arrests_integrated_df['ArLBeat'], errors='coerce').notnull()]
#
# # Remove the period from the end of each value in 'ArLZip'
# arrests_integrated_df['ArLBeat'] = arrests_integrated_df['ArLBeat'].astype(str).str.rstrip('.')
#
# # Convert the 'Weight' column to integers
arrests_integrated_df['ArLBeat'] = pd.to_numeric(arrests_integrated_df['ArLBeat'], errors='coerce').astype('Int64')
#----------------------------------------------------------------------------------------------------------------------
# Mapping of weapon categories
weapon_mapping = {
    'Unarmed': 'unarmed',
    'THREATS': 'unarmed',
    'Handgun': 'firearm',
    'Firearm (Type Not Stated)': 'firearm',
    'Gun': 'firearm',
    'Other Firearm': 'firearm',
    'Shotgun ': 'firearm',
    'Knife - Pocket': 'knife',
    'Knife - Butcher': 'knife',
    'Knife - Other': 'knife',
    'Club': 'other melee',
    'Stabbing Instrument': 'knife',
    'Lethal Cutting Instrument': 'knife',
    'Other': 'other',
    'Drugs': 'other',
    'Vehicle': 'other',
    'Rock': 'other',
    'Poison': 'other',
    'Burn': 'other',
    'Missle/Arrow': 'other',
    'Explosives ': 'other',
    'Hands/Feet': 'hands/ feet',
    'Strangulation': 'hands/ feet'
}

# Map weapon categories and create 'WeaponCategory' column
arrests_integrated_df['ArWeapon'] = arrests_integrated_df['ArWeapon'].map(weapon_mapping)
# Remove rows where 'ArWeapon' is '33'
arrests_integrated_df = arrests_integrated_df[arrests_integrated_df['ArWeapon'] != '33']
#-----------------------------------------------------------------------------------------------------------------------

# Print unique values and their counts for each column
for column_name in arrests_integrated_df.columns:
    print(f"\nUnique values and counts for column '{column_name}':")
    print(arrests_integrated_df[column_name].value_counts())

# # Print unique values for each column
# for column_name in arrests_integrated_df.columns:
#     print(f"\nUnique values for column '{column_name}':")
#     print(arrests_integrated_df[column_name].unique())

total_rows_after = arrests_integrated_df.shape[0]
print(f"\n\nTotal number of rows in the dataset: {total_rows_after}\n")

#-----------------------------------------------------------------------------------------------------------------------
# Descriptive statistics for eye colors during a full moon
full_moon_eye_colors = arrests_integrated_df[arrests_integrated_df['FullMoon'] == 1]['Eyes']
print(full_moon_eye_colors.describe())

# Descriptive statistics for height during a full moon
full_moon_heights = arrests_integrated_df[arrests_integrated_df['FullMoon'] == 1]['Weight']
print(full_moon_heights.describe())
#-----------------------------------------------------------------------------------------------------------------------

# Exclude non-numeric columns from correlation analysis
numeric_columns = arrests_integrated_df.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = arrests_integrated_df[numeric_columns].corr()

# Display correlation matrix
print(correlation_matrix)

#-----------------------------------------------------------------------------------------------------------------------
# Boxplot for eye colors during a full moon
sns.boxplot(x='FullMoon', y='Eyes', data=arrests_integrated_df)
plt.show()

# Histogram for height during a full moon
sns.histplot(data=arrests_integrated_df[arrests_integrated_df['FullMoon'] == 1], x='Weight', kde=True)
plt.show()
#-----------------------------------------------------------------------------------------------------------------------

# Hypothesis test for the difference in height between full moon and non-full moon arrests
full_moon_heights = arrests_integrated_df[arrests_integrated_df['FullMoon'] == 1]['Weight']
non_full_moon_heights = arrests_integrated_df[arrests_integrated_df['FullMoon'] == 0]['Weight']

t_stat, p_value = ttest_ind(full_moon_heights, non_full_moon_heights, nan_policy='omit')
print(f"\n\nT-statistic: {t_stat}, p-value: {p_value}\n")
#-----------------------------------------------------------------------------------------------------------------------

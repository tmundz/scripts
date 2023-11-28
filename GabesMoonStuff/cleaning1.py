import pandas as pd

# Read the 'Police_Arrests.csv' file
arrests_data = pd.read_csv('police_arrest_deleted.csv', dtype={30: str, 46: str})

# Read the 'full_moons.csv' file
full_moons_data = pd.read_csv('full_moons.csv')

# Preprocess the 'ArArrestDate' column in arrests_data
arrests_data['ArArrestDate'] = pd.to_datetime(arrests_data['ArArrestDate'], errors='coerce')

# Preprocess the 'Date' column in full_moons_data to match the new date format
full_moons_data['Date'] = pd.to_datetime(full_moons_data['Date'], format='%d %B %Y', errors='coerce')

# Filter full moon dates within the range of 2015-2022
full_moons_range = full_moons_data[
    (full_moons_data['Date'].dt.year >= 2015) & (full_moons_data['Date'].dt.year <= 2022)]

# Add a new column 'FullMoon' to arrests_data and initialize it with 0
arrests_data['FullMoon'] = 0

# Iterate through each row in arrests_data
for index, row in arrests_data.iterrows():
    arrest_date = row['ArArrestDate']

    # Check if the arrest date is in the full_moons_range
    if any(full_moons_range['Date'] == arrest_date):
        arrests_data.at[index, 'FullMoon'] = 1

# Alternatively, you can use the isin() method for a more concise solution:
# arrests_data['FullMoon'] = arrests_data['ArArrestDate'].isin(full_moons_range['Date']).astype(int)

# Display the integrated dataset
full_moon_entries = arrests_data[arrests_data['FullMoon'] == 1]
print(full_moon_entries)
arrests_data.to_csv('arrests_integrated.csv', index=False)



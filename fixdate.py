import pandas as pd

# Read the CSV file
df = pd.read_csv('future prediction forecast horizon = 12.csv')

# Split the 'temporal_id' column into 'year', 'week', and 'offset' columns
df[['year', 'week+offset']] = df['temporal id'].str.split('-', expand=True)

# Split the 'week+offset' column into 'week' and 'offset' columns
df[['week', 'offset']] = df['week+offset'].str.split('+', expand=True)

# Convert 'week' and 'offset' columns to integers
df['week'] = df['week'].astype(int)
df['offset'] = df['offset'].astype(int)

# Add 'offset' to 'week' to get the final 'week' value
df['week'] = df['week'] + df['offset']

# Drop the 'week+offset' and 'offset' columns
df = df.drop(columns=['week+offset', 'offset'])

# Combine 'year' and 'week' to create the 'temporal_id' column in the desired format
df['temporal id'] = df['year'] + '-' + df['week'].apply(lambda x: str(x).zfill(2))

# Drop the 'year' and 'week' columns if not needed
df = df.drop(columns=['year', 'week'])

# Print the resulting DataFrame
df.to_csv('Prediction_fixed.csv', index=False)
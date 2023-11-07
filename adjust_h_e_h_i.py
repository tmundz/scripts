import pandas as pd
# Define the functions for mapping string values to numeric values
def get_hair(hair_str):
    hair = {"Black": 1, "Brown": 2, "Blonde": 3, "White": 4, "Red": 5, "Other": 6}
    if pd.isna(hair_str):
        return 0
    if hair_str.replace(".", "", 1).isdigit():
        # Handle numeric values that may be represented as floats
        return int(float(hair_str))
    return hair.get(hair_str, 0)

def get_eye(eye_str):
    eye = {"Black": 1, "Brown": 2, "Hazel": 3, "Green": 4, "Blue": 5, "Unknown": 6, "Other": 6}
    if pd.isna(eye_str):
        return 0
    if eye_str.replace(".", "", 1).isdigit():
        # Handle numeric values that may be represented as floats
        return int(float(eye_str))
    return eye.get(eye_str, 0)

# Function to convert height values to feet and inches with 2 decimal places
def get_height(height_str):
    if isinstance(height_str, str) and '-' in height_str:
        feet, inches = height_str.split('-')
        if feet == '':
            return 0
        if inches == '':
            return float(feet)
        return round(float(feet) + (float(inches) / 12.0), 2)
    else:
        if 'nan' in str(height_str):
            return height_str
        return float(height_str)
    
df = pd.read_csv("Police_Arrests_&_Incidents_Clean.csv")
# Apply the functions to create new columns while adding safeguards
# Apply the functions to create new columns while adding safeguards and handling NaN values
df['IncidentNum new'] = df['IncidentNum'].str.replace('-', '')
df['Hair Numeric'] = df.apply(lambda row: get_hair(row['Hair']), axis=1)
df['Eye Numeric'] = df.apply(lambda row: get_eye(row['Eyes']), axis=1)
df['Height in Feet'] = df.apply(lambda row: get_height(row['Height']), axis=1)

# Save the DataFrame with the new columns to a new CSV file
df.to_csv('police_arrest_adjusted.csv', index=False)
import pandas as pd

# Load your CSV file into a DataFrame
df = pd.read_csv('Police_Arrests_&_Incidents_Clean.csv')

# List of columns to delete
columns_to_delete = [
    'Responding Officer #1  Badge No', 'Responding Officer #1  Name',
    'Responding Officer #2 Badge No', 'Responding Officer #2  Name',
    'Reporting Officer Badge No', 'Assisting Officer Badge No',
    'Reviewing Officer Badge No', 'Element Number Assigned',
    'Offense Status', 'X Coordinate', 'Y Cordinate', 'Zip Code',
    'City', 'State', 'HRA', 'Offense Status', 'ArLRA',
    'RMS Code', 'Criminal Justice Information Service Code',
    'Penal Code', 'Gang Related Offense', 'Weapon Used',
    'Year of Incident', 'Service Number ID', 'Watch',
    'Call (911) Problem', 'Type of Property', 'Incident Address',
    'Apartment Number', 'Reporting Area', 'Beat', 'Division',
    'Sector', 'Council District', 'Victim Ethnicity',
    'ArADOW', 'Age', 'ArLDistrict', 'ArLSector', 'Location1',
    'Transport1', 'Transport2', 'ArAction', 'HApt',
    'ArresteeName', 'Element Number Assigned',
    'ArCurrLoc', 'ClothingWorn', 'UpZDate',
    'Service Number ID', 'Date2 of Occurrence ',
    'Person Involvement Type', 'CFS Number', 'Community',
    'Target Area Action Grids'
]

# Delete the specified columns
df.drop(columns=columns_to_delete, inplace=True)

# Save the modified DataFrame back to a CSV file
df.to_csv('police_arrest_deleted.csv', index=False)
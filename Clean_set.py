import pandas as pd

df = pd.read_csv('Police_Arrests_&_Incidents.csv')

remove_list = ['ArLCounty',
'ArOSR',
'ArResisted',
'ArCond',
'ArMedFlag',
'ArMedLoc',
'ArOpComm',
'NickName',
'AliasName',
'Tatoo',
'TatooComment',
'Occupation',
'JobSchStatus',
'Employer',
'Drug',
'Expunged',
'Date1 of Occurrence',
'Year1 of Occurrence',
'Month1 of Occurence',
'Day1 of the Week',
'Time1 of Occurrence',
'Day1 of the Year',
'Year2 of Occurrence',
'Month2 of Occurence',
'Day2 of the Week',
'Time2 of Occurrence',
'Day2 of the Year',
'Date incident created',
'Offense Entered Year',
'Offense Entered Month',
'Offense Entered Day of the Week',
'Offense Entered Time',
'Offense Entered  Date/Time',
'Call Received Date Time',
'Call Date Time',
'Call Cleared Date Time',
'Call Dispatch Date Time',
'Special Report (Pre-RMS)',
'Modus Operandi (MO)',
'Hate Crime',
'Hate Crime Description',
'UCR Offense Name',
'UCR Offense Description',
'UCR Code',
'Offense Type',
'Update Date', 
'Unnamed: 150', 
'Unnamed: 151', 
'Unnamed: 152', 
'Unnamed: 153', 
'Unnamed: 154', 
'Unnamed: 155', 
'Unnamed: 156', 
'Unnamed: 157', 
'Unnamed: 158', 
'Unnamed: 159', 
'Unnamed: 160', 
'Unnamed: 161', 
'Unnamed: 162', 
'Unnamed: 163', 
'Unnamed: 164', 
'Unnamed: 165', 
'Unnamed: 166', 
'Unnamed: 167', 
'Unnamed: 168', 
'Unnamed: 169', 
'Unnamed: 170', 
'Unnamed: 171', 
'Unnamed: 172', 
'Unnamed: 173', 
'Unnamed: 174', 
'Unnamed: 175',
'Transport3',
'Search1',
'ArrestYr',
'ArBkDate',
'ArLApt',
'ArLCity',
'CFS_Number',
'Drug Related Istevencident']

#Remove Listed columns
df = df.drop(remove_list, axis=1)


#save as new csv
df.to_csv('Police_Arrests_&_Incidents_Clean.csv', index=False)

#print list of column names
print(df.columns.tolist())

    
print()
print()



# Function to identify column pairs with over 80% matching data as strings
def identify_high_match_string_data_column_pairs(df, threshold=80):
    matching_data_column_pairs = []

    # Iterate through the columns
    for i in range(len(df.columns)):
        for j in range(i + 1, len(df.columns)):
            column1_values = df[df.columns[i]].astype(str)
            column2_values = df[df.columns[j]].astype(str)

            # Count the matching values
            matching_count = (column1_values == column2_values).sum()

            # Calculate the percentage match
            percentage_match = (matching_count / len(df)) * 100

            if percentage_match >= threshold:
                matching_data_column_pairs.append((df.columns[i], df.columns[j], percentage_match))

    return matching_data_column_pairs

# Identify pairs of columns with over 80% matching data as strings
matching_data_column_pairs = identify_high_match_string_data_column_pairs(df, threshold=80)

if matching_data_column_pairs:
    print("Pairs of columns with over 80% matching data as strings:")
    for pair in matching_data_column_pairs:
        print(f"{pair[0]} and {pair[1]} have {pair[2]:.2f}% matching data.")
else:
    print("No pairs of columns with over 80% matching data as strings found.")
    
    
print()
print()

# Calculate the percentage of missing data for each column
missing_percentage = df.isnull().mean() * 100

# Find columns with over 20% missing data
columns_with_missing_data = missing_percentage[missing_percentage > 20]

if not columns_with_missing_data.empty:
    print("Columns with over 20% missing data:")
    for column, percentage in columns_with_missing_data.items():
        print(f"{column}: {percentage:.2f}% missing")
else:
    print("No columns with over 20% missing data found.")
  




import pandas as pd 

#read csv
df = pd.read_csv('Police_Arrests_&_Incidents_Clean.csv')


# Function to summarize the dataset and save to a file
def summarize_and_save_to_file(df, output_file):
    summary = {}

    # Number of columns
    summary['Number of Columns'] = len(df.columns)

    # Number of unique values in each column
    summary['Unique Values in Each Column'] = df.nunique()

    # Percentage of missing values in each column
    summary['Percentage Missing Values'] = (df.isnull().mean() * 100).round(2)

    # Top 5 most repeated entries in each column and their percentages
    top_repeated_entries = {}
    for column in df.columns:
        top_entries = df[column].value_counts().head(5)
        percentages = (top_entries / len(df[column])) * 100
        top_repeated_entries[column] = list(zip(top_entries.index, top_entries.values, percentages.values.round(2)))

    summary['Top 5 Most Repeated Entries'] = top_repeated_entries

    # Save the summary to the specified output file
    with open(output_file, 'w') as file:
        for key, value in summary.items():
            file.write(f"{key}:\n")
            if isinstance(value, pd.Series):
                file.write(value.to_string() + '\n')
            elif isinstance(value, dict):
                for column, entries in value.items():
                    file.write(f"  {column}:\n")
                    for entry, count, percent in entries:
                        file.write(f"    {entry}: Count={count}, Percentage={percent}%\n")
            else:
                file.write(str(value) + '\n')

# Specify the output file path
output_file = 'dataset_summary.txt'

# Generate dataset summary and save to file
summarize_and_save_to_file(df, output_file)

# Print a confirmation message
print(f"Summary saved to {output_file}")
    
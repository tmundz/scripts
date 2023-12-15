import math
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# # Read 'arrests_final.csv' into a DataFrame
# arrests_df = pd.read_csv('arrests_final.csv')
#
# # Extract relevant columns for analysis
# columns_for_analysis = ['ArArrestTime', 'ArPremises', 'ArWeapon',
#                         'Hair', 'Eyes', 'Race', 'Ethnic', 'Sex',
#                         'DrugRelated', 'DrugType', 'NIBRS Crime Against', 'NIBRS Code']
#
# numeric_columns = ['ArLZip', 'HZIP', 'AgeAtArrestTime', 'Weight', 'HBeat', 'FullMoon']
# short_numeric_columns = ['ArZip', 'HomeZIP', 'Age', 'Weight', 'Beat', 'FullMoon']
#
# categorical_columns = ['ArArrestTime', 'ArPremises', 'ArWeapon',
#     'Hair', 'Eyes', 'Race', 'Ethnic', 'Sex',
#     'DrugRelated', 'DrugType', 'NIBRS Crime Against', 'NIBRS Code']
#
# # Create correlation heatmap with shortened names
# correlation_matrix = arrests_df[numeric_columns].corr()
# correlation_matrix = correlation_matrix.rename(
#     columns=dict(zip(numeric_columns, short_numeric_columns)),
#     index=dict(zip(numeric_columns, short_numeric_columns))
# )
#
# # Increase the figure size
# plt.figure(figsize=(14, 10))
#
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
# plt.title('Correlation Heatmap of Numeric Columns')
#
# # Rotate x and y axis labels for better visibility
# plt.xticks(rotation=45, ha='right')
# plt.yticks(rotation=0)
#
# plt.show()
#
# # Frequent pattern analysis
# data_for_analysis = arrests_df[columns_for_analysis].astype(str)
#
# # Convert categorical data into binary format (one-hot encoding)
# te = TransactionEncoder()
# data_encoded = te.fit(data_for_analysis.apply(
#     lambda x: x.dropna().tolist(), axis=1)).transform(data_for_analysis.apply(lambda x: x.dropna().tolist(), axis=1))
# df_encoded = pd.DataFrame(data_encoded, columns=te.columns_)
#
# # Apply Apriori algorithm to find frequent itemsets
# min_support = 0.01  # Adjust as needed
# frequent_itemsets = apriori(df_encoded, min_support=min_support, use_colnames=True)
#
# # Generate association rules
# rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)
#
# # Visualization of frequent itemsets
# plt.figure(figsize=(12, 6))
# plt.barh(range(len(frequent_itemsets)), frequent_itemsets['support'], align='center')
# plt.yticks(range(len(frequent_itemsets)), frequent_itemsets['itemsets'].apply(lambda x: ', '.join(map(str, x))))
# plt.xlabel('Support')
# plt.title('Frequent Itemsets')
# plt.show()
#
# # Visualization of association rules
# plt.figure(figsize=(12, 6))
# plt.scatter(rules['support'], rules['confidence'], alpha=0.5)
# plt.xlabel('Support')
# plt.ylabel('Confidence')
# plt.title('Association Rules')
# plt.show()

# Read 'arrests_final.csv' into a DataFrame
arrests_df = pd.read_csv('arrests_final.csv')

# Print unique values and their counts for each column
# for column_name in arrests_df.columns:
#     print(f"\nUnique values and counts for column '{column_name}':")
#     print(arrests_df[column_name].value_counts())
total_rows_before = arrests_df.shape[0]
print(f"\nTotal number of rows in the dataset: {total_rows_before}\n\n")


# Print columns with NaN entries
nan_columns = arrests_df.columns[arrests_df.isna().any()].tolist()
print(f"\nColumns with NaN entries: {nan_columns}")

# Count and print NaN entries for each column
nan_counts = arrests_df.isna().sum()
for column_name, nan_count in nan_counts.items():
    print(f"Column '{column_name}' has {nan_count} NaN entries.")

# Drop rows with NaN entries only for the identified columns
arrests_df = arrests_df.dropna(subset=nan_columns)

total_rows_after = arrests_df.shape[0]
print(f"\nTotal number of rows in the dataset: {total_rows_after}\n\n")

# Extract relevant columns for analysis
columns_for_analysis = ['ArArrestTime', 'ArPremises', 'ArWeapon',
                        'Hair', 'Eyes', 'Race', 'Ethnic', 'Sex',
                        'DrugType', 'NIBRS Crime Against', 'NIBRS Code', 'Sector']

numeric_columns = ['ArLZip', 'HZIP', 'AgeAtArrestTime', 'Weight', 'HBeat', 'Sector']
short_numeric_columns = ['ArZip', 'HomeZIP', 'Age', 'Weight', 'Beat', 'Sector']

categorical_columns = ['ArArrestTime', 'ArPremises', 'ArWeapon',
    'Hair', 'Eyes', 'Race', 'Ethnic', 'Sex',
    'DrugRelated', 'DrugType', 'NIBRS Crime Against', 'NIBRS Code']

# Create correlation heatmap with shortened names
correlation_matrix = arrests_df[numeric_columns].corr()
correlation_matrix = correlation_matrix.rename(
    columns=dict(zip(numeric_columns, short_numeric_columns)),
    index=dict(zip(numeric_columns, short_numeric_columns))
)

# Increase the figure size
plt.figure(figsize=(14, 10))

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap of Numeric Columns')

# Rotate x and y axis labels for better visibility
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

plt.show()

# Frequent pattern analysis
data_for_analysis = arrests_df[columns_for_analysis].astype(str)

# Convert categorical data into binary format (one-hot encoding)
te = TransactionEncoder()
data_encoded = te.fit(data_for_analysis.apply(
    lambda x: x.dropna().tolist(), axis=1)).transform(data_for_analysis.apply(lambda x: x.dropna().tolist(), axis=1))
df_encoded = pd.DataFrame(data_encoded, columns=te.columns_)

# Apply Apriori algorithm to find frequent itemsets
min_support = 0.8  # Set the minimum support to 0.3
frequent_itemsets = apriori(df_encoded, min_support=min_support, use_colnames=True)

# Visualization of frequent itemsets
plt.figure(figsize=(20, 14))
plt.barh(range(len(frequent_itemsets)), frequent_itemsets['support'], align='center')
plt.yticks(range(len(frequent_itemsets)), frequent_itemsets['itemsets'].apply(lambda x: ', '.join(map(str, x))))
plt.xlabel('Support')
plt.title(f'Frequent Itemsets (Support > {min_support})')
plt.show()

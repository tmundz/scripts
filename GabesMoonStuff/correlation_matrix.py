import math
from scipy.stats import ttest_ind
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Read 'arrests_final.csv' into a DataFrame
arrests_df = pd.read_csv('arrests_final.csv')

# Extract relevant columns for analysis
columns_for_analysis = ['ArArrestTime', 'ArPremises', 'ArWeapon',
                        'Hair', 'Eyes', 'Race', 'Ethnic', 'Sex',
                        'DrugRelated', 'DrugType', 'NIBRS Crime Against', 'NIBRS Code', 'Sector']

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

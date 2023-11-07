import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('Prediction_fixed.csv')



# Group the DataFrame by 'sector'
grouped = df.groupby('spatial id')

# Create a separate plot for each sector
for sector, group_data in grouped:
    plt.figure()
    plt.plot(group_data['temporal id'], group_data['real'], label='Real', color='blue')
    plt.plot(group_data['temporal id'], group_data['prediction'], label='Prediction', color='red')

    plt.title(f'Sector {sector}')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.legend()
    plt.grid(True)

    # You can save the individual graphs to separate files if needed
    # plt.savefig(f'sector_{sector}_graph.png')

plt.show()

import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

# Read the data from output.csv
data = pd.read_csv('output.csv')

# Select the columns for Price, Year, and Mileage
selected_data = data[['Price', 'Year', 'Mileage']]

# Calculate the correlation matrix
correlation_matrix = selected_data.corr()

# Create the heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')

# Set the title and labels
plt.title('Correlation Heatmap')
plt.xlabel('Variables')
plt.ylabel('Variables')

# Display the heatmap
plt.show()
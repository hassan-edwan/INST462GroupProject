import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('user/micah/csv/DataSet/cars_csv')  

# Data Cleaning and Preprocessing (if needed)

# Group data by company
grouped_data = data.groupby('Company')

# Calculate aggregate statistics
company_stats = grouped_data.agg({'Price': 'mean', 'Miles': 'mean'})

# Reset index for easier plotting
company_stats = company_stats.reset_index()

# Create heatmap
plt.figure(figsize=(12, 8))
heatmap_data = pd.pivot_table(company_stats, values='Price', index='Company', columns='Miles')
sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt=".0f", linewidths=.5)
plt.title('Price vs Miles by Company')
plt.xlabel('Average Miles')
plt.ylabel('Company')
plt.show()

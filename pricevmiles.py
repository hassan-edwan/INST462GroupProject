import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('output.csv', encoding='UTF-8', sep=',')

# Filter out cars with zero mileage
# filtered_data = data[data['Mileage'] > 20000]
# filtered_data = filtered_data[filtered_data['Status'] == 'Certified']
# filtered_data = filtered_data[filtered_data['Country'] == 'Germany']

# Create the scatter plot
# plt.scatter(filtered_data['Mileage'], filtered_data['Price'])
# plt.xlabel('Mileage')
# plt.ylabel('Price')
# plt.title('Price vs Mileage')
# plt.show()
# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

filtered_data = data[data['Mileage'] < 80000]
filtered_data = filtered_data[filtered_data['Mileage'] > 20000]
filtered_data = filtered_data[filtered_data['Price'] < 100000]
filtered_data = filtered_data[filtered_data['Status'] == 'Certified']

# Filter data for each country and plot the scatter plot
countries = ['Germany', 'USA', 'Japan', 'South Korea']
for i, country in enumerate(countries):

    country_filter = filtered_data[filtered_data['Country'] == country]
    # Plot the scatter plot on the corresponding subplot
    ax = axes[i // 2, i % 2]
    ax.scatter(country_filter['Mileage'], country_filter['Price'])
    ax.set_xlabel('Mileage')
    ax.set_ylabel('Price')
    ax.set_title(f'Price vs Mileage for CPO Vehicles - {country}')

# Get legend handles and labels
handles, labels = ax.get_legend_handles_labels()

# Create a mapping of label to handle for scatter plot points
scatter_handles = [(handles[i], labels[i]) for i in range(len(handles)) if labels[i] not in [f'Trendline - {country}' for country in countries_of_interest]]

# Clear the existing legend
ax.legend().remove()

# Create a new legend with only scatter plot handles and labels
ax.legend(handles=[handle[0] for handle in scatter_handles], labels=[handle[1] for handle in scatter_handles], title='Country')

# Show the plot
plt.show()

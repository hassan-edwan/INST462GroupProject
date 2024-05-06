import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('output.csv', encoding='UTF-8', sep=',')


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
    ax.plot(np.unique(country_filter['Mileage']), np.poly1d(np.polyfit(country_filter['Mileage'], country_filter['Price'], 1))(np.unique(country_filter['Mileage'])), color='red')

# Adjust the spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()
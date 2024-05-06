import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('output.csv', encoding='UTF-8', sep=',')

# Filter the data for specific countries and criteria
countries_of_interest = ['Germany', 'Japan', 'South Korea', 'USA']
filtered_data = data[(data['Mileage'] < 80000) & 
                     (data['Mileage'] > 20000) & 
                     (data['Price'] < 100000) & 
                     (data['Status'] == 'Certified') &
                     (data['Country'].isin(countries_of_interest))]

# Set the style and context for seaborn
sns.set(style='whitegrid')  # Set the overall style
sns.set_context('talk')  # Adjust the context for the plot size

# Define a color palette for the selected countries
country_palette = sns.color_palette('Set1', n_colors=len(countries_of_interest))

# Create a scatter plot using Seaborn
plt.figure(figsize=(10, 8))

# Plot data points for selected countries
for i, country in enumerate(countries_of_interest):
    country_data = filtered_data[filtered_data['Country'] == country]
    
    # Plot scatter plot for each country with corresponding color
    sns.scatterplot(x='Mileage', y='Price', data=country_data,
                    color=country_palette[i], label=country, edgecolor='k', s=50)
    
    # Fit and plot regression line (trendline) for each country
    trendline_color = tuple(np.array(country_palette[i]) + 0.1)  # Adjust color slightly
    sns.regplot(x='Mileage', y='Price', data=country_data, scatter=False,
                label=f'Trendline - {country}', ci=None, line_kws={'color': trendline_color})

# Customize labels and title
plt.xlabel('Mileage')
plt.ylabel('Price')
plt.title('Price vs Mileage for Certified Pre-Owned Vehicles')

# Get the current Axes
ax = plt.gca()

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

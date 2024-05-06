import pandas as pd
import plotly.graph_objects as go

# Read the data from output.csv
data = pd.read_csv('output.csv')

# Select the columns for Price, Year, and Mileage
selected_data = data[['Price', 'Year', 'Mileage']]

# Calculate the correlation matrix
correlation_matrix = selected_data.corr()

# Create the text to display inside each heatmap cell
text_values = correlation_matrix.values.round(2)

# Define a custom colorscale with green, white, and black shades
custom_colorscale = [
    [0.0, '#ff6666'],  # red for negative correlation
    [0.3, '#ffffff'],  # white
    [0.5, '#ffffff'],  # white
    [0.99, '#007f00'], # Green for high correlation below 100%
    [1.0, '#000000']   # Black for 100% correlation
]

# Create the heatmap using Plotly
fig = go.Figure(data=go.Heatmap(
    z=correlation_matrix.values,
    x=correlation_matrix.columns,
    y=correlation_matrix.index,
    colorscale=custom_colorscale,
    colorbar=dict(title='Correlation', tickformat='.2f'),
))

# Configure annotations for each cell to display text in black and bold
annotations = []
for i, row in enumerate(correlation_matrix.index):
    for j, col in enumerate(correlation_matrix.columns):
        annotations.append(
            dict(
                x=col,
                y=row,
                text=str(text_values[i, j]),
                xref='x1',
                yref='y1',
                font=dict(color='black', size=12, weight='bold'),
                showarrow=False
            )
        )

# Update layout with title and axis labels
fig.update_layout(
    title='Correlation Heatmap',
    xaxis_title='Variables',
    yaxis_title='Variables',
    width=800,
    height=600,
    font=dict(family='Arial', size=12, color='#333333'),
    plot_bgcolor='white',
    annotations=annotations  # Add annotations to the heatmap
)

# Display the heatmap
fig.show()

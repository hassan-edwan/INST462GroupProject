import pandas as pd
import plotly.graph_objects as go

source = pd.read_csv('pricebycountry.csv', encoding='UTF-8', sep=',')


# Create a heatmap
fig = go.Figure(data=go.Heatmap(
    z=source['Percentage Deviation'],
    x=source['Status'],  
    y=source['Country'],  
    colorscale='Viridis',
    colorbar=dict(title='Percentage Deviation'),
    zmin=-100,
    zmax=100
))


# Customize the layout
fig.update_layout(
    title='Car Prices Percentage Deviation by Country and Status',
    xaxis=dict(title='Status'),  # Flipped x and y axis
    yaxis=dict(title='Country'),  # Flipped x and y axis
    autosize=False,
    width=800,
    height=600
)

# Display the heatmap
fig.show()

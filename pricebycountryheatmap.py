import pandas as pd
import plotly.graph_objects as go

# Read the CSV file into a pandas DataFrame
source = pd.read_csv('pricebycountry.csv', encoding='UTF-8', sep=',')

# Define a custom colorscale from red to green transitioning at 0
custom_colorscale = [
    [0, '#ff6666'],    # Red for values below 0
    [0.12, '#f0f0f0'],  # Light gray for values close to 0
    [0.2, '#f0f0f0'],   # Light gray for values close to 0
    [0.3, '#66cc66'],  # Green for values above 0
    [1, '#66cc66']      # Green for values above 0
]

# Create a heatmap
fig = go.Figure(data=go.Heatmap(
    z=source['Percentage Deviation'],
    x=source['Status'],
    y=source['Country'],
    colorscale=custom_colorscale,
    colorbar=dict(title='Percent Deviation', ticksuffix='%'),
    zmin=-50,
    zmax=400
))

# Customize the layout
fig.update_layout(
    title='Car Prices Percentage Deviation by Country and Status',
    xaxis=dict(title='Status', side='top'),
    yaxis=dict(title='Country', autorange='reversed'),
    autosize=False,
    width=1000,
    height=600,
    margin=dict(l=100, r=100, t=100, b=100),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(family='Arial', size=12, color='#333333'),
    title_font_size=24,
    title_font_family='Arial',
    coloraxis_colorbar=dict(
        thickness=20,
        tickmode='auto',
        tickfont=dict(size=10),
        title_font_size=14,
        title_font_family='Arial'
    )
)

# Update hover behavior to display only 'z' (Percentage Deviation)
fig.update_traces(hovertemplate='Percent Deviation: %{z}%')

# Display the heatmap
fig.show()

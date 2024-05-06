import altair as alt
from vega_datasets import data
import pandas as pd
from altair_saver import save

alt.data_transformers.disable_max_rows()

countries = alt.topo_feature(data.world_110m.url, 'countries')
source = pd.read_csv('output.csv', encoding='UTF-8', sep=',')

chart = alt.Chart(source).mark_bar().encode(
    x='Country:N',
    y='count():Q'
).properties(width=600, height=400)


save(chart, 'output.html')



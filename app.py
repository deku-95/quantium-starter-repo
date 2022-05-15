from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)
# Load data
df = pd.read_csv('data/output.csv')
# Create layout
fig = px.line(df, x='Date', y='Sales', color='Region')
app.layout = html.Div([
    html.H1('Pink Morsel Sales Report'),
    html.Div('''
    The price of pink morsel was increased on January 15. Sales went up.
    '''),
    dcc.Graph(
        id='pink-morsel-sales',
        figure=fig
    )
])

app.run_server(debug=True)

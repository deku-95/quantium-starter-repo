from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)
# Load data
df = pd.read_csv('data/output.csv')
# Create layout and add line color pink
fig = px.line(df, x='Date', y='Sales' , title='Sales history (All)' , color_discrete_sequence=['#ff00ff'])

app.layout = html.Div(
    style= { 'textAlign': 'center', 'font-family': 'Helvetica, sans-serif',
    }, children=
    [
    html.Div(
    style= {'margin': '30px 0 20px 0', 'font-size': '20px'},
    children=
    [
    html.Img(src='static/quantium.png', style={'height': '100px'}),
    html.H1("Soul Foods pink morsel sales report"),
    ]),
    dcc.Graph(id = 'graph', figure=fig, style={
        'backgroundColor': '#f5f5f5',
        'height': '500px',
        'width': '100%',
    }),
    dcc.RadioItems(
        id='region-select',
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': 'North', 'value': 'north'},
            {'label': 'South', 'value': 'south'},
            {'label': 'East', 'value': 'east'},
            {'label': 'West', 'value': 'west'}
        ],
        value='all',
    ),
])

@app.callback(
    Output('graph', 'figure'),
    [Input('region-select', 'value')])
def update_graph(region):
    if region == 'all':
        return fig
    else:
        df_region = df[df['Region'] == region]
        fig_region = px.line(df_region, x='Date', y='Sales', title=f"Sales history({region})",  color_discrete_sequence=['#ff00ff'])
        return fig_region
    

app.run_server(debug=True)

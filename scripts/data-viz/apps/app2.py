import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
import plotly.graph_objects as go
import pandas as pd
from dash import dcc,html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

df = px.data.tips()


layout = dbc.Container([
    html.H1(
        children='Outliers',
     
    ),
    html.P("x-axis:"),
    dcc.Checklist(
        id='x-axis', 
        options=[{'value': x, 'label': x} 
                 for x in ['smoker']],
        value=['time'], 
        labelStyle={'display': 'inline-block'}
    ),
    html.P("y-axis:"),
    dcc.RadioItems(
        id='y-axis', 
        options=[{'value': x, 'label': x} 
                 for x in ['total_bill', 'tip', 'size']],
        value='total_bill', 
        labelStyle={'display': 'inline-block'}
    ),
    dcc.Graph(id="box-plot"),
])

@app.callback(
    Output("box-plot", "figure"), 
    [Input("x-axis", "value"), 
     Input("y-axis", "value")])
def generate_chart(x, y):
    fig = px.box(df, x=x, y=y)
    return fig

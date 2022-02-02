from dash import html,dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

import plotly.express as px
import pandas as pd

data=pd.read_csv("./en.openfoodfacts.org.products.csv",
                     sep="\t", encoding="utf-8", nrows=30000, low_memory=False)

all_dims = list(data.columns)

layout = dbc.Container([
    html.H1(
        children='Comparate',
     
    ),
     dcc.Dropdown(
        
        id="dropdown",
        options=[{"label": x, "value": x} 
                 for x in all_dims],
        value=all_dims[56:58 ],
        multi=True
    ),
    dbc.Alert("you can search the different features to compare them", color="light"),
   
    dcc.Graph(id="splom"),
])

@app.callback(
    Output("splom", "figure"), 
    [Input("dropdown", "value")])
def update_bar_chart(dims):
    fig = px.scatter_matrix(
        data, dimensions=dims)
    return fig

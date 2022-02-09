from dash import html,dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

import plotly.express as px
import pandas as pd

data=pd.read_csv("./en.openfoodfacts.org.products.csv",
                     sep="\t", encoding="utf-8", nrows=30000, low_memory=False)

all_dims = list(data.columns)

# Compare Layout
layout = dbc.Container([
    html.H1(
        children='Comparate',
    ),
    # Dropdown select category 
     dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} 
                 for x in all_dims],
        value=all_dims[56:58 ],
        multi=True
    ),
     
    dbc.Alert("you can search the different features to compare them", color="light"),
    html.Hr(className="my-2"),
    
    #Card Scatter Matrix
        dbc.Card(
       dbc.CardBody([
        html.H2(
        children='Scatter Matrix',
        ),
        dcc.Graph(id="scatter_matrix"),
        dbc.Alert("Tips: use lasso to select points and compare", color="secondary"),
        ]),
       className="mb-3",
       style={'margin-top':'1em'}
    ),
        
])

@app.callback(
    Output("scatter_matrix", "figure"), 
    [Input("dropdown", "value")])
def update_bar_chart(dims):
    fig = px.scatter_matrix(
        data, dimensions=dims)
    return fig

# from dash import html,dcc
import dash_core_components as dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from scripts.dataviz.app import app

import plotly.express as px
import pandas as pd

from scripts.data_loader import get_data

data = get_data(file_path = "./data/en.openfoodfacts.org.products.csv",
                nrows=30000)

all_dims = list(data.columns)

# Compare Layout
layout = dbc.Container([    
    html.H1(
        children='Compare',
    ),
    # Dropdown select category 
     dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} 
                 for x in all_dims],
        value=all_dims[56:58],
        multi=True
    ),
    dbc.Alert("you can search the different features to compare them", color="light"),
    html.Hr(className="my-2"),
    
    # Card Scatter Matrix
    dbc.Card(
       dbc.CardBody([
        html.H2(
        children='Scatter matrix plots',
        ),
        dcc.Graph(id="scatter_matrix", figure={}),
        dbc.Alert("Tips: use lasso to select points and compare", color="secondary"),
        ]),
       className="mb-3",
       style={'margin-top':'1em'}
    ),
        
])

@app.callback(
    Output(component_id="scatter_matrix", component_property="figure"), 
    Input(component_id="dropdown", component_property="value")
    )
def update_graph(dims):
    fig = px.scatter_matrix(
        data, dimensions=dims)
    fig.update_traces(diagonal_visible=False,showupperhalf=True,showlowerhalf=True)
    return fig

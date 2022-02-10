from cmath import log
from gc import collect
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
import plotly.graph_objects as go
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from plotly.subplots import make_subplots

from plotly.tools import FigureFactory as FF
import dash_bootstrap_components as dbc

from scripts.data_loader import get_data

# Loads dataFrame
df = get_data(file_path = "./data/en.openfoodfacts.org.products.csv", 
                   nrows=30000)
#List features
all_dims = list(df.columns)

# Outliers Layout
layout = html.Div([
        html.H1(
        children='Outliers',
        ),

        # Dropdown select category 
        dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} 
                 for x in all_dims ],
        value=all_dims[116],
        multi=False
    ),

    html.Hr(className="my-2"),

    #Card Boxplot
    dbc.Card(
       dbc.CardBody(    [
              html.H2(
        children='BoxPlot',
    ),
                    dcc.Graph(id="boxplot")
                    ]
                    ),
       className="mb-3",
       style={'margin-top':'1em'}
    ),
    #Card Histogramme
    dbc.Card(
       dbc.CardBody(    [
              html.H2(
        children='Histogram',
    ),
                    dcc.Graph(id="histo")
                    ]
                    ),
       className="mb-3",
       style={'margin-top':'1em'}
    ),
    
    #Card Line
    dbc.Card(
       dbc.CardBody(    [
              html.H2(
        children='Line',
    ),
                    dcc.Graph(id="line")
                    ]
                    ),
       className="mb-3",
       style={'margin-top':'1em'}
    ),
    
])


@app.callback(
    Output("boxplot","figure"), 
    [Input("dropdown", "value")])
def update_bar_chart(cat):
   
    
    return px.box(df,x=cat)

#Callback : Histo
@app.callback(
    Output("histo","figure"), 
    [Input("dropdown", "value")])
def update_bar_chart(cat):
    return px.histogram(df,x=cat)


#Callback : Line
@app.callback(
    Output("line","figure"), 
    [Input("dropdown", "value")])
def update_bar_chart(cat):
   
    
    return px.line(df,x=cat)

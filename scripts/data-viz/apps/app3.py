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

df=pd.read_csv("./en.openfoodfacts.org.products.csv",
                     sep="\t", encoding="utf-8", nrows=30000, low_memory=False)

all_dims = list(df.columns)

# df = px.data.tips()
layout = html.Div([
    
      dcc.Dropdown(
        
        id="dropdown",
        options=[{"label": x, "value": x} 
                 for x in all_dims ],
        value=all_dims[116],
        multi=False
    ),
    dcc.Graph(id="ox-plot"),
    dcc.Graph(id="ox-d"),
    dcc.Graph(id="lin"),
    
])


@app.callback(
    Output("ox-plot","figure"), 
    [Input("dropdown", "value")])
def update_bar_chart(cat):
   
    
    return px.box(df,x=cat)

@app.callback(
    Output("ox-d","figure"), 
    [Input("dropdown", "value")])
def update_bar_chart(cat):
   
    
    return px.histogram(df,x=cat)


@app.callback(
    Output("lin","figure"), 
    [Input("dropdown", "value")])
def update_bar_chart(cat):
   
    
    return px.line(df,x=cat)


#  plt.subplots(2)
#     fig = make_subplots(rows=3,cols=1)
#     # count_social = pd.DataFrame.from_dict(data,orient='index')
#     # count_social.columns= [cat]

#     # boxplot = go.Figure(data=[go.Histogram(y=data[cat])])
#     # print(df[cat])
#     # histo=[
#     #     go.Histogram(x=df[cat].values.tolist())
#     #     ]
    
#     histo= px.histogram(df,y=cat)
#     boxplot=
#     fig.append_trace(histo, row=1,col=1)
#     fig.append_trace(boxplot, 2,1)

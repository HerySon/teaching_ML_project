from dash import dcc,html

from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from apps import compare, outilers
from nav import navbar

#Global layout
app.layout =  html.Div(
    [
    dcc.Location(id='url', refresh=False),
    navbar,
    dbc.Container(
        [
              dbc.CardBody([
                html.Div(id='page-content',style={'margin-top':'1em'})

              ])
        ])
    ])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    #Routing
    if pathname == '/apps/comparate':
        return compare.layout
    elif pathname == '/apps/outliers':
        return outilers.layout    
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=False)
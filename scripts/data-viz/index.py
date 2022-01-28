from dash import dcc,html

from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from apps import app1, app2, app3
from nav import navbar

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
    
    if pathname == '/apps/comparate':
        return app1.layout
    elif pathname == '/apps/outliers':
        return app2.layout    
    elif pathname == '/apps/outliers2':
        return app3.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
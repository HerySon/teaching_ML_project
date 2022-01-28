import dash_bootstrap_components as dbc


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Comparate", href="/apps/comparate")),
        dbc.NavItem(dbc.NavLink("Outliers", href="/apps/outliers")),
        dbc.NavItem(dbc.NavLink("Outliers2", href="/apps/outliers2")),

    ],
    brand="OpenFoodFact Explorator",
    brand_href="#",
    color="primary",
    dark=True,
)
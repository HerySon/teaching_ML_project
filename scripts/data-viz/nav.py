import dash_bootstrap_components as dbc


#Navbar and attribute url
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Comparate", href="/apps/comparate")),
        dbc.NavItem(dbc.NavLink("Outliers", href="/apps/outliers")),
    ],
    brand="OpenFoodFact Explorator",
    brand_href="#",
    color="primary",
    dark=True,
)
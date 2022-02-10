import dash_bootstrap_components as dbc


#Navbar and attribute url
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Compare", href="/apps/compare")),
        dbc.NavItem(dbc.NavLink("Outliers", href="/apps/outliers")),
    ],
    brand="OpenFoodFact Explorator",
    brand_href="#",
    color="primary",
    dark=True,
)
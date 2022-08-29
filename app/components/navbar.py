import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Homepage", href="#")),
        dbc.NavItem(dbc.NavLink("Teams", href="#")),
        dbc.NavItem(dbc.NavLink("Players", href="#")),
        dbc.NavItem(dbc.NavLink("Matches", href="#")),
    ],
    brand="SAU-BITIRME",
    brand_href="#",
    color="dark",
    dark=True,
)

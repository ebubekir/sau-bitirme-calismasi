from app.components.box import Box
from app.utils import EMPTY_CHART
from app.helper.dropdown import get_league_list

from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc

leagues_box = Box("Leagues")

leagues_box.children = [
    dbc.Row([
        dbc.Label("League"),
        dbc.Col(dcc.Dropdown(id="league-dropdown", options=get_league_list(), value="Spain LIGA BBVA"), md=2)
    ]),
    dbc.Row([
        dbc.Col(dcc.Loading(
            dash_table.DataTable(
                id="team-list-table",
                style_header={
                    'backgroundColor': 'rgb(30, 30, 30)',
                    'color': 'white'
                },
                style_data={
                    'backgroundColor': 'rgb(50, 50, 50)',
                    'color': 'white'
                },
                sort_action="native",
                filter_action="native",
                hidden_columns=['team_api_id']
            )
        ), md=3),
        dbc.Col([
            dcc.Loading(
                dcc.Graph("team-radar-chart", figure=EMPTY_CHART)
            )
        ], md=9)
    ])
]

layout = [
    dcc.Interval(
        id="load-leagues-interval",
        interval=1 * 1000,
        n_intervals=0,
        max_intervals=1,
    ),
    dbc.Row(leagues_box.render())
]

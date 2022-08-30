from dash import dcc, dash_table, html
import dash_bootstrap_components as dbc

from app.components.box import Box

players_box = Box(title="All Players")

players_box.children = [
    html.H4("Click the player you want to see details...", style={"marginBottom": "20px"}),
    dcc.Loading(
        dash_table.DataTable(
            id=f"player-list-table",
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
            page_action='native',
            page_current=0,
            page_size=25,
            hidden_columns=['player_api_id']
        )
    ),

    dcc.Interval(
        id="load-player-list-interval",
        interval=1 * 1000,
        n_intervals=0,
        max_intervals=1,
    ),
    html.Div(id="redirect-component")
]

layout = [
    dbc.Row(players_box.render())
]

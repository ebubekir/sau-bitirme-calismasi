from dash import dcc

import dash_bootstrap_components as dbc

layout = [
    dbc.Input(id="player-id", type="hidden"),
    dcc.Interval(
        id="playlist-id-load-interval",
        interval=1 * 1000,
        n_intervals=0,
        max_intervals=1,
    )
]

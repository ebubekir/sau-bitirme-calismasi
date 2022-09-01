from app.components.box import Box

from dash import dcc, html
import dash_bootstrap_components as dbc

summary_box = Box(title="Summary")
player_info_box = Box(title="Player Info")

summary_box.children = [
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col('PAS'),
                dbc.Col(html.Div('85', style={"backgroundColor": "green", "text": "white", "width": "fit-content",
                                              "textAlign": "right", "float": "right", "padding": "5px"}))
            ]),
            html.Div([
                html.Div([
                    dbc.Row([
                        dbc.Col('Positioning'),
                        dbc.Col(html.B("95", style={"float": "right"}))
                    ], style={"marginTop": "15px"}),
                    dbc.Progress(value=95, color="success", style={"marginTop": "5px"}),

                ]),
            ])
        ]),
        dbc.Col('Col2'),
        dbc.Col('Col3'),
        dbc.Col('Col4'),
        dbc.Col('Col5'),
        dbc.Col('Col6'),
    ], id="player-summary-box")
]

player_info_box.children = [
    dbc.Row([
        dbc.Col([
            dcc.Loading(
                dcc.Graph(id="player-radar-chart")
            )
        ]),
        dbc.Col([
            'hop'
        ], id="player-info")

    ])
]

layout = [
    dbc.Input(id="player-id", type="hidden"),
    dcc.Interval(
        id="playlist-id-load-interval",
        interval=1 * 1000,
        n_intervals=0,
        max_intervals=1,
    ),
    dbc.Row(player_info_box.render()),
    dbc.Row(summary_box.render(), style={"marginTop": "10px"})
]

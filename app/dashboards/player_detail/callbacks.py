from app.core import app
from app.helper.cache_data import players_cache
from app.helper.cache_data import players_attributes_cache

import pandas as pd
from dash import Output, html
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash_extensions.enrich import Trigger, Input

PAC = ['acceleration', 'sprint_speed']
SHO = ['positioning', 'finishing', 'shot_power', 'long_shots', 'volleys', 'penalties']
PAS = ['vision', 'crossing', 'free_kick_accuracy', 'short_passing', 'long_passing', 'curve']
DRI = ['agility', 'balance', 'reactions', 'ball_control', 'dribbling']
DEF = ['interceptions', 'heading_accuracy', 'standing_tackle', 'sliding_tackle']
PHY = ['jumping', 'stamina', 'strength', 'aggression']


def get_metric_header(title: str, avg_value) -> dbc.Row:
    if 0 < avg_value <= 35:
        badge_bg_color = "red"
    elif 35 < avg_value <= 65:
        badge_bg_color = "orange"
    else:
        badge_bg_color = "green"

    return dbc.Row([
        dbc.Col(title),
        dbc.Col(
            html.Div(str(avg_value), style={"backgroundColor": badge_bg_color, "text": "white", "width": "fit-content",
                                            "textAlign": "right", "float": "right", "padding": "5px"}))
    ])


def get_metric(name: str, value) -> html.Div:
    if 0 < value <= 35:
        bg_color = "danger"
    elif 35 < value <= 65:
        bg_color = "warning"
    else:
        bg_color = "success"

    return html.Div([
        dbc.Row([
            dbc.Col(name),
            dbc.Col(html.B(str(value), style={"float": "right"}))
        ], style={"marginTop": "15px"}),
        dbc.Progress(value=value, color=bg_color, style={"marginTop": "5px"}),
    ])


@app.callback(
    Output("player-id", "value"),
    Input("url", "search")
)
def load_player_id(s):
    return s.replace("?", "")


@app.callback(
    Output("player-summary-box", "children"),
    Input(f"player-id", "value")
)
def load_summary_box(player_id):
    player_df = players_cache()
    player_attr_df = players_attributes_cache()

    df = pd.merge(player_df, player_attr_df, on="player_api_id")
    df = df[df['player_api_id'] == int(player_id)]
    df = df.drop_duplicates(subset="player_name")
    df = df.T.reset_index()
    df.columns = ['metric', 'value']
    df = df[15:]
    results = []
    for metric in ['PAC', 'SHO', 'PAS', 'DRI', 'DEF', 'PHY']:
        tmp_df = df[df['metric'].isin(globals()[metric])]
        results.append(
            dbc.Col([
                get_metric_header(metric, avg_value=float("{:.2f}".format(tmp_df['value'].mean()))),
                html.Div([
                    get_metric(m[1].metric.replace("_", " ").title(), m[1].value) for m in tmp_df.iterrows()
                ])
            ])
        )
    return results

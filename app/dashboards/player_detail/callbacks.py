from app.core import app

from dash import Output
from flask import request
from dash_extensions.enrich import Trigger, Input


@app.callback(
    Output("player-id", "value"),
    Input("url", "search")
)
def load_player_id(s):
    return s.replace("?", "")
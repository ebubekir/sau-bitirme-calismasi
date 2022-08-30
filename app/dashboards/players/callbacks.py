from app.core import app
from app.helper.cache_data import players_cache, players_attributes_cache

import pandas as pd
from dash import Output
from dash_extensions.enrich import Trigger


@app.callback(
    Output("player-list-table", "data"),
    Output("player-list-table", "columns"),
    Trigger(f"load-player-list-interval", "n_intervals")
)
def load_player_data():
    player_data = players_cache()
    player_attributes_data = players_attributes_cache()
    df = pd.merge(player_data, player_attributes_data, on="player_api_id", suffixes=('_x', '_y'))
    data = df[['player_name', 'height', 'weight', 'overall_rating', 'birthday']].drop_duplicates(subset="player_name")
    columns = [{"name": i.replace("_", " ").title(), "id": i} for i in data.columns]
    return data.to_dict('records'), columns

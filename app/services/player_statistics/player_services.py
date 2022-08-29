import pandas as pd
import numpy as np

from app.helper.cache_data import players_cache
from app.helper.cache_data import players_attributes_cache


def top_players_by_skill(skill: str = "overall_rating"):
    player_attr = players_attributes_cache(column_list=['player_api_id', skill])
    player_attr = player_attr.drop_duplicates(subset='player_api_id', keep="first")
    player_attr = player_attr.sort_values(by=skill, ascending=False)

    def get_player_name(player_id: str):
        player = players_cache()
        player = player[player['player_api_id'] == player_id]
        if player.empty:
            return np.nan
        return player['player_name'].values[0]

    player_attr = player_attr[:10]
    player_attr['player_name'] = player_attr['player_api_id'].apply(lambda x: get_player_name(x))
    return player_attr[['player_name', skill]]

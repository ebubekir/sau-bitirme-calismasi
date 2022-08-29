import numpy as np

from app.helper.cache_data import matches_cache
from app.helper.cache_data import league_cache


def get_league_name(league_id):
    league = league_cache()
    league = league[league['id'] == league_id]
    if league.empty:
        return np.nan
    return league['name'].values[0]


def goals_scored_by_leagues_per_season():
    match = matches_cache(column_list=['league_id', 'season', 'home_team_goal', 'away_team_goal'])
    match['total_scored'] = match['home_team_goal'] + match['away_team_goal']
    match = match.groupby(['league_id', 'season']).sum().reset_index()
    match['league_name'] = match['league_id'].apply(lambda x: get_league_name(x))
    return match[['league_name', 'season', 'total_scored']]

import traceback

import numpy as np
import pandas as pd

from app.helper.cache_data import matches_cache
from app.helper.cache_data import team_data_cache


def top_ten_scorer_teams(season: str = "All") -> pd.DataFrame:
    try:
        match = matches_cache(column_list=['season', 'home_team_api_id', 'away_team_api_id', 'home_team_goal', 'away_team_goal'])
        if season != "All":
            match = match[match['season'] == season]
            match = match.drop(columns=['season'])

        def get_team_name(team_api_id: int):
            team = team_data_cache()
            team = team[team['team_api_id'] == team_api_id]
            if team.empty:
                return np.nan
            return team['team_long_name'].values[0]

        match = match[['home_team_api_id', 'away_team_api_id', 'home_team_goal', 'away_team_goal']]
        away_teams = match[['away_team_api_id', 'away_team_goal']]
        match = match.drop(columns=['away_team_api_id', 'away_team_goal'])
        match = match.rename(columns={"home_team_api_id": 'team_api_id', 'home_team_goal': 'goal'})
        away_teams = away_teams.rename(columns={"away_team_api_id": "team_api_id", "away_team_goal": "goal"})

        df = pd.concat([match, away_teams])

        df = df.groupby('team_api_id').sum().reset_index()

        df['team_api_id'] = df['team_api_id'].apply(lambda x: get_team_name(x))

        df = df.sort_values(by='goal', ascending=False)

        df = df[:10]

        return df
    except Exception as e:
        traceback.print_exc()
        return pd.DataFrame()

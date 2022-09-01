from .cache_data import team_data_cache
from .cache_data import country_data_cache
from .cache_data import league_cache
from .cache_data import players_cache
from .cache_data import players_attributes_cache

from dash import html


def seasons_dropdown() -> list:
    seasons = [
        "All",
        "2008/2009",
        "2009/2010",
        "2010/2011",
        "2011/2012",
        "2012/2013",
        "2013/2014",
        "2014/2015",
        "2015/2016", ]
    return [
        {
            "label": html.Div([s], style={"color": "black"}),
            "value": s
        } for s in seasons
    ]


def team_dropdown() -> list:
    df = team_data_cache()
    return [{"label": t, "value": t} for t in df['team_long_name'].unique().tolist()]


def get_player_list(league: str = None, nationality: str = None) -> list:
    df = players_cache()
    return [{"label": t, "value": t} for t in df['player_name'].unique().tolist()]


def get_league_list(country_id: int = None) -> list:
    df = league_cache()
    if country_id:
        df = df[df['country_id'] == country_id]
    return [{"label": html.Div([l], style={"color": "black"}), "value": l} for l in df['name'].unique().tolist()]


def country_dropdown():
    df = country_data_cache()
    return [{"label": c, "value": c} for c in df['name'].unique().tolist()]


def skills_dropdown():
    df = players_attributes_cache()
    return [{
        "label": html.Div([s.replace("_", " ").title()], style={"color": "black"}),
        "value": s
    } for s in df.columns if s not in ['id', 'player_fifa_api_id', 'player_api_id', 'date']]

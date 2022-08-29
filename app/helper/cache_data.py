import pandas as pd
from app.core import cache
from app.utils.data_manager import DataManager


@cache.memoize(expire=3600)
def team_data_cache(column_list: list = None) -> pd.DataFrame:
    return DataManager.read_data('team', column_list=column_list)


@cache.memoize(expire=3600)
def team_attributes_data_cache(column_list: list = None) -> pd.DataFrame:
    return DataManager.read_data('team_attributes', column_list=column_list)


@cache.memoize(expire=3600)
def players_cache(column_list: list = None) -> pd.DataFrame:
    return DataManager.read_data('player', column_list=column_list)


@cache.memoize(expire=3600)
def players_attributes_cache(column_list: list = None) -> pd.DataFrame:
    return DataManager.read_data('player_attributes', column_list=column_list)


@cache.memoize(expire=3600)
def league_cache(column_list: list = None) -> pd.DataFrame:
    return DataManager.read_data('league', column_list=column_list)


@cache.memoize(expire=3600)
def matches_cache(column_list: list = None) -> pd.DataFrame:
    return DataManager.read_data('match', column_list=column_list)


@cache.memoize(expire=3600)
def country_data_cache(column_list: list = None) -> pd.DataFrame:
    return DataManager.read_data('country', column_list=column_list)

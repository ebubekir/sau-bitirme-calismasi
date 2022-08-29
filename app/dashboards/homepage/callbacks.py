import plotly.graph_objects as go
from dash import Input, Output
from dash_extensions.enrich import Trigger

from app.core import app, cache
from app.services.team_statistics import top_ten_scorer_teams
from app.services.player_statistics import top_players_by_skill
from app.services.match_statistics import goals_scored_by_leagues_per_season

page_id = "home-page"


# Top Scorer Teams Callback
@app.callback(
    Input(f"{page_id}-top-scorer-teams-season-filter", "value"),
    Output(f"{page_id}-top-scorer-teams-graph", "figure")
)
@cache.memoize(expire=3600)
def get_top_scorer_teams(season):
    data = top_ten_scorer_teams(season)
    fig = go.Figure()
    fig.add_trace(go.Bar(x=data['team_api_id'], y=data['goal']))
    fig.update_layout(template='plotly_dark')
    return fig


@app.callback(
    Input(f"{page_id}-top-players-skill-filter", "value"),
    Output(f"{page_id}-top-players-graph", "figure")
)
@cache.memoize(expire=3600)
def get_top_players_by_skill(skill):
    data = top_players_by_skill(skill)
    fig = go.Figure()
    fig.add_trace(go.Bar(x=data['player_name'], y=data[skill]))
    fig.update_layout(template='plotly_dark')
    return fig


@app.callback(
    Trigger(f"{page_id}-total-goals-season-interval", "n_intervals"),
    Output(f"{page_id}-total-goals-season-graph", "figure")
)
@cache.memoize(expire=3600)
def get_total_goal_score_league_graph():
    data = goals_scored_by_leagues_per_season()
    fig = go.Figure()

    fig.add_traces([
        go.Scatter(
            x=data[data['league_name'] == d]['season'],
            y=data[data['league_name'] == d]['total_scored'],
            name=d
        )
        for d in data['league_name'].unique().tolist()
    ])

    fig.update_layout(template='plotly_dark')
    return fig

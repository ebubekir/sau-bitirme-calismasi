from dash import html, dcc
import dash_bootstrap_components as dbc
from app.components import Box
from app.helper.dropdown import seasons_dropdown, skills_dropdown
from .callbacks import page_id

teams_box = Box(title="TOP SCORER TEAMS")
teams_box.children = [
    dbc.Row([
        dbc.Col([
            dbc.Label("Season"),
            dcc.Dropdown(
                id=f"{page_id}-top-scorer-teams-season-filter",
                placeholder="Select a season...",
                options=seasons_dropdown(),
                value="All"
            )
        ], md=6)
    ]),
    dbc.Row([
        dcc.Loading(
            dcc.Graph(id=f"{page_id}-top-scorer-teams-graph")
        )
    ], style={"marginTop": "5px"})
]

top_players_box = Box(title="TOP PLAYERS BY SKILL")
top_players_box.children = [
    dbc.Row([
        dbc.Col([
            dbc.Label("Skill"),
            dcc.Dropdown(
                id=f"{page_id}-top-players-skill-filter",
                placeholder="Select a skill...",
                options=skills_dropdown(),
                value="overall_rating"
            )
        ], md=6)
    ]),
    dbc.Row([
        dcc.Loading(
            dcc.Graph(id=f"{page_id}-top-players-graph")
        ),
    ], style={"marginTop": "5px"})
]

goals_league_box = Box(title="TOTAL GOALS IN EACH SEASON BY LEAGUE")
goals_league_box.children = [
    dbc.Row([
        dcc.Loading(
            dcc.Graph(id=f"{page_id}-total-goals-season-graph")
        ),
        dcc.Interval(
            id=f"{page_id}-total-goals-season-interval",
            interval=1 * 1000,
            n_intervals=0,
            max_intervals=1,
        )
    ], style={"marginTop": "5px"})
]

layout = [
    dbc.Row(teams_box.render()),
    dbc.Row(top_players_box.render(), style={"marginTop": "10px"}),
    dbc.Row(goals_league_box.render(), style={"marginTop": "10px"})
]

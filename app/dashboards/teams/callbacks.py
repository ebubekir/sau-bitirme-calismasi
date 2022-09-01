import re

from app.core import app
from app.core.cache import cache
from app.helper.cache_data import league_cache, team_data_cache, matches_cache, team_attributes_data_cache

import plotly.graph_objects as go
from dash import Input, Output, State
from dash.exceptions import PreventUpdate


@app.callback(
    Output("team-list-table", "data"),
    Output("team-list-table", "columns"),
    Input("league-dropdown", "value")
)
@cache.memoize(expire=3600)
def load_team_list(league):
    league_df = league_cache()
    teams_df = team_data_cache()
    matches_df = matches_cache()
    league = league_df[league_df['name'] == league]
    league_id = league['id'].values[0]

    matches_df = matches_df[matches_df['league_id'] == league_id]
    team_ids = matches_df['home_team_api_id'].unique().tolist()
    teams_df = teams_df[teams_df['team_api_id'].isin(team_ids)]
    teams_df = teams_df.rename(columns={"team_long_name": "team_name"})
    teams_df = teams_df[['team_api_id', 'team_name']]
    columns = [{"name": i.replace("_", " ").title(), "id": i} for i in teams_df.columns]
    return teams_df.to_dict('records'), columns


@app.callback(
    Output("team-radar-chart", "figure"),
    Input("team-list-table", "active_cell"),
    State("team-list-table", "data")
)
def load_team_radar_chart(cell, table_data):
    if cell:
        team = table_data[cell['row']]
        team_attr_df = team_attributes_data_cache()
        team_attr_df = team_attr_df[team_attr_df['team_api_id'] == team['team_api_id']]
        team_attr_df = team_attr_df.sort_values(by='date', ascending=False).drop_duplicates(subset='team_api_id')
        team_attr_df = team_attr_df[[c for c in team_attr_df.columns if not c.endswith('Class')]]
        team_attr_df = team_attr_df.T.reset_index()[4:]

        def camel_case_to_title(s):
            return re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', s).title()

        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=team_attr_df[team_attr_df.columns[1]].values.tolist(),
            theta=[camel_case_to_title(l) for l in team_attr_df['index'].values.tolist()],
            fill='toself',
            name="PAC"
        ))

        fig.update_layout(height=600, template="plotly_dark", title="Player Radar Chart", plot_bgcolor="#303030",
                          paper_bgcolor="#303030")
        return fig
    else:
        raise PreventUpdate()

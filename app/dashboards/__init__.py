from .homepage import layout

import importlib
from app.core import app
from dash import html, dcc, Output, Input
from app.components import root_container, navbar

app.layout = html.Div([dcc.Location(id="url"), navbar, root_container])


@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def render_page_content(path_name):
    if path_name == '/':
        return layout
    else:
        module = importlib.import_module(f'dashboards{path_name.replace("/", ".")}')
        return module.layout

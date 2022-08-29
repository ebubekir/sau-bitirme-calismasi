import dash_bootstrap_components as dbc
from dash_extensions.enrich import DashProxy, TriggerTransform


app = DashProxy(
    external_stylesheets=[dbc.themes.DARKLY,
                          "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"],
    external_scripts=["https://cdn.tailwindcss.com"],
    suppress_callback_exceptions=True,
    transforms=[TriggerTransform()]
)



import dash_bootstrap_components as dbc


class Box:
    def __init__(self, title: str = None, children: list = None):
        self.title = title
        self.children = children

    def render(self):
        return dbc.Card(
            [
                dbc.CardHeader(self.title),
                dbc.CardBody(self.children)
            ],
            style={"width": "100%"},
        )

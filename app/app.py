import os
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

debug = False if os.environ["DASH_DEBUG_MODE"] == "False" else True

app = Dash(__name__)

server = app.server

data = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)

graph = px.bar(data, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(
    children=[
        html.H1(
            children=f"Hello Dash in 2022 from {'Dev Server' if debug else 'Prod Server'}"
        ),
        html.Div(children="""Dash: A web application framework for your data."""),
        dcc.Graph(id="example-graph", figure=graph),
    ]
)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8050", debug=debug)

import dash
from dash import dcc, html
import dash_bootstrap_components as dbc


def create_layout(df):
    return dbc.Container(
    fluid=True,
    children=[
        dbc.Row(
            dbc.Col(
                html.H1("Дашборд по погоде в Москве", className="display-4 text-center mt-4 mb-2"),
            ),
        ),
        dbc.Row(
                    [
                        dbc.Col(
                            html.Div([
                                dcc.Graph(id='temperature-graph', config={"displayModeBar": False}),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            dcc.Dropdown(
                                                id='year-dropdown',
                                                options=[{'label': year, 'value': year} for year in
                                                         df['Year'].unique()],
                                                value=df['Year'].max(),
                                                clearable=False,
                                                style={'width': '50%'},
                                                className="cyberpunk-dropdown"
                                            ),
                                            width=4
                                        ),
                                    ],
                                    className="mb-4"
                                ),
                                dcc.Graph(id='scatter-plot', config={"displayModeBar": False}),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            dcc.Dropdown(
                                                id='year-dropdown_1',
                                                options=[{'label': year, 'value': year} for year in
                                                         df['Year'].unique()],
                                                value=df['Year'].max(),
                                                clearable=False,
                                                style={'width': '50%'},
                                                className="cyberpunk-dropdown"
                                            ),
                                            width=4
                                        ),
                                    ],
                                    className="mb-4"
                                ),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            dcc.Tabs([
                                                dcc.Tab(label='Роза ветров', children=[
                                                    html.Div([
#                                               html.H2('Категории скорости ветра', style={"color": "gray"}),
                                                        dcc.Graph(id='wind-rose-plot',
                                                                  config={"displayModeBar": False}),
                                                    ])
                                                ],  className="techno-button"),
                                                dcc.Tab(label='Температурный анализ', children=[
                                                    html.Div([
#                                                        html.H2('Температура по годам', style={"color": "gray"}),
                                                        dcc.Graph(id='temperature-plot',
                                                                  config={"displayModeBar": False}),
                                                    ])
                                                ], className="techno-button"),
                                                dcc.Tab(label='Корреляция температуры и радиации', children=[
                                                    html.Div([
#                                                       html.H2('Корреляция максимальной температуры и индекса солнечной радиации', style={"color": "gray"}),
                                                        dcc.Graph(id='temp-radiation-scatter',
                                                                  config={"displayModeBar": False})
                                                    ]),
                                                    dbc.Row(
                                                        [
                                                            dbc.Col(
                                                                dcc.Dropdown(
                                                                    id='year-dropdown_corr',
                                                                    options=[{'label': year, 'value': year} for year in
                                                                             df['Year'].unique()],
                                                                    value=df['Year'].max(),
                                                                    clearable=False,
                                                                    style={'width': '50%'},
                                                                    className="cyberpunk-dropdown"
                                                                ),
                                                                width=4
                                                            ),
                                                        ],
                                                        className="mb-4"
                                                    ),
                                                ], className="techno-button"),
                                                dcc.Tab(label='Анализ осадков по месяцам', children=[
                                                    html.Div([
#                                                       html.H2('Суммарные осадки по месяцам', style={"color": "gray"}),
                                                        dcc.Graph(id='precipitation-bar',
                                                                  config={"displayModeBar": False})
                                                    ]),
                                                    dbc.Row(
                                                        [
                                                            dbc.Col(
                                                                dcc.Dropdown(
                                                                    id='year-dropdown-precipitation',
                                                                    options=[{'label': year, 'value': year} for year in
                                                                             df['Year'].unique()],
                                                                    value=df['Year'].max(),
                                                                    clearable=False,
                                                                    style={'width': '50%'},
                                                                    className="cyberpunk-dropdown"
                                                                ),
                                                                width=4
                                                            ),
                                                        ],
                                                        className="mb-4"
                                                    ),
                                                ], className="techno-button")
                                            ]),

                                        ),
                                    ],
                                    className="mb-4"
                                ),

                            ], className="techno-panel",),
                           width=12
                        ),
                    ],
                    className="mb-4"
        ),
    ],
    className="minimalist-body"
)
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import os
import csv
from collections import Counter
import sys
import plotly.plotly as py
from dash.dependencies import Input, Output
import cufflinks as cf

with open('Performance Data.csv', encoding='utf-8') as csvfile:

     data = pd.read_csv('Performance Data.csv', low_memory=False, error_bad_lines=False)
     data_dict = {col: list(data[col]) for col in data.columns}

     df = pd.DataFrame(data_dict)
     reader = csv.reader(csvfile)
     sport = df.Sport
     name = df[df.Person == 'Ryan Mullen']
     roadrace = name[name.Discipline == 'Road race']
     fourKm = name[name.Discipline == '4km Individual Pursuit']
     pointsrace = name[name.Discipline == 'Points Race']

app = dash.Dash()

colors = {
    'background': '#FFFFF',
    'text': '#7FDBFF',
    'black': '#11111'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Sports Analysis Dashboard',
        style={
            'textAlign': 'center',
            'color': colors['black']
        }
    ),
    html.H3(
        children="Select/Search Athlete",
        style={
            'textAlign': 'center',
            'color': colors['black']
        }
    ),
    dcc.Dropdown(
        children='Athlete',
        id='athlete_dropdown',
        options=[{'label': i, 'value': i} for i in df.Person.unique()],
        value='10'),
    html.H3(
        children="Select/Search Sport",
        style={
            'textAlign': 'center',
            'color': colors['black']
        }
    ),
    dcc.Dropdown(
        children='Sport',
        id='dropdown1',
        options=[{'label': i, 'value': i} for i in df.Sport.unique()],
        value='10'),
    # dcc.Dropdown(
    #     children='Athlete',
    #     id='dropdown2',
    #     options={'label': 1, 'value': 1}, #Get selected sport and use that as x.Person
    #     value='10'),
    # dcc.Dropdown(
    #     children='Competition',
    #     id='dropdown3',
    #     value='10'),
    html.H1(
        children='',
        style={
            'textAlign': 'center',
            'color': colors['black']
        }
    ),

    html.Div(children='4km Individual Pursuit', style={
        'textAlign': 'left',
        'color': colors['black']
    }),
    html.Div(children='Road Race', style={
        'textAlign': 'right',
        'color': colors['black']
    }),

    dcc.Graph(
        id='Graph1',
        style={"height" : "40%", "width" : "45%", "display": "inline-block", "vertical-align": "left"},
        figure={
            'data':
            [
                go.Scatter(
                    x=fourKm['Date'],
                    y=fourKm['Rank'],
                    mode='lines',
                    opacity=0.7,
                    marker={
                        'size': 5,
                        'line': {'width': 0.5, 'color': 'white'}
                    }
                )

            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'Age'},
                yaxis={'title': 'Rank'},
                margin={'l': 10, 'b': 0, 't': 20, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            ),
            'layout': {
                'plot_bgcolor': colors['black'],
                'paper_bgcolor': colors['black'],
                'font': {
                    'color': colors['black']
                }
            }
        }
    ),
    dcc.Graph(
        id='Graph2',
        style={"height": "40%", "width": "45%", "display": "inline-block", "vertical-align": "right"},
        figure={
            'data':
                [
                    go.Scatter(
                        x=roadrace['Date'],
                        y=roadrace['Rank'],
                        mode='lines',
                        opacity=0.7,
                        marker={
                            'size': 5,
                            'line': {'width': 0.5, 'color': 'white'}
                        }
                    )

                ],
            'layout': go.Layout(
                yaxis=dict(
                    autorange='reversed',
                    title = 'Rank',
                ),
                xaxis=dict(
                    type = 'log',
                    title = 'competition',
                    autorange = 'reversed'
                ),
                margin={'l': 10, 'b': 0, 't': 20, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            ),
            'layout': {
                'plot_bgcolor': colors['black'],
                'paper_bgcolor': colors['black'],
                'font': {
                    'color': colors['black']
                }
            }
        }
    ),
    html.Div(children='Points Race', style={
        'textAlign': 'left',
        'color': colors['black']
    }),
    dcc.Graph(
        id='Graph3',
        style={"height": "40%", "width": "45%", "display": "inline-block", "vertical-align": "right"},
        figure={
            'data':
                [
                    go.Scatter(
                        x=pointsrace['Date'],
                        y=pointsrace['Rank'],
                        mode='lines',
                        opacity=0.7,
                        marker={
                            'size': 5,
                            'line': {'width': 0.5, 'color': 'white'}
                        }
                    )

                ],
            'layout': go.Layout(
                yaxis=dict(
                    autorange='reversed',
                    title='Rank',
                ),
                xaxis=dict(
                    type='log',
                    title='competition',
                    autorange='reversed'
                ),
                margin={'l': 10, 'b': 0, 't': 20, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest',
            ),
            'layout': {
                'plot_bgcolor': colors['black'],
                'paper_bgcolor': colors['black'],
                'font': {
                    'color': colors['black']
                }
            }
        }
    ),
    dcc.Graph(
        id='Graph4',
        style={"height": "40%", "width": "45%", "display": "inline-block", "vertical-align": "right"},
        figure={
            'data':
                [
                    go.Scatter(
                        # x=pointsrace['Date'],
                        # y=pointsrace['Rank'],
                        mode='lines',
                        opacity=0.7,
                        marker={
                            'size': 5,
                            'line': {'width': 0.5, 'color': 'white'}
                        }
                    )

                ],
            'layout': go.Layout(
                yaxis=dict(
                    autorange='reversed',
                    title='Rank',
                ),
                xaxis=dict(
                    type='log',
                    title='competition',
                    autorange='reversed'
                ),
                margin={'l': 10, 'b': 0, 't': 20, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest',
            ),
            'layout': {
                'plot_bgcolor': colors['black'],
                'paper_bgcolor': colors['black'],
                'font': {
                    'color': colors['black']
                }
            }
        }
    ),
])


@app.callback(Output('Graph4', 'figure'),  # Update dropdown box with Athletes froms selected sport.
                [Input('dropdown1', 'value')])
#
# @app.callback(Output('dropdown2', 'figure'),
#                 [Input('dropdown1', 'value')])

def update_graph(selected_dropdown_value):
    dff = df[df['Sport'] == selected_dropdown_value]
    return {
        'data': [{
            'x': dff.Date,
            'y': dff.Rank,
            'line': {
                'width': 3,
                'shape': 'spline'
            }
        }],
        'layout': {
            'margin': {
                'l': 30,
                'r': 20,
                'b': 30,
                't': 20
            }
        }
    }

if __name__ == '__main__':
    app.run_server(debug=True)
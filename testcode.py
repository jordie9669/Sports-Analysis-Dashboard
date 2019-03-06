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

all_options = {
    'America': {
        'New York': ['Statue of Liberty', 'Empire State Building'],
        'San Francisco': ['Golden Gate Bridge', 'Mission District'],
    },
    'Canada': {
        u'Montréal': ['Biodome', 'Parc Laurier'],
        'Toronto': ['CN Tower', 'Royal Ontario Museum'],
    }
}
app.layout = html.Div([
    # dcc.RadioItems(
    #     id='sports-dropdown',
    #     options=[{'label': k, 'value': k} for k in all_options.keys()],
    #     #value = 'America'
    # ),
    dcc.Dropdown(
        children='Sport',
        id='sports-dropdown',
        options=[{'label': i, 'value': i} for i in df.Sport.unique()],
        value='10'),
    dcc.Dropdown(
        children='Athlete',
        id='athletes-dropdown'),
    dcc.Dropdown(
        children='Events',
        id='events-dropdown'
),
    # html.Hr(),
    #
    # dcc.RadioItems(id='athletes-dropdown'),
    #
    # html.Hr(),
    #
    # dcc.RadioItems(id='events-dropdown'),

    html.Div(id='display-selected-values')

])


@app.callback(
    dash.dependencies.Output('athletes-dropdown', 'options'),
    [dash.dependencies.Input('sports-dropdown', 'value')])
def set_sports_options(selected_sport):
    return [{'label': i, 'value': i} for i in [selected_sport]]

@app.callback(
    dash.dependencies.Output('sports-dropdown', 'value'),
    [dash.dependencies.Input('sports-dropdown', 'options')])
def set_athletes_value(available_options):
    return available_options[0]['value']

@app.callback(
    dash.dependencies.Output('events-dropdown', 'options'),
    [dash.dependencies.Input('sports-dropdown', 'value'),
     dash.dependencies.Input('athletes-dropdown', 'value')])
def set_events_options(selected_sport, selected_athlete):
    return [{'label': i, 'value': i} for i in [selected_sport][selected_athlete]]


@app.callback(
    dash.dependencies.Output('events-dropdown', 'value'),
    [dash.dependencies.Input('events-dropdown', 'options')])
def set_events_value(available_options):
    return available_options[0]['value']


@app.callback(
    dash.dependencies.Output('display-selected-values', 'children'),
    [dash.dependencies.Input('sports-dropdown', 'value'),
     dash.dependencies.Input('athletes-dropdown', 'value'),
     dash.dependencies.Input('events-dropdown', 'value')])
def set_display_children(selected_sport, selected_athlete, selected_event):
    return u'{} is in {}, {}'.format(
        selected_event, selected_athlete, selected_sport,
)

if __name__ == '__main__':
    app.run_server(debug=True)
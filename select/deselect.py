import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import csv

# df = pd.read_csv(
#     'https://raw.githubusercontent.com/plotly/'
#     'datasets/master/gapminderDataFiveYear.csv')
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

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='date-slider',
        min=df['Date'].min(),       #get year of data from excel and use first year
        max=df['Date'].max(),          #use last year
        value=df['Date'].min(),         #starts at first year
        marks={str(Date): str(Date) for Date in df['Date'].unique()}
    )
])


@app.callback(
    dash.dependencies.Output('graph-with-slider', 'figure'),
    [dash.dependencies.Input('date-slider', 'value')])
def update_figure(selected_date):
    filtered_df = df[df.Date == selected_date]
    traces = []
    for i in filtered_df.Person.unique():
        df_by_person = filtered_df[filtered_df['Person'] == i]
        traces.append(go.Scatter(
            x=df_by_person['Date'],
            y=df_by_person['Rank'],
            text=df_by_person['Person'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        ))

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'Rank'},
            yaxis={'title': 'Athlete', 'range': [20, 90]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)
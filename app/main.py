import pandas as pd
import dash
import plotly
import plotly.express as px
from dash import html, dcc, Dash
from dash.dependencies import Input, Output

# Constats definition
DATA = plotly.data.gapminder()
DROP_DOWN_FEATURE = ('lifeExp', 'gdpPercap', 'pop')


def get_drop_down_para(in_str):
    lst_of_dict = []
    for year in DATA[in_str].unique():
        lst_of_dict.append({'label': f'{year}', 'value': year})
    
    return {'id': 'drop1',
            'options': lst_of_dict,
        'value': DATA[in_str].unique()[0]}


drop = get_drop_down_para('year')


def get_drop_down_para2():
    lst_of_dict = []
    for item in DROP_DOWN_FEATURE:
        lst_of_dict.append({'label': f'{item}', 'value': item})
    return {'id': 'drop2',
            'options': lst_of_dict,
        'value': DATA.columns[0]}


drop2 = get_drop_down_para2()

app = Dash(__name__)

app.layout = html.Div([
    
    html.H1('Test run of the app!'),    

    dcc.Dropdown(id=drop2['id'], options=drop2['options'], value=drop2['value']),

    dcc.Dropdown(id=drop['id'], options=drop['options'], value=drop['value']),
    
    dcc.Graph(id='fig_one')
    
])

# Callback items are defined after layout
@app.callback(Output('fig_one', 'figure'), 
             [Input('drop1', 'value'),
             Input('drop2', 'value')])
def get_update_graph(select_year, select_feature):
    filt_data = DATA.loc[DATA['year'] == select_year]
    fig = px.choropleth(filt_data,
                        locations="iso_alpha",
                        color=select_feature, 
                        hover_name="country", 
                        color_continuous_scale=px.colors.sequential.Plasma)
    
    fig.update_layout(transition_duration=500)
    return fig


if __name__ == '__main__':
     app.run_server(debug=True)

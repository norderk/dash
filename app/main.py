import pandas as pd
import dash
import plotly
import plotly.express as px
from dash import html, dcc, Dash
from dash.dependencies import Input, Output

# Constats definition
DATA = plotly.data.gapminder()


def get_drop_down_para():
    lst_of_dict = []
    for year in DATA['year'].unique():
        lst_of_dict.append({'label': f'{year}', 'value': year})
    
    return {'id': 'drop1',
            'options': lst_of_dict,
        'value': 1952}


drop = get_drop_down_para()

app = Dash(__name__)

app.layout = html.Div([
    
    html.H1('Test run of the app!'),    

    dcc.Dropdown(id=drop['id'], options=drop['options'], value=drop['value']),
    
    dcc.Graph(id='fig_one')
    
])

# Callback items are defined after layout
@app.callback(Output('fig_one', 'figure'), [Input('drop1', 'value')])
def get_update_graph(select_year):
    filt_data = DATA.loc[DATA['year'] == select_year]
    fig = px.choropleth(filt_data,
                        locations="iso_alpha",
                        color="pop", 
                        hover_name="country", 
                        color_continuous_scale=px.colors.sequential.Plasma)
    
    fig.update_layout(transition_duration=500)
    return fig


if __name__ == '__main__':
     app.run_server(debug=True)

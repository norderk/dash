import pandas as pd
import dash
from dash import dash_table
import plotly
import plotly.express as px
from dash import html, dcc, Dash
from dash.dependencies import Input, Output, State


DATA = px.data.election()

app = dash.Dash(__name__)

app.layout = html.Div([


    dash_table.DataTable(id='table1',
                         data = [],
                         #columns=[{'name': i, 'id': i, 'selectable': True} for i in DATA.columns],
                         #data=[list(DATA.to_dict(orient='records'))],
                         selected_rows=[],
                         row_selectable="multi",
                         editable=True)
])

@app.callback(Output('table1', 'data'), 
              [Input('table1', 'selected_rows')])
def exp_row(selected_rows):

    if len(selected_rows) < 1:
        columns=[{'name': i, 'id': i, 'selectable': True} for i in DATA.columns]
        data=DATA.to_dict(orient='records')
        return [columns, data]

    # if selected_rows is None:
    #     return dash_table.DataTable(id='table1',
    #                      columns=[{'name': i, 'id': i, 'selectable': True} for i in DATA.columns],
    #                      data=list(DATA.to_dict(orient='records')),
    #                      selected_rows=[],
    #                      row_selectable="multi",
    #                      editable=True)


    # new_df = pd.DataFrame([])
    # for ind, row in DATA.iterrows():
    #     new_df.append(row, ignore_index=True)
    #     if ind in selected_rows:
    #         row['district'] = 'This is added information!'
    #         new_df.append(row, ignore_index=True)
    # return new_df.to_dict(orient='records')

if __name__ == '__main__':
    app.run_server(debug=True)
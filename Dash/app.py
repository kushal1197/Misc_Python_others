import os
import pathlib

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
import plotly.graph_objs as go
import dash_daq as daq
import pandas as pd
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)

df = pd.read_csv('D:\Dash\Data\Daily Sales report 01-03-2019 to 06-06-2019.csv')
df2 = pd.read_csv('D:\Dash\Data\Available Inventory.csv')
df3 = pd.read_excel('D:\Dash\Data\media_sale.xlsx')
# df3 = pd.read_csv('D:\Dash\Data\category_sale.csv')
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

def generate_table(dataframe, max_rows=20):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app.layout = html.Div(children=[
    html.H1(children='AM/ PM STORES'),

    html.Div([    
    html.Label('Select sales type'),
        dcc.Dropdown(
            id='sales-dropdown',
            options=[
                {'label': 'TOTAL BILLS', 'value': 'TB'},
                {'label': 'TOTAL TAXABLE AMOUNT', 'value': 'TTA'},
                {'label': 'TOTAL AMOUNT', 'value': 'TA'},
                {'label': 'TOTAL TAX AMOUNT', 'value': 'TTAXA'},
                {'label': 'Taxable Amount 0%', 'value': 'TAXA0'},
                {'label': 'Taxable Amount 3%', 'value': 'TAXA3'},
                {'label': 'Taxable Amount 5%', 'value': 'TAXA5'},
                {'label': 'Taxable Amount 12%', 'value': 'TAXA12'},
                {'label': 'Taxable Amount 18%', 'value': 'TAXA18'},
                {'label': 'Taxable Amount 28%', 'value': 'TAXA28'},
                {'label': 'TOTAL CESS AMOUNT', 'value': 'TCA'},
                {'label': 'TOTAL ADDL CESS AMOUNT', 'value': 'TACA'},
                {'label': 'CASH', 'value': 'CASH'},
                {'label': 'CARD', 'value': 'CARD'},
                {'label': 'OTHER MODES', 'value': 'OM'},
                {'label': 'AMOUNT RETURN', 'value': 'AR'},
                {'label': 'AMOUNT RETURN TO CREDIT', 'value': 'ARTC'},
                {'label': 'TOTAL ITEMS SOLD', 'value': 'TIS'},
                {'label': 'TOTAL QTY', 'value': 'TQ'},
                {'label': 'RETURNED ITEMS COUNT', 'value': 'RIC'},
                {'label': 'RETURNED QTY', 'value': 'RQ'}
                # [{'label': i, 'value': i} for i in df.columns],
            ],
            # value=['TB', 'TTA', 'TA','TTAXA','TAXA0','TAXA3','TAXA5','TAXA12','TAXA18','TAXA28','TCA','TACA','CASH','CARD','OM','AR','ARTC','TIS', 'TQ','RIC','RQ'],
            # value=['TA'],
            multi = True
        ),
    ],style={'width': '90%', 'display': 'inline-block'}),    
    html.Div([
        dcc.Graph(
            id='daily-sales',
            # figure={
                # 'data': [
                    # {'x': df['DATE'], 'y': df['TOTAL BILLS'], 'type': 'scatter', 'name': 'TOTAL BILLS'},
                    # {'x': df['DATE'], 'y': df['TOTAL TAXABLE AMOUNT'], 'type': 'scatter', 'name': 'TOTAL TAXABLE AMOUNT'},
                    # {'x': df['DATE'], 'y': df['TOTAL AMOUNT'], 'type': 'scatter', 'name': 'TOTAL AMOUNT'},
                # ],
       
                # 'layout': {
                    # 'title': 'Daily Sales',
                    # 'plot_bgcolor': colors['background'],
                    # 'paper_bgcolor': colors['background'],
                    # 'font': {
                        # 'color': colors['text']
                    # }
                # }
            # }
        ),
    ]
    ),    
    html.Div([    
    html.Label('Available Inventory'),
        dcc.Dropdown(
            id='number-rows',
        ),
    ],style={'width': '48%', 'display': 'inline-block'}),  
    generate_table(df2),


])

@app.callback(
    Output('daily-sales', 'figure'),
    [Input('sales-dropdown', 'value')
     ])

def sales_graph(yaxis_column_name):
    # trace1 = []
    # for column in yaxis_column_name:
        # trace1.append(
        # go.Scatter(x=column['DATE'],y=column['DATE']))
    # data = [val for sublist in trace1 for val in sublist]        
    # figure = {'data': data,
              # 'layout': go.Layout(colorway=["#5E0DAC", '#FF4F00', '#375CB1', 
                                            # '#FF7400', '#FFF400', '#FF0056'],
            # height=600,
            # xaxis={"title":"Date",
                   # 'rangeselector': {'buttons': list([{'count': 1, 'label': '1M', 
                                                       # 'step': 'month', 
                                                       # 'stepmode': 'backward'},
                                                      # {'count': 6, 'label': '6M', 
                                                       # 'step': 'month', 
                                                       # 'stepmode': 'backward'},
                                                      # {'step': 'all'}])},
                   # 'rangeslider': {'visible': True}, 'type': 'date'},
             # yaxis={"title":"Sales Type"})}
    return {
        'data': [dict(
            x=value['DATE'],
            y=yaxis_column_name['value'],
            # y=df['TOTAL BILLS']['DATE'],
            # y=value['DATE'],
            mode='scatter',
        )],
        
    }
    # return figure
    # return value
if __name__ == '__main__':
    app.run_server(debug=True)
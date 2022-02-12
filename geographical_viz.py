import pandas as pd
import sqlite3
import dash
import plotly.graph_objects as go
from dash import  dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
app.scripts.config.serve_locally = True


# db_cursor = conn.cursor()
# acc_df = pd.read_csv('databases/accident_clean.csv')


#App Layout
app.layout = html.Div(id = 'main_div', children = [

    html.H1(id = 'header_1', children ='Web Application Dashboards with Dash'),

    dcc.Dropdown(
        id = 'count_of_data_points',
        options = [
            {'label': '10', 'value': 10},
            {'label': '100', 'value': 100},
            {'label': '1000', 'value': 1000},
            {'label': '10000', 'value': 10000},
            {'label': '100000', 'value': 100000},
        ],
        multi = False,
        value = 100,
        style = {'width': '40%'}
    ),

    dcc.Graph(id = 'line_plot', figure = {})
    
    
    ]
)



#Collecting data from DB depending on feature name & number of data points
def slct_DB_series(feature, data_points):

    
    #connect to DB
    conn = sqlite3.connect('databases/car_acc.db')
    #DB Cursor
    db_cursor = conn.cursor()
     
    slct_stmt = """
                SELECT (?) AS (?)
                FROM car_acc_table
                
                LIMIT (?)
    
                """

    inputs = (feature, feature, data_points)

    db_cursor.execute(slct_stmt, inputs)

    column = db_cursor.fetchall()

    
    db_cursor.close()
    conn.close()

    return column



@app.callback(
    Output(component_id= 'line_plot', component_property= 'figure'),
    Input(component_id='count_of_data_points', component_property= 'value')
)

def geographical_map(data_points):

   

    fig = go.Figure(
        go.Densitymapbox(lat= slct_DB_series('Latitude', data_points),
                        lon= slct_DB_series('Longitude', data_points),
                        z = slct_DB_series('Number of Vehicles', data_points),
                        radius= 10,
                        opacity= 0.3,
                        # mode = 'markers'
                        # zoom = 2
                        )
        # go.Densitymapbox(lat= acc_df['Latitude'].head(data_points),
        #                     lon= acc_df['Longitude'].head(data_points),
        #                     z = acc_df['Number_of_Vehicles'].head(data_points),
        #                     radius= 10,
        #                     opacity= 0.3
        #                     )
    )
    fig.update_layout(mapbox_style= 'stamen-terrain',
                        mapbox_center_lon= 0,
                        mapbox_center_lat= 52,
                        # zoom = 10
                        )
    
    fig.update_layout(margin={'r':0,"t":0,"l":0,"b":0})
    
    # fig.add_trace(
    #     go.Scatter(x= acc_df['Day_of_Week'].head(10), y= acc_df['Number_of_Vehicles'].head(10),
    #     mode = 'lines',
    #     name = 'plot'
    #                 )

    #             )


    return fig





# def stock_prices():
#     # Function for creating line chart showing Google stock prices over time 
#     fig = go.Figure([go.Scatter(x = df['date'], y = df['GOOG'],\
#                      line = dict(color = 'firebrick', width = 4), name = 'Google')
#                      ])
#     fig.update_layout(title = 'Prices over time',
#                       xaxis_title = 'Dates',
#                       yaxis_title = 'Prices'
#                       )
#     return fig  

 
# app.layout = html.Div(id = 'parent', children = [
#     html.H1(id = 'H1', children = 'Styling using html components', style = {'textAlign':'center',\
#                                             'marginTop':40,'marginBottom':40}),

        
#         # dcc.Graph(id = 'line_plot', figure = stock_prices())    
#     ]
#                      )





#Dash Components


#Plotly Graphs


#Callback

#inputs & outputs

#dataframe copy


#Initialize
if __name__ == '__main__':
    app.run_server(debug = True)
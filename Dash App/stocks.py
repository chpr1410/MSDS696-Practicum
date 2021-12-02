import dash
#from dash import html
import dash_html_components as html
#from dash import dcc
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Input, Output, State
import dash_table
import dash_table.FormatTemplate as FormatTemplate
from dash_table.Format import Sign

import pandas as pd
import pathlib
import statistics


model_result_df = pd.read_csv('https://raw.githubusercontent.com/chpr1410/MSDS696-Practicum/main/Logs/Result%20Logs/By%20Window/Result%20Log%20by%20Window%20-%2030%20min.csv')

print(model_result_df.head())

# DataTable
dff = model_result_df.drop(['TP','FP','TN','FN'], axis=1)


app = dash.Dash()

options = []
ticker_list = list(set(list(model_result_df['Ticker'])))
ticker_list = sorted(ticker_list)


mydict = {}
mydict['label'] = 'All'
mydict['value'] = 'All'
options.append(mydict)

for tic in ticker_list:
    #{'label': 'user sees', 'value': 'script sees'}
    mydict = {}
    mydict['label'] = tic #Apple Co. AAPL
    mydict['value'] = tic
    options.append(mydict)

metric_options = [
            {'label':'ROC Score', 'value':'ROC Score' },
            {'label': 'Passive Return', 'value':'Passive Return'},
            {'label': "Model's Return", 'value':'Strat Return'},
            #{'label': "Model Over Passive", 'value':'Model Over Passive'},
            ]

day_options = [
            {'label':'All', 'value':5 },
            {'label':'Monday', 'value':0 },
            {'label': 'Tuesday', 'value':1},
            {'label': "Wednesday", 'value':2},
            {'label': "Thursday", 'value':3},
            {'label': "Friday", 'value':4},
            ]

hour_options = [
            {'label':'All', 'value':0 },
            {'label':'9', 'value':9 },
            {'label': '10', 'value':10},
            {'label': "11", 'value':11},
            {'label': "12", 'value':12},
            {'label': "13", 'value':13},
            {'label': "14", 'value':14},
            {'label': "15", 'value':15},
            ]

app.layout = html.Div([

                ###########################################################################
                                            # Main Title
                ###########################################################################
                html.H1('Using Deep Learning to Find Stock Pricing Patterns'),

                dcc.Markdown('''
                    ### By: Chris Pranger
                    #### Regis University
                    #### MSDS 696 - Data Science Practicum II
                    [GitHub](https://github.com/chpr1410)
                    [LinkedIn](https://www.linkedin.com/in/christopherpranger/)
                '''),

                dcc.Markdown(''' --- '''),
                dcc.Markdown(''' --- '''),

                dcc.Markdown('''

                    ## Dashboard Description

                    The dashboards below are a way to visualize the results of this project.

                    The dashboard is broken down into three different sections:

                    **1.) Comparing Metrics of Different Stocks By Window**

                    This section plots the metrics for models of individual stocks, and allows for a comparison between them.
                    Metrics include ROC Score, Model % Returns, and Passive % Returns.
                    Performance can be analyzed by stock ticker, day of the week, and hour of the day.

                    **2.) Comparing Metrics for Different Groups of Stocks By Window**

                    This section allows for an analysis of a group of stocks and how they performed together.
                    The metrics are the same as above, except they are averaged for the selection of stocks
                    instead of showing each one individually.

                    **3.) Selecting a Portfolio of Stocks and Viewing Financial Performance**

                    This section allows one to determine which models and stocks performed best for specific windows.
                    By filtering the datatable, one can select which stocks - and for which windows - they would like
                    to add to their portfolio.  The graphs plot the performance of the portfolio and the bottom output
                    shows the average weekly percentage return as well as this weekly rate on an annual basis.

                    Can you choose a portfolio that provides positive performance?


                '''),


                dcc.Markdown(''' --- '''),
                dcc.Markdown(''' --- '''),

                ###########################################################################
                                            # First Section Title
                ###########################################################################
                html.H2('Comparing Metrics of Different Stocks By Window'),


                ###########################################################################
                                            # First Dropdown Sections
                ###########################################################################
                html.Div([html.H3('Choose Ticker(s):', style={'paddingRight': '30px'}),
                dcc.Dropdown(
                          id='my_ticker_symbol',
                          options = options,
                          value = ['AGG'],
                          multi = True,
                          searchable = True
                          # style={'fontSize': 24, 'width': 75}
                )

                ], style={'display': 'inline-block', 'verticalAlign':'top', 'width': '30%'}),
                html.Div([html.H3('Choose Day(s):', style={'paddingRight': '30px'}),
                dcc.Dropdown(
                          id='my_day_window',
                          options = day_options,
                          value = [5],
                          multi = True,
                          searchable = True
                          # style={'fontSize': 24, 'width': 75}
                )

                ], style={'display': 'inline-block', 'verticalAlign':'top', 'width': '30%'}),
                html.Div([html.H3('Choose Hour(s):', style={'paddingRight': '30px'}),
                dcc.Dropdown(
                          id='my_hour_window',
                          options = hour_options,
                          value = [0],
                          multi = True,
                          searchable = True
                          # style={'fontSize': 24, 'width': 75}
                )


                ], style={'display': 'inline-block', 'verticalAlign':'top', 'width': '30%'}),
                html.Div([html.H4('Push Submit to Generate Graphs:', style={'paddingRight': '30px'}),

                ], style={'display':'inline-block'}),
                html.Div([
                    html.Button(id='submit-button',
                                n_clicks = 0,
                                children = 'Submit',
                                style = {'fontSize': 14, 'marginLeft': '50px'}
                               )
                ], style={'display': 'inline-block'}),


                ###########################################################################
                                            # First Graphs
                ###########################################################################
                dcc.Graph(id='my_graph',
                            figure={'data':[
                                {'x':[1,2], 'y':[3,1]}

                            ], #'layout':go.Layout(title='Relative Stock Returns Comparison',
                               #                             yaxis = {'title':'Returns', 'tickformat':".2%"}
                                         #)
                                   }
                ),

                dcc.Graph(id='my_graph2',
                            figure={'data':[
                                {'x':[1,2], 'y':[3,1]}

                            ], #'layout':go.Layout(title='Relative Stock Returns Comparison',
                               #                             yaxis = {'title':'Returns', 'tickformat':".2%"}
                                         #)
                                   }
                ),

                dcc.Graph(id='my_graph3',
                            figure={'data':[
                                {'x':[1,2], 'y':[3,1]}

                            ], #'layout':go.Layout(title='Relative Stock Returns Comparison',
                               #                             yaxis = {'title':'Returns', 'tickformat':".2%"}
                                         #)
                                   }
                ),

                dcc.Markdown(''' --- '''),
                ###########################################################################
                                            # Second Section Title
                ###########################################################################
                html.H2('Comparing Metrics for Different Groups of Stocks By Window'),


                ###########################################################################
                                            # Second Dropdown Sections
                ###########################################################################
                html.Div([html.H3('Choose Ticker(s):', style={'paddingRight': '30px'}),
                dcc.Dropdown(
                          id='my_ticker_symbol2',
                          options = options,
                          value = ['AGG'],
                          multi = True,
                          searchable = True
                          # style={'fontSize': 24, 'width': 75}
                )

                ], style={'display': 'inline-block', 'verticalAlign':'top', 'width': '30%'}),
                html.Div([html.H3('Choose Day(s):', style={'paddingRight': '30px'}),
                dcc.Dropdown(
                          id='my_day_window2',
                          options = day_options,
                          value = [5],
                          multi = True,
                          searchable = True
                          # style={'fontSize': 24, 'width': 75}
                )

                ], style={'display': 'inline-block', 'verticalAlign':'top', 'width': '30%'}),
                html.Div([html.H3('Choose Hour(s):', style={'paddingRight': '30px'}),
                dcc.Dropdown(
                          id='my_hour_window2',
                          options = hour_options,
                          value = [0],
                          multi = True,
                          searchable = True
                          # style={'fontSize': 24, 'width': 75}
                )


                ], style={'display': 'inline-block', 'verticalAlign':'top', 'width': '30%'}),
                html.Div([html.H4('Push Submit to Generate Graphs:', style={'paddingRight': '30px'}),

                ], style={'display':'inline-block'}),
                html.Div([
                    html.Button(id='submit-button2',
                                n_clicks = 0,
                                children = 'Submit',
                                style = {'fontSize': 14, 'marginLeft': '50px'}
                               )
                ], style={'display': 'inline-block'}),


                ###########################################################################
                                            # Second Graphs
                ###########################################################################
                dcc.Graph(id='my_graph4',
                            figure={'data':[
                                {'x':[1,2], 'y':[3,1]}

                            ], #'layout':go.Layout(title='Relative Stock Returns Comparison',
                               #                             yaxis = {'title':'Returns', 'tickformat':".2%"}
                                         #)
                                   }
                ),

                dcc.Graph(id='my_graph5',
                            figure={'data':[
                                {'x':[1,2], 'y':[3,1]}

                            ], #'layout':go.Layout(title='Relative Stock Returns Comparison',
                               #                             yaxis = {'title':'Returns', 'tickformat':".2%"}
                                         #)
                                   }
                ),

                dcc.Graph(id='my_graph6',
                            figure={'data':[
                                {'x':[1,2], 'y':[3,1]}

                            ], #'layout':go.Layout(title='Relative Stock Returns Comparison',
                               #                             yaxis = {'title':'Returns', 'tickformat':".2%"}
                                         #)
                                   }
                ),

                dcc.Markdown(''' --- '''),
                dcc.Markdown(''' --- '''),

                ###########################################################################
                                            # Third Section Title
                ###########################################################################
                html.H2('Selecting a Portfolio of Stocks and Viewing Financial Performance'),

                ###########################################################################
                                            # Data Table
                ###########################################################################

                dcc.Markdown(''' --- '''),
                html.H4('DataTable For Portfolio Selection'),
                html.Div([
                    dash_table.DataTable(
                        id='datatable_id',
                        data=dff.to_dict('records'),
                        columns=[{
                            'id': 'Ticker',
                            'name': 'Ticker',
                            'type': 'text'
                        }, {
                            'id': 'Weekday',
                            'name': 'Day of Week',
                            'type': 'numeric',
                        }, {
                            'id': 'Hour',
                            'name': 'Hour of Day',
                            'type': 'numeric',
                        }, {
                            'id': 'Minute',
                            'name': 'Minute',
                            'type': 'numeric',
                        }, {
                            'id': 'ROC Score',
                            'name': 'ROC Score (%)',
                            'type': 'numeric',
                            'format': FormatTemplate.percentage(1)
                        },{
                            'id': 'Strat Return',
                            'name': 'Average Model Return (%)',
                            'type': 'numeric',
                            'format': FormatTemplate.percentage(3).sign(Sign.positive)
                        },{
                            'id': 'Passive Return',
                            'name': 'Averagae Passive Return (%)',
                            'type': 'numeric',
                            'format': FormatTemplate.percentage(3).sign(Sign.positive)
                        }],
                        editable=False,
                        filter_action="native",
                        sort_action="native",
                        sort_mode="multi",
                        row_selectable="multi",
                        row_deletable=False,
                        selected_rows=[],
                        page_action="native",
                        page_current= 0,
                        page_size= 10,

                    ),
                ],className='row'),
                html.Div([html.H4('Push Submit to Generate Portfolio:', style={'paddingRight': '30px'}),

                ], style={'display':'inline-block'}),

                html.Div([
                    html.Button(id='submit-button3',
                                n_clicks = 0,
                                children = 'Submit',
                                style = {'fontSize': 14, 'marginLeft': '50px'}
                               )
                ], style={'display': 'inline-block'}),

                 ###########################################################################
                                            # Third Graphs
                ###########################################################################
                dcc.Graph(id='my_graph7',
                            figure={'data':[
                                {'x':[1,2], 'y':[3,1]}

                            ], #'layout':go.Layout(title='Relative Stock Returns Comparison',
                               #                             yaxis = {'title':'Returns', 'tickformat':".2%"}
                                         #)
                                   }
                ),

                dcc.Graph(id='my_graph8',
                            figure={'data':[
                                {'x':[1,2], 'y':[3,1]}

                            ], #'layout':go.Layout(title='Relative Stock Returns Comparison',
                               #                             yaxis = {'title':'Returns', 'tickformat':".2%"}
                                         #)
                                   }
                ),

                dcc.Graph(id='my_graph9',
                            figure={'data':[
                                {'x':[1,2], 'y':[3,1]}

                            ], #'layout':go.Layout(title='Relative Stock Returns Comparison',
                               #                             yaxis = {'title':'Returns', 'tickformat':".2%"}
                                         #)
                                   }
                ),


                ###########################################################################
                                            # Indicator
                ###########################################################################


                dcc.Markdown(''' --- '''),
                dcc.Markdown(''' --- '''),

                ###########################################################################
                                            # Third Section Title
                ###########################################################################
                html.H2('Portfolio Performance'),

                dcc.Graph(id='my_graph10',
                            figure={'data':[
                                {'x':[1,2], 'y':[3,1]}

                            ], #'layout':go.Layout(title='Relative Stock Returns Comparison',
                               #                             yaxis = {'title':'Returns', 'tickformat':".2%"}
                                         #)
                                   }
                ),



])

@app.callback(Output('my_graph', 'figure'),
            Output('my_graph2', 'figure'),
            Output('my_graph3', 'figure'),
            [Input('submit-button', 'n_clicks')],
            [State('my_ticker_symbol', 'value'),
                State('my_day_window', 'value'),
                State('my_hour_window', 'value')],       
)
def update_graph(n_clicks, stock_ticker, day, hour):

    if stock_ticker == ['All']:
        stock_ticker = ticker_list

    # Toggle Days
    if day == [5]:
        day = [0,1,2,3,4]
    # Toggle Hours
    if hour == [0]:
        hour = [9,10,11,12,13,14,15]

    # Get x_labels
    day_str = []
    for d in day:
        if d == 0:
            day_str.append("Mon")
        elif d == 1:
            day_str.append("Tues")
        elif d == 2:
            day_str.append("Wed")
        elif d == 3:
            day_str.append("Thur")
        elif d == 4:
            day_str.append("Fri")

    x_label = []
    for d in day_str:
        for h in hour:
            x_label.append(d + " " + str(h))


    ###################################################################################################################
    stock_dict = {}
    # Get y_data (Trim DF)
    for ticker in stock_ticker:
        stock_dict[ticker] = []
        for d in day:
            for h in hour:
                # Group DF by ticker, day, and hour
                df_slice = model_result_df.loc[(model_result_df['Ticker'] == ticker) & (model_result_df['Weekday'] == d) & (model_result_df['Hour'] == h)]

                # Get average for that group
                avg_for_window = statistics.mean(df_slice['ROC Score'])

                # append to stock_dict[ticker]
                stock_dict[ticker].append(avg_for_window)

    stock_df = pd.DataFrame.from_dict(stock_dict)
    stock_df['Window'] = x_label

    fig = px.scatter(stock_df, x='Window', y=stock_df.columns[0:],
                    labels=dict(value='ROC Score (0 to 1)', variable="Ticker"),title="ROC Score For Different Windows")

    fig.update_xaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
    #fig.update_xaxes(showgrid=True, gridwidth=0.1, gridcolor='crimson')
    fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')

    ###############################################################################################################
    stock_dict = {}
    # Get y_data (Trim DF)
    for ticker in stock_ticker:
        stock_dict[ticker] = []
        for d in day:
            for h in hour:
                # Group DF by ticker, day, and hour
                df_slice = model_result_df.loc[(model_result_df['Ticker'] == ticker) & (model_result_df['Weekday'] == d) & (model_result_df['Hour'] == h)]

                # Get average for that group
                avg_for_window = statistics.mean(df_slice['Strat Return'])

                # append to stock_dict[ticker]
                stock_dict[ticker].append(round(avg_for_window*100,5))

    stock_df = pd.DataFrame.from_dict(stock_dict)
    stock_df['Window'] = x_label

    fig2 = px.scatter(stock_df, x='Window', y=stock_df.columns[0:],
                    labels=dict(value="Strat. Return (Already in %)", variable="Ticker"),title="Strategy Return For Different Windows")

    fig2.update_xaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
    #fig2.update_xaxes(showgrid=True, gridwidth=0.1, gridcolor='crimson')
    fig2.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')

    ###############################################################################################################
    stock_dict = {}
    # Get y_data (Trim DF)
    for ticker in stock_ticker:
        stock_dict[ticker] = []
        for d in day:
            for h in hour:
                # Group DF by ticker, day, and hour
                df_slice = model_result_df.loc[(model_result_df['Ticker'] == ticker) & (model_result_df['Weekday'] == d) & (model_result_df['Hour'] == h)]

                # Get average for that group
                avg_for_window = statistics.mean(df_slice['Passive Return'])

                # append to stock_dict[ticker]
                stock_dict[ticker].append(round(avg_for_window*100,5))

    stock_df = pd.DataFrame.from_dict(stock_dict)
    stock_df['Window'] = x_label

    fig3 = px.scatter(stock_df, x='Window', y=stock_df.columns[0:],
                    labels=dict(value="Pass. Return (Already in %)", variable="Ticker"),title="Passive Returns For Different Windows")

    fig3.update_xaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
    #fig2.update_xaxes(showgrid=True, gridwidth=0.1, gridcolor='crimson')
    fig3.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')

    return fig, fig2, fig3

@app.callback(Output('my_graph4', 'figure'),
            Output('my_graph5', 'figure'),
            Output('my_graph6', 'figure'),
            [Input('submit-button2', 'n_clicks')],
            [State('my_ticker_symbol2', 'value'),
                    State('my_day_window2', 'value'),
                    State('my_hour_window2', 'value')],
)


def update_graph2(n_clicks2, stock_ticker2, day2, hour2):

    '''
    ########################################################################
                            Second Section of Graphs
    ########################################################################

    '''
    if stock_ticker2 == ['All']:
        stock_ticker2 = ticker_list

    # Toggle Days
    if day2 == [5]:
        day2 = [0,1,2,3,4]
    # Toggle Hours
    if hour2 == [0]:
        hour2 = [9,10,11,12,13,14,15]

    # Get x_labels
    day_str = []
    for d in day2:
        if d == 0:
            day_str.append("Mon")
        elif d == 1:
            day_str.append("Tues")
        elif d == 2:
            day_str.append("Wed")
        elif d == 3:
            day_str.append("Thur")
        elif d == 4:
            day_str.append("Fri")

    x_label = []
    for d in day_str:
        for h in hour2:
            x_label.append(d + " " + str(h))

    ###################################################################################################################
    # Get y_data (Trim DF)
    df_first_slice = model_result_df.loc[(model_result_df['Ticker'].isin(stock_ticker2))]
    window_avgs_list = []
    for d in day2:
        for h in hour2:
            # Group DF by ticker, day, and hour
            df_slice = df_first_slice.loc[(df_first_slice['Weekday'] == d) & (df_first_slice['Hour'] == h)]

            # Get average for that group
            avg_for_window = statistics.mean(df_slice['ROC Score'])

            # append to stock_dict[ticker]
            window_avgs_list.append(avg_for_window)

    stock_df = pd.DataFrame()
    stock_df['Window'] = x_label
    stock_df['Returns'] = window_avgs_list

    fig4 = px.bar(stock_df, x='Window', y='Returns',
                    labels=dict(value='ROC Score (0 to 1)', variable="Ticker",Returns='Avg. ROC Score'),title="Portfolio Avg. ROC Score For Different Windows")

    fig4.update_xaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
    fig4.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')
    fig4.update_traces(marker_color='darkblue')

    ###################################################################################################################
    # Get y_data (Trim DF)
    df_first_slice = model_result_df.loc[(model_result_df['Ticker'].isin(stock_ticker2))]
    window_avgs_list = []
    for d in day2:
        for h in hour2:
            # Group DF by ticker, day, and hour
            df_slice = df_first_slice.loc[(df_first_slice['Weekday'] == d) & (df_first_slice['Hour'] == h)]

            # Get average for that group
            avg_for_window = statistics.mean(df_slice['Strat Return'])

            # append to stock_dict[ticker]
            window_avgs_list.append(round(avg_for_window*100,5))

    stock_df = pd.DataFrame()
    stock_df['Window'] = x_label
    stock_df['Returns'] = window_avgs_list

    fig5 = px.bar(stock_df, x='Window', y='Returns',
                    labels=dict(value='Avg. Strategy Return', variable="Ticker",Returns='Avg. Strategy Return (Already in %)'),title="Portfolio Avg. Strategy Returns For Different Windows")

    fig5.update_xaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
    fig5.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')
    fig5.update_traces(marker_color='darkblue')

    ###################################################################################################################
    # Get y_data (Trim DF)
    df_first_slice = model_result_df.loc[(model_result_df['Ticker'].isin(stock_ticker2))]
    window_avgs_list = []
    for d in day2:
        for h in hour2:
            # Group DF by ticker, day, and hour
            df_slice = df_first_slice.loc[(df_first_slice['Weekday'] == d) & (df_first_slice['Hour'] == h)]

            # Get average for that group
            avg_for_window = statistics.mean(df_slice['Passive Return'])

            # append to stock_dict[ticker]
            window_avgs_list.append(round(avg_for_window*100,5))

    stock_df = pd.DataFrame()
    stock_df['Window'] = x_label
    stock_df['Returns'] = window_avgs_list

    fig6 = px.bar(stock_df, x='Window', y='Returns',
                    labels=dict(value='Avg. Passive Return', variable="Ticker",Returns='Avg. Passive Return (Already in %)'),title="Portfolio Avg. Passive Returns For Different Windows")

    fig6.update_xaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
    fig6.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')
    fig6.update_traces(marker_color='darkblue')

    return fig4, fig5, fig6


@app.callback(Output('my_graph7', 'figure'),
            Output('my_graph8', 'figure'),
            Output('my_graph9', 'figure'),
            Output('my_graph10', 'figure'),
            [Input('submit-button3', 'n_clicks')],
            [State('datatable_id', 'selected_rows')],
)
def update_graph3(n_clicks3, chosen_rows):
    '''
    ########################################################################
                            Data Table
    ########################################################################

    '''
    if len(chosen_rows)==0:
        df_filterd = dff[dff['Ticker'].isin(['AGG'])]
    else:
        print(chosen_rows)
        df_filterd = dff[dff.index.isin(chosen_rows)]
    ###################################################################################

    '''
    ########################################################################
                            Third Section of Graphs
    ########################################################################

    '''


    # Toggle Days
    day3 = [0,1,2,3,4]
    # Toggle Hours
    hour3 = [9,10,11,12,13,14,15]

    # Get x_labels
    day_str = []
    for d in day3:
        if d == 0:
            day_str.append("Mon")
        elif d == 1:
            day_str.append("Tues")
        elif d == 2:
            day_str.append("Wed")
        elif d == 3:
            day_str.append("Thur")
        elif d == 4:
            day_str.append("Fri")

    x_label = []
    for d in day_str:
        for h in hour3:
            x_label.append(d + " " + str(h))

    ###################################################################################################################
    # Get y_data (Trim DF)
    window_avgs_list = []
    for d in day3:
        for h in hour3:
            # Group DF by ticker, day, and hour
            df_slice = df_filterd.loc[(df_filterd['Weekday'] == d) & (df_filterd['Hour'] == h)]

            # Get average for that group
            try:
                avg_for_window = statistics.mean(df_slice['ROC Score'])
            except:
                avg_for_window = 0

            # append to stock_dict[ticker]
            window_avgs_list.append(avg_for_window)

    stock_df = pd.DataFrame()
    stock_df['Window'] = x_label
    stock_df['Returns'] = window_avgs_list

    fig7 = px.bar(stock_df, x='Window', y='Returns',
                    labels=dict(value='ROC Score (0 to 1)', variable="Ticker",Returns='Avg. ROC Score'),title="Portfolio Avg. ROC Score For Different Windows")

    fig7.update_xaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
    fig7.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')
    fig7.update_traces(marker_color='darkred')

    ###################################################################################################################
    # Get y_data (Trim DF)
    window_avgs_strat = []
    for d in day3:
        for h in hour3:
            # Group DF by ticker, day, and hour
            df_slice = df_filterd.loc[(df_filterd['Weekday'] == d) & (df_filterd['Hour'] == h)]

            # Get average for that group
            try:
                avg_for_window = statistics.mean(df_slice['Strat Return'])
            except:
                avg_for_window = 0

            # append to list
            window_avgs_strat.append(round(avg_for_window*100,5))

    stock_df = pd.DataFrame()
    stock_df['Window'] = x_label
    stock_df['Returns'] = window_avgs_strat

    fig8 = px.bar(stock_df, x='Window', y='Returns',
                    labels=dict(value='Avg. Strategy Return', variable="Ticker",Returns='Avg. Strategy Return (Already in %)'),title="Portfolio Avg. Strategy Returns For Different Windows")

    fig8.update_xaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
    fig8.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')
    fig8.update_traces(marker_color='darkred')

    ###################################################################################################################
    # Get y_data (Trim DF)
    window_avgs_list = []
    for d in day3:
        for h in hour3:
            # Group DF by ticker, day, and hour
            df_slice = df_filterd.loc[(df_filterd['Weekday'] == d) & (df_filterd['Hour'] == h)]

            # Get average for that group
            try:
                avg_for_window = statistics.mean(df_slice['Passive Return'])
            except:
                avg_for_window = 0

            # append to list
            window_avgs_list.append(round(avg_for_window*100,5))

    stock_df = pd.DataFrame()
    stock_df['Window'] = x_label
    stock_df['Returns'] = window_avgs_list

    fig9 = px.bar(stock_df, x='Window', y='Returns',
                    labels=dict(value='Avg. Passive Return', variable="Ticker",Returns='Avg. Passive Return (Already in %)'),title="Portfolio Avg. Passive Returns For Different Windows")

    fig9.update_xaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
    fig9.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')
    fig9.update_traces(marker_color='darkred')

    #############################################################################################

    beg_cap = 100
    end_cap = beg_cap
    for rate in window_avgs_strat:
        profit = end_cap * (rate/100)
        end_cap = end_cap + profit

    weekly_rate = (end_cap - beg_cap)/ beg_cap

    annual_rate = (((1+weekly_rate)**52)-1)

    beg_cap = 100
    end_cap = beg_cap
    for rate in window_avgs_list:
        profit = end_cap * (rate/100)
        end_cap = end_cap + profit

    weekly_rate_pass = (end_cap - beg_cap)/ beg_cap

    annual_rate_pass = (((1+weekly_rate_pass)**52)-1)

    fig10 = go.Figure()

    fig10.add_trace(go.Indicator(
        mode = "number",
        title = {"text": "Model Returns<br><span style='font-size:0.8em;color:gray'>Weekly (Top) Annualized (Bottom)</span>"},
        number = {'suffix': "%"},
        value = round(weekly_rate*100,2),
        domain = {'x': [0, 0.5], 'y': [0.5, 1]}))

    fig10.add_trace(go.Indicator(
        mode = "number",
        number = {'suffix': "%"},
        value = round(annual_rate*100,2),
        domain = {'x': [0, 0.5], 'y': [0, 0.5]}))

    fig10.add_trace(go.Indicator(
        mode = "number",
        title = {"text": "Passive Returns<br><span style='font-size:0.8em;color:gray'>Weekly (Top) Annualized (Bottom)</span>"},
        number = {'suffix': "%"},
        value = round(weekly_rate_pass*100,2),
        domain = {'x': [0.5, 1], 'y': [0.5, 1]}))

    fig10.add_trace(go.Indicator(
        mode = "number",
        number = {'suffix': "%"},
        value = round(annual_rate_pass*100,2),
        domain = {'x': [0.5, 1], 'y': [0, 0.5]}))

    return fig7, fig8, fig9, fig10


if __name__ == '__main__':
    app.run_server()
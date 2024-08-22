import dash
from dash import dcc, html, Input, Output, dash_table, State
import pandas as pd
import plotly.express as px
import base64
import io

# Main function
def main():
    app = create_dash_app()
    app.run_server(debug=True)

# Function to create the Dash app
def create_dash_app():
    external_stylesheets = ['https://bootswatch.com/5/darkly/bootstrap.min.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    app.layout = html.Div([
        html.Div([
            html.H1("Interactive Data Dashboard", style={'textAlign': 'center', 'marginBottom': '20px', 'color': 'white'}),
        ], className='row'),
        html.Div([
            dcc.Upload(
                id='upload-data',
                children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'marginBottom': '20px',
                    'backgroundColor': '#444'
                },
                multiple=False
            ),
        ], className='row'),
        html.Div([
            html.Button('Back', id='undo-button', n_clicks=0, className='btn btn-primary', style={'marginBottom': '20px'}),
        ], className='row'),
        html.Div([
            dash_table.DataTable(
                id='data-table',
                columns=[],
                data=[],
                style_table={'overflowX': 'auto'},
                style_header={'backgroundColor': 'rgb(30, 30, 30)', 'color': 'white'},
                style_cell={'backgroundColor': 'rgb(50, 50, 50)', 'color': 'white'}
            ),
        ], className='row'),
        html.Div([
            html.Div([
                dcc.Dropdown(id='x-axis-dropdown', style={'color': 'black'}),
            ], className='six columns'),
            html.Div([
                dcc.Dropdown(id='y-axis-dropdown', style={'color': 'black'}),
            ], className='six columns')
        ], className='row', style={'marginTop': '20px'}),
        html.Div([
            dcc.Graph(id='bar-chart'),
        ], className='row', style={'marginTop': '20px'})
    ], className='container')

    register_callbacks(app)
    return app

# Function to register callbacks
def register_callbacks(app):
    @app.callback(
        [Output('data-table', 'data'),
         Output('data-table', 'columns'),
         Output('x-axis-dropdown', 'options'),
         Output('y-axis-dropdown', 'options'),
         Output('x-axis-dropdown', 'value'),
         Output('y-axis-dropdown', 'value')],
        [Input('upload-data', 'contents'),
         Input('upload-data', 'filename'),
         Input('undo-button', 'n_clicks')],
        [State('data-table', 'data')]
    )
    def update_output(contents, filename, n_clicks, current_data):
        if contents is not None:
            content_type, content_string = contents.split(',')
            decoded = base64.b64decode(content_string)
            try:
                df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
            except Exception as e:
                return current_data, [], [], [], None, None

            columns = [{"name": i, "id": i} for i in df.columns]
            data = df.to_dict('records')
            options = [{'label': col, 'value': col} for col in df.columns]
            return data, columns, options, options, df.columns[0], df.columns[1]

        if n_clicks > 0:
            return [], [], [], [], None, None

        return current_data, [], [], [], None, None

    @app.callback(
        Output('bar-chart', 'figure'),
        [Input('x-axis-dropdown', 'value'),
         Input('y-axis-dropdown', 'value'),
         State('data-table', 'data')]
    )
    def update_bar_chart(x_col, y_col, table_data):
        if x_col and y_col and table_data:
            df = pd.DataFrame(table_data)
            fig = px.bar(df, x=x_col, y=y_col)
            return fig
        return {}

    app.update_output = update_output  # Export the callback function
    app.update_bar_chart = update_bar_chart  # Export the callback function

if __name__ == '__main__':
    main()

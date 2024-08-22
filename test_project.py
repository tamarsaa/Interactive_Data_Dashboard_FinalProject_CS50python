import pytest
from dash import Dash

from project import create_dash_app

def test_create_dash_app():
    app = create_dash_app()
    assert app is not None

def test_update_output():
    app = Dash(__name__)
    app.update_output = create_dash_app().update_output
    result = app.update_output(None, None, 0, [])
    assert result == ([], [], [], [], None, None)

def test_update_output_with_data():
    app = Dash(__name__)
    app.update_output = create_dash_app().update_output
    content = 'data:text/csv;base64,Y29sMSxjb2wyCmRhdGExLGRhdGEyCmRhdGEzLGRhdGE0Cg=='
    filename = 'test.csv'
    result = app.update_output(content, filename, 0, [])
    assert len(result[0]) > 0  # Check if data is returned

def test_update_bar_chart():
    app = Dash(__name__)
    app.update_bar_chart = create_dash_app().update_bar_chart
    result = app.update_bar_chart(None, None, [])
    assert result == {}

def test_update_bar_chart_with_data():
    app = Dash(__name__)
    app.update_bar_chart = create_dash_app().update_bar_chart
    x_col = 'col1'
    y_col = 'col2'
    table_data = [{'col1': 'data1', 'col2': 'data2'}, {'col1': 'data3', 'col2': 'data4'}]
    result = app.update_bar_chart(x_col, y_col, table_data)
    assert result is not None

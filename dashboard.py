"""
Simple Plotly Dash frontend for CareerBot Employee Management API
"""
import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import requests
from datetime import datetime

# API Configuration
API_BASE_URL = "http://localhost:8000"

# Initialize Dash app
app = dash.Dash(__name__, title="CareerBot Dashboard")

# Custom styles
COLORS = {
    'background': '#f5f5f5',
    'text': '#2c3e50',
    'primary': '#3498db',
    'success': '#2ecc71',
    'danger': '#e74c3c',
    'card': '#ffffff'
}

app.layout = html.Div(style={'backgroundColor': COLORS['background'], 'padding': '20px'}, children=[
    # Header
    html.Div([
        html.H1('CareerBot Employee Dashboard',
                style={'color': COLORS['text'], 'textAlign': 'center', 'marginBottom': '10px'}),
        html.P('Real-time employee management and analytics',
               style={'textAlign': 'center', 'color': '#7f8c8d', 'fontSize': '16px'})
    ]),

    html.Hr(),

    # Refresh button
    html.Div([
        html.Button('Refresh Data', id='refresh-button', n_clicks=0,
                   style={'backgroundColor': COLORS['primary'], 'color': 'white',
                          'border': 'none', 'padding': '10px 20px', 'fontSize': '16px',
                          'borderRadius': '5px', 'cursor': 'pointer', 'marginBottom': '20px'})
    ], style={'textAlign': 'center'}),

    # Store for employee data
    dcc.Store(id='employee-data'),

    # Summary Statistics
    html.Div(id='summary-stats', style={'marginBottom': '30px'}),

    # Charts Section
    html.Div([
        html.Div([
            html.H3('Employees by Department', style={'color': COLORS['text']}),
            dcc.Graph(id='department-chart')
        ], style={'width': '48%', 'display': 'inline-block', 'backgroundColor': COLORS['card'],
                  'padding': '20px', 'borderRadius': '10px', 'marginRight': '2%'}),

        html.Div([
            html.H3('Average Salary by Department', style={'color': COLORS['text']}),
            dcc.Graph(id='salary-chart')
        ], style={'width': '48%', 'display': 'inline-block', 'backgroundColor': COLORS['card'],
                  'padding': '20px', 'borderRadius': '10px'})
    ], style={'marginBottom': '30px'}),

    # Employee Table
    html.Div([
        html.H3('Employee Directory', style={'color': COLORS['text'], 'marginBottom': '15px'}),
        html.Div(id='employee-table')
    ], style={'backgroundColor': COLORS['card'], 'padding': '20px', 'borderRadius': '10px'}),

    # Footer
    html.Div([
        html.Hr(),
        html.P('Last updated: ', style={'display': 'inline', 'color': '#7f8c8d'}),
        html.Span(id='last-update', style={'color': COLORS['primary'], 'fontWeight': 'bold'})
    ], style={'textAlign': 'center', 'marginTop': '30px'})
])


def fetch_employees():
    """Fetch employee data from the API"""
    try:
        response = requests.get(f"{API_BASE_URL}/employees")
        if response.status_code == 200:
            return response.json()
        else:
            return []
    except Exception as e:
        print(f"Error fetching employees: {e}")
        return []


@app.callback(
    Output('employee-data', 'data'),
    Input('refresh-button', 'n_clicks')
)
def update_employee_data(n_clicks):
    """Update employee data from API"""
    employees = fetch_employees()
    return employees


@app.callback(
    [Output('summary-stats', 'children'),
     Output('department-chart', 'figure'),
     Output('salary-chart', 'figure'),
     Output('employee-table', 'children'),
     Output('last-update', 'children')],
    Input('employee-data', 'data')
)
def update_dashboard(employees):
    """Update all dashboard components"""
    if not employees:
        empty_msg = html.Div([
            html.H4('No data available', style={'color': COLORS['danger'], 'textAlign': 'center'}),
            html.P('Make sure the API is running on http://localhost:8000',
                   style={'textAlign': 'center', 'color': '#7f8c8d'})
        ])
        empty_fig = go.Figure()
        empty_fig.update_layout(template='plotly_white')
        return empty_msg, empty_fig, empty_fig, empty_msg, 'N/A'

    # Convert to DataFrame
    df = pd.DataFrame(employees)

    # Summary Statistics
    total_employees = len(df)
    total_departments = df['department'].nunique()
    avg_salary = df['salary'].mean()
    total_payroll = df['salary'].sum()

    summary = html.Div([
        html.Div([
            html.Div([
                html.H4(str(total_employees), style={'fontSize': '36px', 'margin': '0', 'color': COLORS['primary']}),
                html.P('Total Employees', style={'margin': '0', 'color': '#7f8c8d'})
            ], style={'backgroundColor': COLORS['card'], 'padding': '20px', 'borderRadius': '10px',
                      'textAlign': 'center', 'width': '23%', 'display': 'inline-block', 'marginRight': '2%'}),

            html.Div([
                html.H4(str(total_departments), style={'fontSize': '36px', 'margin': '0', 'color': COLORS['success']}),
                html.P('Departments', style={'margin': '0', 'color': '#7f8c8d'})
            ], style={'backgroundColor': COLORS['card'], 'padding': '20px', 'borderRadius': '10px',
                      'textAlign': 'center', 'width': '23%', 'display': 'inline-block', 'marginRight': '2%'}),

            html.Div([
                html.H4(f'${avg_salary:,.0f}', style={'fontSize': '36px', 'margin': '0', 'color': '#e67e22'}),
                html.P('Average Salary', style={'margin': '0', 'color': '#7f8c8d'})
            ], style={'backgroundColor': COLORS['card'], 'padding': '20px', 'borderRadius': '10px',
                      'textAlign': 'center', 'width': '23%', 'display': 'inline-block', 'marginRight': '2%'}),

            html.Div([
                html.H4(f'${total_payroll:,.0f}', style={'fontSize': '36px', 'margin': '0', 'color': '#9b59b6'}),
                html.P('Total Payroll', style={'margin': '0', 'color': '#7f8c8d'})
            ], style={'backgroundColor': COLORS['card'], 'padding': '20px', 'borderRadius': '10px',
                      'textAlign': 'center', 'width': '23%', 'display': 'inline-block'})
        ])
    ])

    # Department Chart
    dept_counts = df['department'].value_counts().reset_index()
    dept_counts.columns = ['Department', 'Count']

    dept_fig = px.pie(dept_counts, values='Count', names='Department',
                      title='',
                      color_discrete_sequence=px.colors.qualitative.Set3)
    dept_fig.update_traces(textposition='inside', textinfo='percent+label')
    dept_fig.update_layout(showlegend=False, template='plotly_white')

    # Salary Chart
    salary_by_dept = df.groupby('department')['salary'].mean().reset_index()
    salary_by_dept.columns = ['Department', 'Average Salary']
    salary_by_dept = salary_by_dept.sort_values('Average Salary', ascending=True)

    salary_fig = px.bar(salary_by_dept, x='Average Salary', y='Department',
                        orientation='h',
                        title='',
                        color='Average Salary',
                        color_continuous_scale='Blues')
    salary_fig.update_layout(showlegend=False, template='plotly_white',
                            xaxis_title='Average Salary ($)',
                            yaxis_title='')
    salary_fig.update_traces(text=salary_by_dept['Average Salary'].apply(lambda x: f'${x:,.0f}'),
                            textposition='outside')

    # Employee Table
    table_df = df[['id', 'name', 'email', 'department', 'position', 'salary', 'hire_date']].copy()
    table_df['salary'] = table_df['salary'].apply(lambda x: f'${x:,.2f}')

    employee_table = dash_table.DataTable(
        data=table_df.to_dict('records'),
        columns=[{'name': col.replace('_', ' ').title(), 'id': col} for col in table_df.columns],
        style_table={'overflowX': 'auto'},
        style_cell={
            'textAlign': 'left',
            'padding': '10px',
            'fontFamily': 'Arial, sans-serif'
        },
        style_header={
            'backgroundColor': COLORS['primary'],
            'color': 'white',
            'fontWeight': 'bold'
        },
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': '#f9f9f9'
            }
        ],
        page_size=10,
        sort_action='native',
        filter_action='native'
    )

    last_update = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return summary, dept_fig, salary_fig, employee_table, last_update


if __name__ == '__main__':
    print("Starting CareerBot Dashboard...")
    print("Dashboard will be available at: http://localhost:8050")
    print("Make sure the FastAPI backend is running on http://localhost:8000")
    app.run_server(debug=True, host='0.0.0.0', port=8050)

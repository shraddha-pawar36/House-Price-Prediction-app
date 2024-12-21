
import joblib, dash
from dash import dcc,Dash, html, Input, Output, State,dash_table
import pandas as pd
from sklearn.linear_model import LinearRegression

# load the data
df = pd.read_csv('USA_Housing.csv')

sample = df.head()

# load the model
model = joblib.load('train.pkl')

# Initialize the app
app = dash.Dash(__name__)

# layout
app.layout = html.Div([
    html.H1('House Price Prediction App',style={
            'textAlign': 'center',
            'color': 'blue'
        }),
    html.H2('Sample Data'),
    dash_table.DataTable(data=sample.to_dict('records'),style_header={
        'border':'solid',
            'backgroundColor': 'lightblue',
            'fontWeight': 'bold'
        },
        style_cell={
            'border':'solid',
            'backgroundColor':'lightgray',
            'textAlign': 'center'
        }),
    html.H2('Enter the input values to predict the Price of House'),
    html.Label('Enter Average Area Income: '),
    dcc.Input(id='input-income', type='number', placeholder='Avg. Area Income'),
    html.Br(),html.Br(),
    html.Label('Enter Average Area House Age: '),
    dcc.Input(id='input-house-age', type='number', placeholder='Avg. Area House Age'),
    html.Br(),html.Br(),
    html.Label('Enter Average Number of rooms: '),
    dcc.Input(id='input-num-rooms', type='number', placeholder='Avg. Area Number of Rooms'),
    html.Br(),html.Br(),
    html.Label('Enter Average Area Number of Bedrooms: '),
    dcc.Input(id='input-num-bedrooms', type='number', placeholder='Avg. Area Number of Bedrooms'),
    html.Br(),html.Br(),
    html.Label('Enter Area Population: '),
    dcc.Input(id='input-area-population', type='number', placeholder='Area Population'),
    html.Br(),html.Br(),
    html.Label('Click to predict House Price: '),
    html.Button('Predict House Price', id='predict-button', n_clicks=0,style={'border':'solid',
            'backgroundColor': 'skyblue',
            'fontWeight': 'bold'}),
    html.Br(),html.Br(),
    html.Div(id='output-prediction')
])

@app.callback(
    Output('output-prediction', 'children'),
    [Input('predict-button', 'n_clicks')],
    [State('input-income', 'value'),
     State('input-house-age', 'value'),
     State('input-num-rooms', 'value'),
     State('input-num-bedrooms', 'value'),
     State('input-area-population', 'value')],
    prevent_initial_call=True
)
def update_prediction(n_clicks, income, house_age, num_rooms, num_bedrooms, area_population):
    if n_clicks == 0:
        return dash.no_update

    # Prepare the features for prediction
    features = pd.DataFrame({
        'Avg. Area Income': [income],
        'Avg. Area House Age': [house_age],
        'Avg. Area Number of Rooms': [num_rooms],
        'Avg. Area Number of Bedrooms': [num_bedrooms],
        'Area Population': [area_population]
    })

    # Predict house price using the loaded model
    prediction = model.predict(features)

    return f'Predicted House Price: ${prediction[0]:,.2f}'

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
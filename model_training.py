# import libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# load data
df = pd.read_csv('USA_Housing.csv')

# split the data
x = df.iloc[:, 0:5]
y = df['Price']

model = LinearRegression()
# Train/ Fit the model

model.fit(x,y)
# save Trained Model
joblib.dump(model, 'train.pkl')

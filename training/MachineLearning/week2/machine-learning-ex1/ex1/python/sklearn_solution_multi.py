
import matplotlib.pyplot as plt
import numpy as np
from sklearn import  linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

df = pd.read_csv('../ex1data2.txt', names=['x','x2', 'y'])
x = pd.DataFrame(df, columns=['x', 'x2']).as_matrix(columns=['x','x2'])
y = pd.DataFrame(df, columns=['y'])
# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(x, y)

# Make predictions using the testing set
y_pred = regr.predict(x)

print('y pred', y_pred);
plt.scatter(x, y,  color='black')
plt.plot(x, y_pred, color='blue', linewidth=3)
plt.show()
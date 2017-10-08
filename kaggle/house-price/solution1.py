# https://www.dataquest.io/blog/kaggle-getting-started/

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error


train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

print ("Train data shape:", train.shape)
print ("Test data shape:", test.shape)

train.head()
train.SalePrice.describe()
print ("Skew is:", train.SalePrice.skew())
plt.hist(train.SalePrice, color='blue')

target = np.log(train.SalePrice)
print ("Skew is:", target.skew())
plt.hist(target, color='blue')

# Working with Numeric Features

numeric_features = train.select_dtypes(include=[np.number])
numeric_features.dtypes

corr = numeric_features.corr()

print (corr['SalePrice'].sort_values(ascending=False)[:5], '\n')
print (corr['SalePrice'].sort_values(ascending=False)[-5:])
train.OverallQual.unique()

quality_pivot = train.pivot_table(index='OverallQual',
                                  values='SalePrice', aggfunc=np.median)

quality_pivot.plot(kind='bar', color='blue')
plt.xlabel('Overall Quality')
plt.ylabel('Median Sale Price')
plt.xticks(rotation=0)

plt.scatter(x=train['GrLivArea'], y=target)
plt.ylabel('Sale Price')
plt.xlabel('Above grade (ground) living area square feet')

plt.scatter(x=train['GarageArea'], y=target)
plt.ylabel('Sale Price')
plt.xlabel('Garage Area')

#Handling Null Values

nulls = pd.DataFrame(train.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
nulls

print ("Unique values are:", train.MiscFeature.unique())

# Wrangling the non-numeric Features

categoricals = train.select_dtypes(exclude=[np.number])
categoricals.describe()

# Transforming and engineering features

print ("Original: \n") 
print (train.Street.value_counts(), "\n")

train['enc_street'] = pd.get_dummies(train.Street, drop_first=True)
test['enc_street'] = pd.get_dummies(train.Street, drop_first=True)
print ('Encoded: \n') 
print (train.enc_street.value_counts())

condition_pivot = train.pivot_table(index='SaleCondition',
                                    values='SalePrice', aggfunc=np.median)
condition_pivot.plot(kind='bar', color='blue')
plt.xlabel('Sale Condition')
plt.ylabel('Median Sale Price')
plt.xticks(rotation=0)
def encode(x): return 1 if x == 'Partial' else 0
train['enc_condition'] = train.SaleCondition.apply(encode)
test['enc_condition'] = test.SaleCondition.apply(encode)

condition_pivot = train.pivot_table(index='enc_condition', values='SalePrice', aggfunc=np.median)
condition_pivot.plot(kind='bar', color='blue')
plt.xlabel('Encoded Sale Condition')
plt.ylabel('Median Sale Price')
plt.xticks(rotation=0)

# Alley
def alleyEncode(x): return 1 if x == 'Pave' else 0
train['alley_condition'] = train.Alley.apply(alleyEncode)
test['alley_condition'] = test.Alley.apply(alleyEncode)

# GarageFinish
def GarageFinishEncode(x): 
  if x == 'Fin': 
    return 2 
  elif x == 'RFn':
    return 1
  return 0

train['GarageFinish_condition'] = train.GarageFinish.apply(GarageFinishEncode)
test['GarageFinish_condition'] = test.GarageFinish.apply(GarageFinishEncode)


data = train.select_dtypes(include=[np.number]).interpolate().dropna() 

sum(data.isnull().sum() != 0)

# Build a linear model

y = np.log(train.SalePrice)
X = data.drop(['SalePrice', 'Id'], axis=1)


X_train, X_test, y_train, y_test = train_test_split(
                                    X, y, random_state=42, test_size=.33)

lr = linear_model.LinearRegression()

model = lr.fit(X_train, y_train)
print ("R^2 is: \n", model.score(X_test, y_test))

predictions = model.predict(X_test)

print ('RMSE is: \n', mean_squared_error(y_test, predictions))

actual_values = y_test
plt.scatter(predictions, actual_values, alpha=.75,
            color='b') #alpha helps to show overlapping data
plt.xlabel('Predicted Price')
plt.ylabel('Actual Price')
plt.title('Linear Regression Model')

submission = pd.DataFrame()
submission['Id'] = test.Id

feats = test.select_dtypes(
        include=[np.number]).drop(['Id'], axis=1).interpolate()

predictions = model.predict(feats)

final_predictions = np.exp(predictions)

print ("Original predictions are: \n", predictions[:5], "\n")
print ("Final predictions are: \n", final_predictions[:5])

submission['SalePrice'] = final_predictions
submission.head()

submission.to_csv('data/submission2.csv', index=False)


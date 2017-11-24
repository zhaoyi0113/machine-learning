# https://www.kaggle.com/c/sberbank-russian-housing-market/data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')


def deal_with_missing_data(data_set):
    null_data = data_set.isnull().sum().sort_values(ascending=False)
    percent = (data_set.isnull().sum() / data_set.isnull().count()
               ).sort_values(ascending=False)
    missing_data = pd.concat([null_data, percent],
                             axis=1, keys=['Total', 'Percent'])
    missing_data.head(20)
    filtered_data = data_set.drop(
        (missing_data[missing_data['Total'] > 1]).index, 1)
    return filtered_data

def analyze_data(data_set):
    numeric_features = data_set.select_dtypes(include=[np.number])
    # correlations
    corr = numeric_features.corr()
    print(corr['price_doc'].sort_values(ascending=False)[:5], '\n')
    print(corr['price_doc'].sort_values(ascending=False)[-5:])
    # full_sq has high correlation with price_doc
    full_sq_pivot = data_set.pivot_table(index='full_sq', values='price_doc', aggfunc=np.median)
    full_sq_pivot.plot(kind='bar', color='blue')
    plt.xlabel('full_sq')
    plt.ylabel('Median Sale Price')
    plt.xticks(rotation=0)
    plt.show()

def linearRegression(df, test):
    regr = linear_model.LinearRegression()
    cols = ['full_sq', 'sport_count_5000', 'sport_count_3000',
            'trc_count_5000', 'sport_count_2000', 'office_sqm_5000']
    x = pd.DataFrame(df, columns=cols).as_matrix(columns=cols)
    testX = pd.DataFrame(test, columns=cols).as_matrix(columns=cols)
    y = pd.DataFrame(df, columns=['price_doc'])
    regr.fit(x, y)
    y_pred = regr.predict(testX)
    print('y pred', y_pred)
    return y_pred


filtered_data = deal_with_missing_data(train)

pred = linearRegression(filtered_data, test)

final = pd.DataFrame(data=(test['id']))
final['price_doc']=pred

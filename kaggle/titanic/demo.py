import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import random
import numpy as np
import pandas as pd
from sklearn import datasets, svm, cross_validation, tree, preprocessing, metrics
import sklearn.ensemble as ske
import tensorflow as tf
from tensorflow.contrib import learn
# import tensorflow.contrib.learn.python.learn as learn
# from sklearn import datasets, metrics


titanic_df = pd.read_excel('data/titanic3.xls', 'titanic3', index_col=None, na_values=['NA'])
# print("%s\n", titanic_df.head())
print('overall survive mean \n', titanic_df['survived'].mean())
print('survived rate by class \n', titanic_df.groupby('pclass').mean())
class_sex_grouping = titanic_df.groupby(['pclass','sex']).mean()
print('group by class and sex \n', class_sex_grouping)

group_by_age = pd.cut(titanic_df["age"], np.arange(0, 90, 10))
age_grouping = titanic_df.groupby(group_by_age).mean()

titanic_df = titanic_df.drop(['body','cabin','boat'], axis=1)
titanic_df["home.dest"] = titanic_df = titanic_df.dropna()
titanic_df["home.dest"].fillna("NA")

print('count\n', titanic_df.count())


def preprocess_titanic_df(df):
    processed_df = df.copy()
    le = preprocessing.LabelEncoder()
    processed_df.sex = le.fit_transform(processed_df.sex)
    processed_df.embarked = le.fit_transform(processed_df.embarked)
    processed_df = processed_df.drop(['name','ticket','home.dest'],axis=1)
    return processed_df

processed_df = preprocess_titanic_df(titanic_df)

X = processed_df.drop(['survived'], axis=1).values
y = processed_df['survived'].values

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.2)

clf_dt = tree.DecisionTreeClassifier(max_depth=10)
clf_dt.fit (X_train, y_train)
print(clf_dt.score (X_test, y_test))

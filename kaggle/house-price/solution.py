import matplotlib.pyplot as plt
import numpy as np
from sklearn import  linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import seaborn as sns
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats


def boxPlotVar(var):
  data = pd.concat([df_train['SalePrice'], df_train[var]], axis=1)
  f, ax = plt.subplots(figsize=(8, 6))
  fig = sns.boxplot(x=var, y="SalePrice", data=data)
  fig.axis(ymin=0, ymax=800000);

def scatterPlotVar(var):
  data = pd.concat([df_train['SalePrice'], df_train[var]], axis=1)
  data.plot.scatter(x=var, y='SalePrice', ylim=(0,800000));

def handleMissingData(df_train):
  # missing data
  df_train.isnull().sum()  # get the number of na values for each columns
  total = df_train.isnull().sum().sort_values(ascending=False)
  percent = (df_train.isnull().sum()/df_train.isnull().count()).sort_values(ascending=False)
  missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
  missing_data.head(20)
  #dealing with missing data
  df_train = df_train.drop((missing_data[missing_data['Total'] > 1]).index,1)
  df_train = df_train.drop(df_train.loc[df_train['Electrical'].isnull()].index)
  df_train.isnull().sum().max() #just checking that there's no missing data missing...
  return df_train

def corrPlot(df_train):
  # correlation matrix
  corrmat = df_train.corr()
  f, ax = plt.subplots(figsize=(12, 9))
  sns.heatmap(corrmat, vmax=.8, square=True);

  #saleprice correlation matrix
  k = 10 #number of variables for heatmap
  cols = corrmat.nlargest(k, 'SalePrice')['SalePrice'].index
  cm = np.corrcoef(df_train[cols].values.T)
  sns.set(font_scale=1.25)
  hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)

  #scatterplot
  sns.set()
  cols = ['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt']
  sns.pairplot(df_train[cols], size = 2.5)

def linearRegression(df, test):
  regr = linear_model.LinearRegression()
  cols = ['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt']
  x = pd.DataFrame(df, columns=cols).as_matrix(columns=cols)
  testX = pd.DataFrame(test, columns=cols).as_matrix(columns=cols)
  y = pd.DataFrame(df, columns=['SalePrice'])
  regr.fit(x, y)
  y_pred = regr.predict(testX)
  print('y pred', y_pred);

def plotData(df_train):
  try:
    #histogram
    sns.distplot(df_train['SalePrice']);
  except:
    pass

  ##skewness and kurtosis
  print("Skewness: %f" % df_train['SalePrice'].skew())
  print("Kurtosis: %f" % df_train['SalePrice'].kurt())
  #Relationship with numerical variables
  ##scatter plot grlivarea/saleprice
  scatterPlotVar('GrLivArea')

  ##catter plot totalbsmtsf/saleprice
  scatterPlotVar('TotalBsmtSF')

  # Relationship with categorical features
  ## box plot overallqual/saleprice
  boxPlotVar('OverallQual')
  boxPlotVar('YearBuilt')

  corrPlot(df_train)
  plt.show()

df_train = pd.read_csv('./data/train.csv')
df_test = pd.read_csv('./data/test.csv');

df_train = handleMissingData(df_train)

# plotData(df_train)

linearRegression(df_train, df_test)

# 
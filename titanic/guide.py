# data analysis and wrangling
import pandas as pd
import numpy as np
import random as rnd
import os
# visualization
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

# machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier


# The Python Pandas packages helps us work with our datasets. We start by acquiring the training and testing datasets into Pandas DataFrames. We also combine these datasets to run certain operations on both datasets together.
# In [2]:
# Acquire data¶

train_df = pd.read_csv('./data/train.csv')
test_df = pd.read_csv('./data/test.csv')
combine = [train_df, test_df]

# Analyze by describing data
# Pandas also helps describe the datasets answering following questions
# early in our project.

# Which features are available in the dataset?

# Noting the feature names for directly manipulating or analyzing these. These feature names are described on the Kaggle data page here.
# In [3]:

print(train_df.columns.values)

# Which features are categorical?
# These values classify the samples into sets of similar samples. Within
# categorical features are the values nominal, ordinal, ratio, or interval
# based? Among other things this helps us select the appropriate plots for
# visualization.
# Categorical: Survived, Sex, and Embarked. Ordinal: Pclass.

# Which features are numerical?

# Which features are numerical? These values change from sample to sample.
# Within numerical features are the values discrete, continuous, or
# timeseries based? Among other things this helps us select the
# appropriate plots for visualization.
# Continous: Age, Fare. Discrete: SibSp, Parch.

# preview the data
head = train_df.head()
print(head)

# Which features are mixed data types?

# Numerical, alphanumeric data within same feature. These are candidates
# for correcting goal.

# Ticket is a mix of numeric and alphanumeric data types. Cabin is
# alphanumeric.

# Which features may contain errors or typos?

# This is harder to review for a large dataset, however reviewing a few samples from a smaller dataset may just tell us outright, which features may require correcting.
# Name feature may contain errors or typos as there are several ways used
# to describe a name including titles, round brackets, and quotes used for
# alternative or short names.

tail = train_df.tail()
print(tail)

# Which features contain blank, null or empty values?
# These will require correcting.

# Cabin > Age > Embarked features contain a number of null values in that order for the training dataset.
# Cabin > Age are incomplete in case of test dataset.

# What are the data types for various features?

# Helping us during converting goal.
# Seven features are integer or floats. Six in case of test dataset.
# Five features are strings (object).
print(train_df.info())
print('_' * 40)
print(test_df.info())

# What is the distribution of numerical feature values across the samples?

# This helps us determine, among other early insights, how representative is the training dataset of the actual problem domain.
# Total samples are 891 or 40% of the actual number of passengers on board the Titanic (2,224).
# Survived is a categorical feature with 0 or 1 values.
# Around 38% samples survived representative of the actual survival rate at 32%.
# Most passengers (> 75%) did not travel with parents or children.
# Nearly 30% of the passengers had siblings and/or spouse aboard.
# Fares varied significantly with few passengers (<1%) paying as high as $512.
# Few elderly passengers (<1%) within age range 65-80.

print(train_df.describe())

# Review survived rate using `percentiles=[.61, .62]` knowing our problem description mentions 38% survival rate.
# Review Parch distribution using `percentiles=[.75, .8]`
# SibSp distribution `[.68, .69]`
# Age and Fare `[.1, .2, .3, .4, .5, .6, .7, .8, .9, .99]`

# What is the distribution of categorical features?
# Names are unique across the dataset (count=unique=891)
# Sex variable as two possible values with 65% male (top=male, freq=577/count=891).
# Cabin values have several dupicates across samples. Alternatively several passengers shared a cabin.
# Embarked takes three possible values. S port used by most passengers (top=S)
# Ticket feature has high ratio (22%) of duplicate values (unique=681).

print(train_df.describe(include=['O']))

# print(train_df[['Pclass', 'Survived']].groupby(['Pclass']))

print(train_df[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived', ascending=False))

print(train_df[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False))

print(train_df[["SibSp", "Survived"]].groupby(['SibSp'], as_index=False).mean().sort_values(by='Survived', ascending=False))

print(train_df[["Parch", "Survived"]].groupby(['Parch'], as_index=False).mean().sort_values(by='Survived', ascending=False))

g = sns.FacetGrid(train_df, col='Survived')
g.map(plt.hist, 'Age', bins=20)
os.system("pause")
plt.show()
# https://www.kaggle.com/c/sberbank-russian-housing-market/data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')


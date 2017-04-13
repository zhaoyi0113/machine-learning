import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Creating a Series by passing a list of values, letting pandas create a default integer index:
s = pd.Series([1,3,5,np.nan,6,8])
print(s)

#Creating a DataFrame by passing a numpy array, with a datetime index and labeled columns:
dates = pd.date_range('20130101', periods=6)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df)

# Creating a DataFrame by passing a dict of objects that can be converted to series-like.

df2 = pd.DataFrame({ 'A' : 1.,
                        'B' : pd.Timestamp('20130102'),
                        'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                        'D' : np.array([3] * 4,dtype='int32'),
                        'E' : pd.Categorical(["test","train","test","train"]),
                        'F' : 'foo' })
print(df2)

# Having specific dtypes
print(df2.dtypes)

#See the top & bottom rows of the frame

print(df.head())

print(df.tail(3))
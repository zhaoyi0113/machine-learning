# https://www.springboard.com/blog/beginners-guide-neural-network-in-python-scikit-learn-0-18/
import pandas as pd
from sklearn.model_selection import train_test_split


wine = pd.read_csv('data/wine_data.csv', names = ["Cultivator", "Alchol", "Malic_Acid", "Ash", "Alcalinity_of_Ash", "Magnesium", "Total_phenols", "Falvanoids", "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue", "OD280", "Proline"])

# Data Preprocessing

X = wine.drop('Cultivator',axis=1)
y = wine['Cultivator']

X_train, X_test, y_train, y_test = train_test_split(X, y)

## scale data

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Fit only to the training data
scaler.fit(X_train)
StandardScaler(copy=True, with_mean=True, with_std=True)

# Now apply the transformations to the data:
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Training the model

from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(13,13,13),max_iter=500)

mlp.fit(X_train,y_train)

# Predicitions

predictions = mlp.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix

print(confusion_matrix(y_test,predictions))

print(classification_report(y_test,predictions))



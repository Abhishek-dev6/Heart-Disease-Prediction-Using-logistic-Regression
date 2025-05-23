# -*- coding: utf-8 -*-
"""HeartDisease.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CL47iR6BNOfm8WnUoW9gH7kSM5X3gpwS
"""

#@title Load The Dataset
import pandas as pd
df = pd.read_csv("/content/Heart_Disease_Prediction.csv")
df.head()
df.info()

print(df.columns.tolist())

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df.drop('Heart Disease', axis=1))

from sklearn.model_selection import train_test_split
X = df.drop('Heart Disease', axis=1)
y = df['Heart Disease']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)

from sklearn.metrics import classification_report, confusion_matrix
y_pred = model.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

from sklearn.model_selection import GridSearchCV
params = {'C': [0.1, 1, 10]}
grid = GridSearchCV(LogisticRegression(), param_grid=params)
grid.fit(X_train, y_train)

import matplotlib.pyplot as plt
importances = model.coef_[0]
features = X.columns
plt.barh(features, importances)

sample = [[57, 1, 2, 140, 241, 0, 1, 123, 1, 0.2, 2, 0, 2]]
pred = model.predict(sample)
print("Heart disease risk:", "Yes,chance of coming Heart Disease" if pred[0] == 1 else "No,chance of coming Heart Disease")
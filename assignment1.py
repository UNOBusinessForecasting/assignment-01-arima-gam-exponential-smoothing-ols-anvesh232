# -*- coding: utf-8 -*-
"""assignment1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZScd4FSvkWtEzEa_wojw9J2jJVgIAk5r
"""

import pandas as pd
url="https://github.com/dustywhite7/econ8310-assignment1/raw/main/assignment_data_train.csv"
url1="https://github.com/dustywhite7/econ8310-assignment1/raw/main/assignment_data_test.csv"
df=pd.read_csv(url)
df_test=pd.read_csv(url1)

df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df_test['Timestamp'] = pd.to_datetime(df_test['Timestamp'])
for data in [df, df_test]:
    data['year'] = data['Timestamp'].dt.year
    data['month'] = data['Timestamp'].dt.month
    data['day'] = data['Timestamp'].dt.day
    data['hour'] = data['Timestamp'].dt.hour
    data['day_of_week'] = data['Timestamp'].dt.dayofweek

from pygam import LinearGAM, s
model = LinearGAM(s(0) + s(1) + s(2) + s(3))
X_train = df[['hour', 'day_of_week', 'month', 'year']]
y_train = df['trips']
modelFit = model.fit(X_train, y_train)

X_test = df_test[['hour', 'day_of_week', 'month', 'year']]
pred = modelFit.predict(X_test)
df_test['trips'] = pred

print("Number of predictions:", len(pred))

df_test.head()
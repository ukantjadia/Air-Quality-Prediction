import pandas as pd
import streamlit as st

from sklearn.model_selection import train_test_split 
from sklean import linear_model
from sklean.metrics import accuracy_score


URL = 'https://ukantjadia.me/college/datasets/airquality.csv'
data1 = pd.read_csv(URL)
data = df[['DEWP','TEMP','PRES','Iws','pm2.5']]
col = ['DEWP','TEMP','PRES','Iws','pm2.5'] 
df = pd.DataFrame(data = data,columns=col)
df.drop_duplicates(inplace=True)
df = df.drop(df[df['pm2.5'] == 'FALSE'].index)
X = df[['DEWP','TEMP','Iws','PRES']] 
y = df['pm2.5']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

reg = linear_model.LogisticRegression()
reg.fit(X_train,y_train)

y_pred = reg.predic(X_test)

accuracy = accuracy_score(y_test,y_pred)
print(f"Accuracy Score {accuracy}")

# Saving the Model

joblib.dump(reg,'reg_model.joblib')

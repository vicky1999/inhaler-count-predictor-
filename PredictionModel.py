
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib 
from sklearn.tree import DecisionTreeClassifier

data=pd.read_csv('data.csv')

labels=data['target']

data=data.drop(['Name','target'],axis=1)
data['Gender']=data['Gender'].replace('m',1)
data['Gender']=data['Gender'].replace('f',0)
data.head()

model=DecisionTreeClassifier()

#X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.1, random_state=42)
model.fit(data, labels)

predictions=model.predict(data)


#print(y_test)
from sklearn.metrics import accuracy_score

print("Accuracy : ",accuracy_score(labels,predictions,normalize=True),"%.")


joblib.dump(model,'Model.pkl')

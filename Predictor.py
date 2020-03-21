#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  21 17:49:04 2020

@author: vignesh
"""

import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.externals import joblib
model=joblib.load('Model.pkl');

import os

from flask import Flask,request,render_template

app = Flask(__name__)

#model=pickle.load(open('model.pkl',rb))

@app.route('/',methods=['POST','GET'])
def hello():
    return render_template('index.html', prediction_Result="Value Missing")
    #return "Hello World!"
 
@app.route('/predictor',methods=['POST','GET'])
def predict():
    result=request.form
    #name=result['Name']
    age=result['age']
    gender=result['Gender']
    tempe=result['Temperature']
    air=result['air']
    if(tempe==''):
        tempe=0
    if(air==''):
        air=0.0
    l=[]
    #l.append(int(name))
    l.append(int(age))
    l.append(int(gender))
    l.append(int(tempe))
    l.append(float(air))
    print(l)
    li=np.array([l])
    pred=model.predict(li)
    return render_template('index.html',prediction_Result='You will take %d - %d times the Inhaler.'%(pred,pred+1))
    

if(__name__ == "__main__"):
    app.run()

from distutils.log import debug
from urllib import request
from flask import Flask, render_template, request
import pickle
import pandas as pd
import joblib


app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def form():    
    if request.method == 'POST' and 'age' in request.form and 'weight' in request.form:
        clf = joblib.load("myregr.pkl")
        age = int(request.form.get('age'))
        weight = int(request.form.get('weight'))
        x = pd.DataFrame([[age, weight]], columns=["Age", "Weight"])
        prediction = clf.predict(x)[0]
    
    return render_template('form.html', reqval = prediction)
    
    
from flask import Flask,request,render_template,app
import os  # for getting the path of current directory
from flask import Response
import numpy as np
import pandas as  pd
import pickle

app = Flask(__name__)

scaler = pickle.load(open('Model\ StandardScaler.pkl','rb'))
model=pickle.load(open("Model\ prediction_model.pkl","rb"))


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predictdata",methods=['GET','POST'])
def predict_datapoint():
    results = ""

    if request.method =='POST':

        Pregnancies = int(request.form.get("Pregnancies"))
        Glucose = float(request.form.get("Glucose"))
        BloodPressure = float(request.form.get("BloodPressure"))
        SkinThickness = float(request.form.get("SkinThickness"))
        Insulin = float(request.form.get("Insulin"))
        BMI = float(request.form.get("BMI"))
        DiabetesPedigreeFunction = float(request.form.get("DiabetesPedigreeFunction"))
        Age = int(request.form.get("Age"))

        

        new_data=scaler.transform([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        predict = model.predict(new_data)

        if predict[0] == 1:
            results = 'Diabetic'

        else:
            results = 'Non Diabetic'

        return render_template('single_prediction.html',result=results)

    else:
        return render_template('home.html')
    
if __name__=='__main__':
    app.run(host='0.0.0.0')


    
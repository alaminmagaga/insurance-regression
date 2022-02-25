import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

model= pickle.load(open('insurance_regression.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=["POST"])
def predict():

    age = request.form['age']
    age = int(age)
    #sex
    sex = request.form['sex']
    if sex == "male":
        sex = 1
    elif sex == "female":
        sex = 0
    #bmi
    bmi = request.form['bmi']
    bmi = int(bmi) 
    #children
    children = request.form['children']
    children = int(children)
    #smoker
    smoker = request.form['smoker']
    if smoker == "Yes":
        smoker = 1
    elif smoker == "No":
        smoker = 0
    region = request.form['region']
    region=int(region)   
    int_features = [age,sex,
                    bmi,
                    children,
                    smoker,
                    region]
    final_features = [int_features]
    prediction = model.predict(final_features).round(2)

	
    return render_template('result.html', prediction_text='The Patient Insurance Claim is ${}'.format(prediction[0]))



if __name__ == "__main__":
    app.run(debug=True)
    
    

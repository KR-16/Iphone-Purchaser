from logging import debug
from flask import Flask,render_template,request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)
model = pickle.load(open("Decision Tree Iphone Predictor.pkl","rb"))


@app.route(rule="/",methods = ["GET"])
def home():
    return render_template("main.html")

standard_to = LabelEncoder()

@app.route("/predict",methods = ["POST"])
def predict():
    if request.method == "POST":
        Gender = (request.form["Gender"])
        if Gender == "Male":
            Gender = 0
        else:
            Gender = 1
        Age = int(request.form["Age"])
        Salary = float(request.form["Salary"])

        # These features in the model
        prediction = model.predict([[Gender,Age,Salary]])

        if prediction == 0:
            return render_template("main.html",prediction_texts = "Not an Iphone purchaser")
        else:
            return render_template("main.html",prediction_texts = "Iphone purchaser")


if __name__ == "__main__":
    app.run(debug = True)

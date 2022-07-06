import flask
from flask import Flask, request
import flasgger
from flasgger import Swagger
import pickle
import pandas as pd

app = Flask(__name__)
Swagger(app)

pickle_in = open("breast_cancer.pkl", "rb")
model = pickle.load(pickle_in)

@app.route('/')
def home():
    return "AIDI 2004 mid-term test"

@app.route('/predict', methods = ["POST"])
def predict():
    """
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
    responses:
        200:
            description: The output values
    """
    test_df = pd.read_csv(request.files.get("file"))
    prediction = model.predict(test_df)
    pred_list = []
    for i in prediction:
        if i == 0:
            pred_list.append("B")
        else:
            pred_list.append("M")
    return "The predicted class for the test file is"+ str(list(pred_list))

if __name__ == "__main__":
    app.run(debug= True)
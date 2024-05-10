from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
app = Flask(__name__)
CORS(app)

with open("crop.pkl", "rb") as file:
    model = pickle.load(file)

with open("label_encoder.pkl", "rb") as encoder_file:
    label_encoder = pickle.load(encoder_file)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    nitrogen = int(data["nitrogen"])
    phosphorus = int(data["phosphorus"])
    potassium = int(data["potassium"])
    temperature = float(data["temperature"])
    humidity = float(data["humidity"])
    ph_value = float(data["ph"])
    rainfall = float(data["rainfall"])
    croptype = data["cropType"].capitalize()
    sowing_season = data["sowing_season"].capitalize()

    prediction = model.predict(
        [
            [
                nitrogen,
                phosphorus,
                potassium,
                temperature,
                humidity,
                ph_value,
                rainfall,
                croptype,
                sowing_season,
            ]
        ]
    )
    rounded_prediction = np.round(prediction).astype(int)
    print("prediction= "+ str(prediction))
    print(type(prediction))
    print(rounded_prediction)
    print(type(rounded_prediction))
    # Check if prediction is a single value or a list
    if isinstance(prediction, list):
        decoded_prediction = label_encoder.inverse_transform(rounded_prediction)
    else:
        decoded_prediction = label_encoder.inverse_transform([rounded_prediction])[0]
    return jsonify({"prediction": decoded_prediction})



if __name__ == "__main__":
    app.run(debug=True)

print("hey")

# Crop Recommendation System

## Overview

This repository contains a Crop Recommendation System developed using Flask and machine learning techniques. The system predicts the most suitable crop for cultivation based on input parameters such as soil nutrients, environmental factors, crop type, and sowing season.

## Features

- **Machine Learning Model:** Utilizes a Random Forest algorithm as the trained machine learning model to predict recommended crops.
- **User Interface:** Includes a simple UI for the system built with HTML and JavaScript in `index.html`.
- **RESTful API:** Implements a Flask API for easy interaction with the system.
- **Input Parameters:** Requires input parameters like nitrogen, phosphorus, potassium levels, temperature, humidity, pH value, and rainfall.
- **Cross-Origin Resource Sharing (CORS):** Enables cross-origin resource sharing using Flask-CORS.
- **Label Encoding:** Utilizes label encoding techniques for categorical data transformation.

## Usage

1. Clone the repository to your local machine.
2. Install the required dependencies listed in `requirements.txt`.
3. Run the Flask application using `python app.py`.
4. Open `index.html` in a web browser to access the user interface.
5. Enter input data and click the "Predict" button to receive crop recommendations.

## File Structure

- `app.py`: Contains the Flask application with endpoints for prediction.
- `crop.pkl`: Trained machine learning model (Random Forest) for crop recommendation.
- `label_encoder.pkl`: Saved label encoder for categorical data transformation.
- `index.html`: User interface HTML file for the application.
- `requirements.txt`: Dependencies required to run the application.

## Contribution

Contributions to enhance functionality, optimize code, or improve documentation are welcome. Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

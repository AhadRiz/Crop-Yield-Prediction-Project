from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('crop_yield_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        temp = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        rainfall = float(request.form['rainfall'])

        # Create a DataFrame for prediction
        input_data = pd.DataFrame([[temp, humidity, rainfall]], columns=['Temperature', 'Humidity', 'Rainfall'])

        # Load scaler and scale the input data
        scaler = joblib.load('scaler.pkl')
        input_data_scaled = scaler.transform(input_data)

        # Make prediction
        prediction = model.predict(input_data_scaled)

        return jsonify({'prediction': prediction[0]})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)

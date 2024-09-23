# Crop Yield Prediction

This project predicts crop yields based on weather data (temperature, humidity, rainfall) using a machine learning model.

## Project Structure

- `app.py`: Flask app to serve predictions via a web interface.
- `project.py`: Main script for data preprocessing, model building, and saving.
- `multan_data.csv`: Weather and crop yield data for Multan.
- `templates/index.html`: Frontend web interface for user input.
- `requirements.txt`: Dependencies required for the project.

## How to Run

1. Install the required dependencies
2. Run the Flask app
3. Open your browser and go to `http://127.0.0.1:5000/` to access the web interface.

## Dependencies

- Flask
- Pandas
- Scikit-learn
- Joblib

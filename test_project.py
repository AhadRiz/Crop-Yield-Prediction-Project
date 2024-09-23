import unittest
import joblib
import pandas as pd

class TestCropYieldModel(unittest.TestCase):
    def setUp(self):
        # Load model and scaler
        self.model = joblib.load('crop_yield_model.pkl')
        self.scaler = joblib.load('scaler.pkl')

    def test_prediction(self):
        # Create a test input
        test_input = pd.DataFrame([[300.0, 50.0, 100.0]], columns=['Temperature', 'Humidity', 'Rainfall'])
        test_input_scaled = self.scaler.transform(test_input)

        # Predict yield
        prediction = self.model.predict(test_input_scaled)
        self.assertGreater(prediction[0], 0)

if __name__ == '__main__':
    unittest.main()

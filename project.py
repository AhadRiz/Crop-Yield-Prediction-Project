import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor  # Use a more complex model
from sklearn.metrics import mean_squared_error
import joblib

# Load data
data = pd.read_csv('multan_data.csv')

# Feature and target selection
features = ['Temperature', 'Humidity', 'Rainfall']
target = 'Crop_Yield'

# Normalize the features
scaler = MinMaxScaler()
data[features] = scaler.fit_transform(data[features])

# Split data into train and test sets
X = data[features]
y = data[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a more complex model (Random Forest)
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Save the model and scaler
joblib.dump(model, 'crop_yield_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("Model saved successfully as 'crop_yield_model.pkl'")

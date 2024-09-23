import csv
import requests
import random

# OpenWeatherMap API Key and URL
api_key = 'ddc4d7caca0f99bc56b1f04713c2ad54'
location = 'Multan,PK'
url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'

# Placeholder data for crop yield
crop_yield_data = {
    '2020': 2.5,  # example yield (tons/hectare)
    '2021': 2.7,
    '2022': 2.9,
    '2023': 3.0,
}

# Open the CSV file for writing
with open('multan_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Year', 'Temperature', 'Humidity', 'Rainfall', 'Crop_Yield'])

    for year, yield_value in crop_yield_data.items():
        response = requests.get(url)
        weather_data = response.json()

        # Add some variability to the temperature, humidity, and rainfall
        temp = weather_data['main']['temp'] + random.uniform(-3, 3)  # Variation of ±3K
        humidity = weather_data['main']['humidity'] + random.uniform(-10, 10)  # Variation of ±10%
        rainfall = random.uniform(30, 70)  # Random rainfall in mm/year

        writer.writerow([year, temp, humidity, rainfall, yield_value])

print("CSV file generated successfully.")

import requests
import pandas as pd

url = "https://archive-api.open-meteo.com/v1/era5"
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "start_date": "2021-01-01",
    "end_date": "2021-12-31",
    "hourly": "temperature_2m",
    "timezone": "auto"
}

response = requests.get(url, params=params)
response.raise_for_status()  

data = response.json()
time = data["hourly"]["time"]
temp = data["hourly"]["temperature_2m"]
df = pd.DataFrame({"time": time, "temperature_2m": temp})

# Save to CSV
df.to_csv("berlin_temperature_2021.csv", index=False)
print("Data saved to berlin_temperature_2021.csv")

import dataLoadVisualize as dlv
import pandas as pd
import matplotlib.pyplot as plt

def lowestTemperatureDate(df):
    min_temp = df['temperature_2m'].min()
    low_temp_dates = df[df['temperature_2m'] == min_temp]['time']
    return list(low_temp_dates)
def highestTemperatureDate(df):
    max_temp = df['temperature_2m'].max()
    high_temp_dates = df[df['temperature_2m'] == max_temp]['time']
    return list(high_temp_dates)
def exclusiveColdDays(df):
    cold_days = df[df['temperature_2m'] < 0]
    plt.figure(figsize=(10, 5))
    plt.plot(df['time'], df['temperature_2m'], label='Temperature (°C)', color='blue')
    plt.axhline(0, color='red', linestyle='--', label='Freezing Point (0°C)')
    plt.scatter(cold_days['time'], cold_days['temperature_2m'], color='orange', label='Cold Days', zorder=5)
    plt.title('Cold Days in Berlin')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    return list(cold_days['time'])
def dataLoadVisualize():
    try:
        df = dlv.load_data()
        # dlv.data_visualization(df)
        return df
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    df = dataLoadVisualize()
    low_dates = lowestTemperatureDate(df)
    high_dates = highestTemperatureDate(df)
    print("Dates with the highest temperature:", high_dates)
    print("Dates with the lowest temperature:", low_dates)
    cold_days = exclusiveColdDays(df)
    

import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data(file_path="berlin_temperature_2021.csv"):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    else:
        df = pd.read_csv(file_path)
        print(f"Data loaded from {file_path}")
        return df
def data_visualization(df):
    if df.empty:
        print("No data to visualize.")
    else:
        df['time'] = pd.to_datetime(df['time'])
        plt.figure(figsize=(12, 6))
        plt.plot(df['time'], df['temperature_2m'], label='Temperature (°C)', color='blue')
        plt.title('Hourly Temperature in Berlin (2021)')
        plt.xlabel('Time')
        plt.ylabel('Temperature (°C)')
        plt.xticks(rotation=45)
        plt.grid()
        plt.legend()
        plt.tight_layout()
        plt.show()
        df['time'] = df['time'].dt.date
        daily_avg = df.groupby('time')['temperature_2m'].mean().reset_index()
        plt.figure(figsize=(12, 6))
        plt.plot(daily_avg['time'], daily_avg['temperature_2m'], label='Daily Average Temperature (°C)', color='orange')
        plt.title('Daily Average Temperature in Berlin (2021)')
        plt.xlabel('Date')
        plt.ylabel('Average Temperature (°C)')
        plt.xticks(rotation=45)
        plt.grid()
        plt.legend()
        plt.tight_layout()
        plt.show()
        df['temperature_2m'].plot(kind='hist', bins=30, color='green', alpha=0.7)
        plt.title('Temperature Distribution in Berlin (2021)')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Frequency')
        plt.grid()
        plt.tight_layout()
        plt.show()
        df['temperature_2m'].plot(kind='box', vert=False, color='purple')
        plt.title('Temperature Box Plot in Berlin (2021)')
        plt.xlabel('Temperature (°C)')
        plt.grid()
        plt.tight_layout()
        plt.show()
        df['time'] = pd.to_datetime(df['time'])
        monthly_avg = df.resample('ME', on='time')['temperature_2m'].mean().reset_index()
        monthly_avg.rename(columns={'temperature_2m': 'monthly_avg'}, inplace=True)
        plt.figure(figsize=(12, 6))
        plt.plot(monthly_avg['time'], monthly_avg['monthly_avg'], label='Monthly Average Temperature (°C)', color='red')
        plt.title('Monthly Average Temperature in Berlin (2021)')
        plt.xlabel('Month')
        plt.ylabel('Average Temperature (°C)')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()
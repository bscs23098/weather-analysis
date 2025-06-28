# Weather Data Analysis Project

This project loads, analyzes, and visualizes weather data using Python. It identifies the dates with the highest and lowest temperatures, and visualizes cold days (below freezing) in Berlin.

## Features

- Load weather data from a CSV or other source
- Find dates with the highest and lowest temperatures
- Visualize cold days (temperature below 0°C)
- Simple, modular code structure

## Requirements

- Python 3.x
- pandas
- matplotlib

## Setup

1. Clone or download this repository.
2. Install dependencies (preferably in a virtual environment):

   ```powershell
   pip install pandas matplotlib
   ```

3. Make sure your data file is available and the `dataLoadVisualize.py` module is set up to load it.

## Usage

Run the main script:

```powershell
python main.py
```

This will:
- Load the weather data
- Print the dates with the highest and lowest temperatures
- Show a plot of cold days in Berlin

## File Structure

- `main.py` — Main script for analysis and visualization
- `dataLoadVisualize.py` — Module for loading and (optionally) visualizing data
- `dataCollect.py` — (Optional) For collecting data from an API

## Example Output

```
Dates with the highest temperature: ['2023-07-15']
Dates with the lowest temperature: ['2023-01-10']
```
A plot window will also appear showing cold days.

## Customization

- Change the city or data source by editing `dataLoadVisualize.py`.
- Adjust column names in `main.py` if your data uses different headers.

## License

MIT License

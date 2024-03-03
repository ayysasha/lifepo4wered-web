from flask import Flask, render_template, jsonify
import subprocess
from datetime import datetime, timedelta
from threading import Thread
import time
import json
import os


app = Flask(__name__)

battery_capacity_ah = 160
output_voltage = 5

data_history = {
    "vbat": [],
    "vin": [],
    "iout": [],
}

def get_lifepo4wered_data(variable):
    command = ['lifepo4wered-cli', 'get', variable]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        if result.stdout:
            return float(result.stdout.strip()) / 1000
    except Exception as e:
        print(f"Error getting {variable}: {e}")
    return None

def collect_data():
    while True:
        now = datetime.now()
        for key in data_history.keys():
            value = get_lifepo4wered_data(key)
            if value is not None:
                data_history[key].append((now.isoformat(), value))  # Store ISO format datetime

        if len(data_history['vbat']) > 43200:  # Keep last 43200 data points (24 hours at 2-second intervals)
            for key in data_history:
                data_history[key].pop(0)

        save_data_history()  # Save data history after each collection cycle

        time.sleep(5)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    # Serve the latest data point for real-time updates
    latest_data = {key: data_history[key][-1] if data_history[key] else (None, 0) for key in data_history}
    # Calculate additional metrics as needed
    watts = latest_data['iout'][1] * output_voltage
    battery_percentage = ((latest_data['vbat'][1] - 3.0) / (3.65 - 3.0)) * 100 if latest_data['vbat'][1] else 0
    battery_percentage = max(0, min(100, battery_percentage))
    time_remaining_hours = 'N/A'
    if latest_data['iout'][1] > 0:
        time_remaining_hours = battery_capacity_ah / latest_data['iout'][1]

    return jsonify({
        'latest': {
            'vbat': latest_data['vbat'][1],
            'vin': latest_data['vin'][1],
            'iout': latest_data['iout'][1],
            'watts': watts,
            'battery_percentage': battery_percentage,
            'time_remaining_hours': time_remaining_hours
        },
        'history': {
            'vbat': data_history['vbat'],
            'vin': data_history['vin'],
            'iout': data_history['iout']
        }
    })

def save_data_history():
    temp_file_path = 'data_history_temp.json'
    with open(temp_file_path, 'w') as file:
        json.dump(data_history, file, indent=4)
    
    # Check the size of the temp file
    if os.path.getsize(temp_file_path) > 1e9:  # 1GB in bytes
        # If the file size is too large, you can implement a mechanism to reduce the data
        # For example, remove oldest entries or split data into multiple files
        print("Data history size exceeds 1GB. Implement data reduction strategy.")
        # Example strategy: Keep only the latest N entries (simplistic approach)
        for key in data_history:
            data_history[key] = data_history[key][-100000:]  # Adjust N based on your needs
        
        # Save the reduced data
        with open('data_history.json', 'w') as file:
            json.dump(data_history, file, indent=4)
        os.remove(temp_file_path)  # Remove temporary file
    else:
        # If the temp file size is acceptable, replace the old file with the new one
        os.rename(temp_file_path, 'data_history.json')

def load_data_history():
    try:
        with open('data_history.json', 'r') as file:
            global data_history
            data_history = json.load(file)
    except FileNotFoundError:
        print("No existing data history found. Starting fresh.")

if __name__ == '__main__':
    load_data_history()  # Ensure this line is added to load data on startup
    data_collector = Thread(target=collect_data, daemon=True)
    data_collector.start()
    app.run(host='0.0.0.0', port=5000, debug=True)

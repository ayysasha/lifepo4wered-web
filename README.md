# Solar Powered Pi Monitor

![image](https://github.com/ayysasha/lifepo4wered-web/assets/19575937/23247b10-a990-451e-b706-59a30d89855c)


# Solar Power Monitoring System

This project is a web-based application designed to monitor and visualize solar power data. It allows users to view historical power generation data, understand performance trends, and make informed decisions about their solar power systems.

## Features

- **Data Visualization**: Interactive graphs to display solar power generation data over time.
- **Dark Mode**: A toggle for switching between light and dark mode for better visibility according to user preference.
- **Responsive Design**: The interface is fully responsive and adapts to different screen sizes for optimal viewing on any device.

## Installation

To set up the project locally, follow these instructions:

### Prerequisites

- Python 3.x installed on your machine.
- https://github.com/xorbit/LiFePO4wered-Pi Installed on your RPI
- Flask installed in your Python environment.
- A modern web browser.

### Getting Started

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   ```
2. **Navigate to the project directory**:
   ```bash
   cd solar-power-monitoring-system
   ```
3. **Install dependencies** (if any listed in `requirements.txt`):
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. To run the Flask server, execute:
   ```bash
   python app.py
   ```
2. Access the web interface by opening `http://localhost:5000` in your web browser.

### Configuration

- **Changing the Bound IP Address**:
  To modify the bound IP address of the Flask server, open `app.py` and locate the line `app.run(host='0.0.0.0', port=5000)`. Replace `'0.0.0.0'` with your desired IP address.

- **Modifying the Battery Capacity Variable**:
  In `app.py`, search for the `battery_capacity` variable and adjust its value according to your system's specifications. This value is in amp-hours.

## File Structure

- `app.py` - The Flask application script.
- `index.html` - The main HTML file for the web interface.
- `styles.css` - Contains styles for the web interface.
- `script.js` - JavaScript for interactive web elements.

## Contributing

We welcome contributions! If you have suggestions for improvements or bug fixes, please feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

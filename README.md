# Solar Powered Pi Monitor

![image](https://github.com/ayysasha/lifepo4wered-web/assets/19575937/23247b10-a990-451e-b706-59a30d89855c)


# Solar Power Monitoring System

This project is a web-based application designed to monitor and visualize solar power data from the Lifepo4wered hardware sold by silicognition (https://www.tindie.com/products/silicognition/lifepo4weredpi-2/). It allows users to view historical power generation data, understand performance trends, and make informed decisions about their solar power systems.

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

## Running Your Application as a Service on Raspberry Pi

To ensure your Python web application starts automatically on your Raspberry Pi's boot, follow these steps to configure it as a systemd service.

### Prerequisites

- Ensure you have the path to your application's directory.
- Know the username under which you want the service to run.

If you're unsure about the directory path or your username, you can use the `pwd` command in the terminal within your application's directory to get the path, and `whoami` to get your current username.

### Step 1: Create a systemd Service File

1. Open a terminal on your Raspberry Pi.
2. Create a new systemd service file using a text editor. Replace `<your_service_name>` with a meaningful name for your service:
   ```bash
   sudo nano /etc/systemd/system/<your_service_name>.service
   ```
3. Insert the following content, adjusting `User`, `WorkingDirectory`, and `ExecStart` with your specific details:
   ```ini
   [Unit]
   Description=Your App Description
   After=network.target

   [Service]
   User=<your_username>
   WorkingDirectory=<path_to_your_app>
   ExecStart=/usr/bin/python3 <your_app.py>
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```
   Replace `<your_username>`, `<path_to_your_app>`, and `<your_app.py>` with your actual username, application directory path, and Python script name, respectively.

4. Save and exit the editor (for nano, press `Ctrl+X`, followed by `Y`, then `Enter`).

### Step 2: Enable and Start Your Service

1. Reload the systemd configuration to recognize your new service:
   ```bash
   sudo systemctl daemon-reload
   ```
2. Enable your service to start at boot:
   ```bash
   sudo systemctl enable <your_service_name>.service
   ```
3. Start the service immediately to test:
   ```bash
   sudo systemctl start <your_service_name>.service
   ```
4. (Optional) Check the status of your service:
   ```bash
   sudo systemctl status <your_service_name>.service
   ```

### Step 3: Monitoring and Logs

- To view your application's logs:
  ```bash
  journalctl -u <your_service_name>.service
  ```
- To restart your service:
  ```bash
  sudo systemctl restart <your_service_name>.service
  ```
- To stop your service, if necessary:
  ```bash
  sudo systemctl stop <your_service_name>.service
  ```

## Contributing

We welcome contributions! If you have suggestions for improvements or bug fixes, please feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

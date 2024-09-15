# Serial Assistant

A Python-based serial port communication assistant with a graphical user interface.

## Features

- Connect to serial ports
- Read and display data from serial ports
- Send data to serial ports
- Configurable baud rate and port selection

## Installation

1. Clone the repository:
git clone https://github.com/yourusername/serial_assistant.git

2. Change to the project directory:
cd serial_assistant

3. Create a virtual environment and activate it:
python -m venv venv
venv\Scripts\activate  # On macOS/Linux use: source venv/bin/activate

4. Install the required packages:
pip install -r requirements.txt

## Usage

Run the application:
python src/main.py

## Running Tests

To run the unit tests:
bash scripts/run_tests.sh

## Building Documentation

To build the documentation:
cd docs
make html

The documentation will be available in the `docs/_build/html` directory.

## License

This project is licensed under the MIT License.
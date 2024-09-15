# src/core/serial_handler.py
import serial
from serial.tools import list_ports
from src.utils.helpers import cached_function

class SerialHandler:
    def __init__(self):
        self.serial = None

    def list_ports(self):
        return [port.device for port in list_ports.comports()]

    def connect(self, port, baud_rate):
        try:
            self.serial = serial.Serial(port, baud_rate, timeout=1)
            return True
        except serial.SerialException:
            return False

    def disconnect(self):
        if self.serial and self.serial.is_open:
            self.serial.close()

    def read_data(self):
        if self.serial and self.serial.is_open:
            return self.serial.readline().decode('utf-8').strip()
        return None

    def write_data(self, data):
        if self.serial and self.serial.is_open:
            self.serial.write(data.encode('utf-8'))

    @cached_function
    def list_ports(self):
        return [port.device for port in list_ports.comports()]
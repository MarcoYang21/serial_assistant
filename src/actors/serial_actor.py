# src/actors/serial_actor.py
import pykka
from src.core.serial_handler import SerialHandler
from src.core.state_machine import SerialStateMachine

class SerialActor(pykka.ThreadingActor):
    def __init__(self):
        super().__init__()
        self.serial_handler = SerialHandler()
        self.state_machine = SerialStateMachine()

    def connect(self, port, baud_rate):
        if self.serial_handler.connect(port, baud_rate):
            self.state_machine.connect()
            return True
        return False

    def disconnect(self):
        self.serial_handler.disconnect()
        self.state_machine.disconnect()

    def read_data(self):
        if self.state_machine.is_connected():
            self.state_machine.start_reading()
            data = self.serial_handler.read_data()
            self.state_machine.stop_reading()
            return data
        return None

    def write_data(self, data):
        if self.state_machine.is_connected():
            self.state_machine.start_writing()
            self.serial_handler.write_data(data)
            self.state_machine.stop_writing()

# src/core/state_machine.py
from transitions import Machine

class SerialStateMachine(object):
    states = ['disconnected', 'connected', 'reading', 'writing']

    def __init__(self):
        self.machine = Machine(model=self, states=SerialStateMachine.states, initial='disconnected')

        self.machine.add_transition('connect', 'disconnected', 'connected')
        self.machine.add_transition('disconnect', '*', 'disconnected')
        self.machine.add_transition('start_reading', 'connected', 'reading')
        self.machine.add_transition('stop_reading', 'reading', 'connected')
        self.machine.add_transition('start_writing', 'connected', 'writing')
        self.machine.add_transition('stop_writing', 'writing', 'connected')

    def on_enter_connected(self):
        print("Connected to serial port")

    def on_exit_connected(self):
        print("Disconnected from serial port")

    def on_enter_reading(self):
        print("Started reading from serial port")

    def on_enter_writing(self):
        print("Started writing to serial port")

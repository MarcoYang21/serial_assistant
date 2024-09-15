# tests/test_state_machine.py
import unittest
from src.core.state_machine import SerialStateMachine

class TestSerialStateMachine(unittest.TestCase):
    def setUp(self):
        self.state_machine = SerialStateMachine()

    def test_initial_state(self):
        self.assertEqual(self.state_machine.state, 'disconnected')

    def test_connect_transition(self):
        self.state_machine.connect()
        self.assertEqual(self.state_machine.state, 'connected')

    def test_disconnect_transition(self):
        self.state_machine.connect()
        self.state_machine.disconnect()
        self.assertEqual(self.state_machine.state, 'disconnected')

    def test_start_reading_transition(self):
        self.state_machine.connect()
        self.state_machine.start_reading()
        self.assertEqual(self.state_machine.state, 'reading')

if __name__ == '__main__':
    unittest.main()

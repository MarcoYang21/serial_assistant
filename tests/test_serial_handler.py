# tests/test_serial_handler.py
import unittest
from unittest.mock import patch, MagicMock
from src.core.serial_handler import SerialHandler

class TestSerialHandler(unittest.TestCase):
    def setUp(self):
        self.serial_handler = SerialHandler()

    @patch('src.core.serial_handler.list_ports')
    def test_list_ports(self, mock_list_ports):
        mock_list_ports.comports.return_value = [
            MagicMock(device='COM1'),
            MagicMock(device='COM2')
        ]
        ports = self.serial_handler.list_ports()
        self.assertEqual(ports, ['COM1', 'COM2'])

    @patch('src.core.serial_handler.serial.Serial')
    def test_connect(self, mock_serial):
        result = self.serial_handler.connect('COM1', 9600)
        self.assertTrue(result)
        mock_serial.assert_called_once_with('COM1', 9600, timeout=1)

    @patch('src.core.serial_handler.serial.Serial')
    def test_disconnect(self, mock_serial):
        self.serial_handler.serial = MagicMock()
        self.serial_handler.disconnect()
        self.serial_handler.serial.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()

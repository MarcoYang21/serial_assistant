# tests/test_data_processor.py
import unittest
from src.core.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.data_processor = DataProcessor()

    def test_process_data(self):
        processed_data = []
        self.data_processor.get_observable().subscribe(
            on_next=lambda x: processed_data.append(x)
        )

        self.data_processor.process_data("test")
        self.data_processor.process_data("DATA")
        self.data_processor.process_data("")

        self.assertEqual(processed_data, ["TEST", "DATA"])

if __name__ == '__main__':
    unittest.main()

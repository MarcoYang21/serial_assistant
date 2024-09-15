# src/gui/widgets/serial_config.py
from PySide6.QtWidgets import QWidget, QFormLayout, QComboBox, QPushButton
from ...core.serial_handler import SerialHandler

class SerialConfigWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QFormLayout(self)

        self.port_combo = QComboBox()
        self.baud_combo = QComboBox()
        self.connect_button = QPushButton("Connect")

        layout.addRow("Port:", self.port_combo)
        layout.addRow("Baud Rate:", self.baud_combo)
        layout.addWidget(self.connect_button)

        self.populate_combos()

    def populate_combos(self):
        serial_handler = SerialHandler()
        self.port_combo.addItems(serial_handler.list_ports())
        self.baud_combo.addItems(['9600', '19200', '38400', '57600', '115200'])

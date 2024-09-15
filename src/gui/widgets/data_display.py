# src/gui/widgets/data_display.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton

class DataDisplayWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.data_display = QTextEdit()
        self.data_display.setReadOnly(True)
        
        self.clear_button = QPushButton("Clear")

        layout.addWidget(self.data_display)
        layout.addWidget(self.clear_button)

        self.clear_button.clicked.connect(self.clear_display)

    def update_data(self, data):
        self.data_display.append(data)

    def clear_display(self):
        self.data_display.clear()

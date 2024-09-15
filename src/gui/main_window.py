from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer
from .widgets.serial_config import SerialConfigWidget
from .widgets.data_display import DataDisplayWidget
from ..actors.serial_actor import SerialActor
from ..actors.gui_actor import GuiActor
from ..core.data_processor import DataProcessor
from .gui_signals import gui_signals

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Serial Assistant")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        
        self.serial_config = SerialConfigWidget()
        self.data_display = DataDisplayWidget()

        layout.addWidget(self.serial_config)
        layout.addWidget(self.data_display)

        self.serial_actor = SerialActor.start().proxy()
        self.gui_actor = GuiActor.start().proxy()
        self.data_processor = DataProcessor()

        self.serial_config.connect_button.clicked.connect(self.toggle_connection)
        
        # 连接 gui_signals 的信号
        gui_signals.update_data_signal.connect(self.data_display.update_data)

        self.read_timer = QTimer(self)
        self.read_timer.timeout.connect(self.read_serial_data)

    def toggle_connection(self):
        if self.serial_config.connect_button.text() == "Connect":
            port = self.serial_config.port_combo.currentText()
            baud_rate = int(self.serial_config.baud_combo.currentText())
            if self.serial_actor.connect(port, baud_rate).get():
                self.serial_config.connect_button.setText("Disconnect")
                self.read_timer.start(100)  # Read every 100ms
        else:
            self.serial_actor.disconnect()
            self.serial_config.connect_button.setText("Connect")
            self.read_timer.stop()

    def read_serial_data(self):
        data = self.serial_actor.read_data().get()
        if data:
            processed_data = self.data_processor.process_data(data)
            self.gui_actor.tell({'command': 'update_data', 'data': processed_data})

    def closeEvent(self, event):
        self.gui_actor.stop()
        self.serial_actor.stop()
        super().closeEvent(event)

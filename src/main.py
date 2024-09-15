# src/main.py
import sys
from PySide6.QtWidgets import QApplication
from .gui.main_window import MainWindow  # 使用相對導入

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
from PySide6.QtCore import QObject, Signal

class GuiSignals(QObject):
    update_data_signal = Signal(object)

gui_signals = GuiSignals()

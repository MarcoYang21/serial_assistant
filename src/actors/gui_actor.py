import pykka
from ..gui.gui_signals import gui_signals

class GuiActor(pykka.ThreadingActor):
    def on_receive(self, message):
        if message.get('command') == 'update_data':
            gui_signals.update_data_signal.emit(message['data'])

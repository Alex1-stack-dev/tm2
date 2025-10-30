from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit
from controllers.g2_controller import G2Controller
from controllers.colorado_controller import ColoradoController
from utils.logger import log_error
from PyQt6.QtCore import QThread, pyqtSignal

class TimingThread(QThread):
    status_update = pyqtSignal(str)
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
    def run(self):
        try:
            result = self.controller.start_race()
            self.status_update.emit("\n".join(result) if isinstance(result, list) else str(result))
        except Exception as e:
            self.status_update.emit(f"Error: {e}")
            log_error(e)

class TimingTab(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = G2Controller() # Set from settings
        self.layout = QVBoxLayout()
        self.status = QTextEdit()
        self.status.setReadOnly(True)
        self.start_btn = QPushButton("Start Race")
        self.start_btn.clicked.connect(self.start_race)
        self.layout.addWidget(QLabel("Timing Control"))
        self.layout.addWidget(self.start_btn)
        self.layout.addWidget(self.status)
        self.setLayout(self.layout)
    def start_race(self):
        self.thread = TimingThread(self.controller)
        self.thread.status_update.connect(self.status.append)
        self.thread.start()

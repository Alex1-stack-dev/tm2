from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import time

class HardwareWorker(QThread):
    resultReady = pyqtSignal(str)
    error = pyqtSignal(str)

    def run(self):
        try:
            time.sleep(2)  # Simulate device I/O
            self.resultReady.emit("Device responded with OK.")
        except Exception as e:
            self.error.emit(str(e))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Threaded UX Example")
        layout = QVBoxLayout()
        self.button = QPushButton("Start Device Job")
        self.button.clicked.connect(self.start_job)
        self.status = QLabel()
        layout.addWidget(self.button)
        layout.addWidget(self.status)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def start_job(self):
        self.button.setDisabled(True)
        self.status.setText("Working...")
        self.worker = HardwareWorker()
        self.worker.resultReady.connect(self.on_result)
        self.worker.error.connect(self.on_error)
        self.worker.start()

    def on_result(self, text):
        self.status.setText(text)
        self.button.setDisabled(False)

    def on_error(self, text):
        self.status.setText("Error: " + text)
        self.button.setDisabled(False)

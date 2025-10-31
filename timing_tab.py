from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QProgressBar, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QThread, pyqtSignal

FONT_FAMILY = "Arial Rounded MT Bold, Arial, Helvetica, sans-serif"

class TimingWorker(QThread):
    status = pyqtSignal(str)
    done = pyqtSignal(list)
    def run(self):
        import time
        self.status.emit("Connecting to Timing Device...")
        time.sleep(2)  # Simulated operation
        self.status.emit("Retrieving data...")
        time.sleep(2)
        self.done.emit([["Athlete A", "25.41"]])

class TimingTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        layout = QVBoxLayout()
        self.status = QLabel("Idle. Click to sync timing.")
        self.status.setFont(QFont(FONT_FAMILY, 12))
        self.pb = QProgressBar()
        self.pb.setMaximum(0); self.pb.setMinimum(0)
        self.pb.hide()
        sync_btn = QPushButton("Sync Timing Device")
        sync_btn.setToolTip("Synchronize with external timing device and fetch results.")
        sync_btn.clicked.connect(self.sync_device)
        layout.addWidget(self.status)
        layout.addWidget(self.pb)
        layout.addWidget(sync_btn)
        layout.addStretch()
        self.setLayout(layout)
    def sync_device(self):
        self.pb.show()
        self.worker = TimingWorker()
        self.worker.status.connect(self.status.setText)
        self.worker.done.connect(self.sync_done)
        self.worker.start()
    def sync_done(self, results):
        self.pb.hide()
        QMessageBox.information(self, "Timing Complete", f"Timing device imported {len(results)} results.")
5. Help Tab Example (help_tab.py)
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QTextBrowser
from PyQt6.QtGui import QFont

FONT_FAMILY = "Arial Rounded MT Bold, Arial, Helvetica, sans-serif"

class HelpTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("Welcome to Swim Meet Manager! 🏊")
        label.setFont(QFont(FONT_FAMILY, 14))
        doc = QTextBrowser()
        doc.setPlainText(
            """
            Features:
            - Manage meet info, athletes, results and exports
            - Integrate with industry timing devices
            - Live results webserver
            - Save, edit, validate all meet details

            Tooltips are available on most fields.
            For support: support@example.com
            """
        )
        layout.addWidget(label)
        layout.addWidget(doc)
        self.setLayout(layout)

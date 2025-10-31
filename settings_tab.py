from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox, QPushButton, QFileDialog, QMessageBox, QLineEdit
from utils.logger import get_logger
import json

logger = get_logger(__name__)

class SettingsTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.log_box = QCheckBox("Enable detailed logging"); self.log_box.setChecked(True)
        self.log_box.setToolTip("Toggle verbose output/logging for debugging.")
        self.export_path_edit = QLineEdit(); self.export_path_edit.setToolTip("Default export directory.")
        self.save_btn = QPushButton("Save Settings"); self.save_btn.clicked.connect(self.save_settings)
        self.load_btn = QPushButton("Load Settings"); self.load_btn.clicked.connect(self.load_settings)

        layout.addWidget(QLabel("General Settings (persist to .json file):"))
        layout.addWidget(self.log_box)
        layout.addWidget(QLabel("Export path:"))
        layout.addWidget(self.export_path_edit)
        layout.addWidget(self.save_btn)
        layout.addWidget(self.load_btn)
        self.setLayout(layout)

    def save_settings(self):
        settings = {
            'logging': self.log_box.isChecked(),
            'export_path': self.export_path_edit.text(),
        }
        fname, _ = QFileDialog.getSaveFileName(self, 'Settings file', filter='JSON files (*.json)')
        if fname:
            with open(fname, 'w') as f:
                json.dump(settings, f, indent=4)
            logger.info(f"Settings saved: {fname}")
            QMessageBox.information(self, "Saved", f"Settings saved:
{fname}")

    def load_settings(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Settings file', filter='JSON files (*.json)')
        if fname:
            with open(fname, 'r') as f:
                s = json.load(f)
                self.log_box.setChecked(s.get('logging', True))
                self.export_path_edit.setText(s.get('export_path', ''))
            logger.info(f"Settings loaded: {fname}")
            QMessageBox.information(self, "Loaded", f"Settings loaded:
{fname}")

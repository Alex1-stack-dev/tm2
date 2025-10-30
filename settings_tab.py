from PyQt6.QtWidgets import QWidget, QVBoxLayout, QComboBox, QLabel

class SettingsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.timing_system = QComboBox()
        self.timing_system.addItems(["Time Machine G2", "Colorado Time Systems"])
        self.layout.addWidget(QLabel('Timing System:'))
        self.layout.addWidget(self.timing_system)
        self.setLayout(self.layout)

from PyQt6.QtWidgets import QMainWindow, QTabWidget
from timing_tab import TimingTab
from meet_tab import MeetTab
from results_tab import ResultsTab
from settings_tab import SettingsTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Swim Meet Manager")
        self.tabs = QTabWidget()
        self.tabs.addTab(TimingTab(), "Timing")
        self.tabs.addTab(MeetTab(), "Meet")
        self.tabs.addTab(ResultsTab(), "Results")
        self.tabs.addTab(SettingsTab(), "Settings")
        self.setCentralWidget(self.tabs)

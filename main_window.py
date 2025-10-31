import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QMessageBox
from PyQt6.QtCore import Qt
from meet_tab import MeetTab
from timing_tab import TimingTab
from results_tab import ResultsTab
from settings_tab import SettingsTab
from help_content import onboarding_dialog
from utils.logger import get_logger

logger = get_logger(__name__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Swim Meet Manager v2")
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Add each independently-coded, robust tab
        self.tab_meet = MeetTab(parent=self)
        self.tab_timing = TimingTab(parent=self)
        self.tab_results = ResultsTab(parent=self)
        self.tab_settings = SettingsTab(parent=self)
        self.tabs.addTab(self.tab_meet, "Meet Setup")
        self.tabs.addTab(self.tab_timing, "Timing Devices")
        self.tabs.addTab(self.tab_results, "Results/Export")
        self.tabs.addTab(self.tab_settings, "Settings & Tools")

        # Optional: On first start, show onboarding
        self.show_onboarding_if_needed()

        self.menu = self.menuBar().addMenu('Help')
        helpAction = self.menu.addAction('Onboarding/Help')
        helpAction.triggered.connect(lambda: onboarding_dialog(self))

    def show_onboarding_if_needed(self):
        # Logic for onboarding only on first start
        # ...
        onboarding_dialog(self)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Confirm Exit', "Are you sure you want to quit?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            logger.info("Application exited by user.")
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())

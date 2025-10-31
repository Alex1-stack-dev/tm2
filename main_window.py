from PyQt6.QtWidgets import QMainWindow, QTabWidget, QMessageBox, QAction, QMenu
from meet_tab import MeetTab
from timing_tab import TimingTab
from results_tab import ResultsTab
from settings_tab import SettingsTab
from help_tab import HelpTab
from PyQt6.QtGui import QFont, QKeySequence
from PyQt6.QtCore import Qt

def themed_palette():
    from PyQt6.QtGui import QPalette, QColor
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor("#F0F7FA"))
    palette.setColor(QPalette.ColorRole.Base, QColor("#FFFFFF"))
    palette.setColor(QPalette.ColorRole.Highlight, QColor("#0097A7"))
    palette.setColor(QPalette.ColorRole.WindowText, QColor("#082032"))
    return palette

FONT_FAMILY = "Arial Rounded MT Bold, Arial, Helvetica, sans-serif"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Swim Meet Manager Professional")
        self.setGeometry(100, 50, 1200, 800)
        self.setPalette(themed_palette())
        self.setFont(QFont(FONT_FAMILY, 11))
        self.tabs = QTabWidget()
        self.tabs.addTab(MeetTab(), "🏊 Meet Info")
        self.tabs.addTab(TimingTab(), "⏲ Devices & Sync")
        self.tabs.addTab(ResultsTab(), "🏅 Results & Export")
        self.tabs.addTab(SettingsTab(), "⚙️ Settings")
        self.tabs.addTab(HelpTab(), "❓ Help & Onboarding")
        self.setCentralWidget(self.tabs)
        self.create_menus()
        self.tabs.setCurrentIndex(0)
    def create_menus(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("&File")
        help_menu = menubar.addMenu("&Help")
        exit_action = QAction("E&xit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        about_action = QAction("&About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    def show_about(self):
        QMessageBox.information(self, "About", "Swim Meet Manager\nContact: support@example.com")
    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, 'Exit', "Quit the Swim Meet Manager?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

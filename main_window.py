from PyQt6.QtWidgets import (
    QMainWindow, QMessageBox, QLineEdit, QPushButton, QVBoxLayout,
    QWidget, QLabel, QToolTip, QDialog, QTextEdit
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

class HelpDialog(QDialog):
    def __init__(self, help_text, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Help & Onboarding")
        layout = QVBoxLayout()
        text = QTextEdit()
        text.setReadOnly(True)
        text.setText(help_text)
        layout.addWidget(text)
        self.setLayout(layout)
        self.setMinimumSize(400, 300)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Swim Meet Manager")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.event_name = QLineEdit()
        self.event_name.setPlaceholderText("Enter event name...")
        self.event_name.setToolTip("Type the event name here, e.g., '100m Freestyle'")
        layout.addWidget(QLabel("Event Name:"))
        layout.addWidget(self.event_name)

        self.add_button = QPushButton("Add Event")
        self.add_button.setToolTip("Add the event to the meet (cannot be blank or duplicate)")
        self.add_button.clicked.connect(self.add_event)
        layout.addWidget(self.add_button)

        self.help_button = QPushButton("Help / Onboarding")
        self.help_button.clicked.connect(self.show_help)
        layout.addWidget(self.help_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_event(self):
        name = self.event_name.text().strip()
        if not name:
            self.show_error("Event name cannot be blank.")
            return
        # For duplicates, check actual event data model here
        # if name in existing_events: ...
        self.show_status(f"Event '{name}' added.", success=True)
        self.event_name.clear()

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText(message)
        msg.setWindowTitle("Input Error")
        msg.show()
        msg.exec()

    def show_status(self, message, success=False):
        if success:
            self.statusBar().showMessage(message, 3000)  # Green or happy icon as style add-on
        else:
            self.statusBar().showMessage(message, 3000)

    def show_help(self):
        help_text = (
            "Welcome to Swim Meet Manager!\n\n"
            "- Fill in the event form, then click 'Add Event'.\n"
            "- Tooltips provide extra information for each field/button.\n"
            "- Errors are shown for missing or duplicate data.\n"
            "- Retry options will appear if hardware/export fails.\n"
            "- Use the Help button for onboarding at any time."
        )
        dlg = HelpDialog(help_text, self)
        dlg.exec()

# For icons/colors, set icons with QPushButton.setIcon(QIcon('...')) and use style sheets for success/error colors.

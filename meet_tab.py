from PyQt6.QtWidgets import (
    QWidget, QFormLayout, QLineEdit, QPushButton, QLabel, QMessageBox
)
from PyQt6.QtGui import QFont

FONT_FAMILY = "Arial Rounded MT Bold, Arial, Helvetica, sans-serif"

class MeetTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        layout = QFormLayout()
        self.name = QLineEdit(); self.name.setPlaceholderText("e.g. District Championship"); self.name.setToolTip("Required. Enter the full meet name.")
        self.date = QLineEdit(); self.date.setPlaceholderText("2025-11-01"); self.date.setToolTip("Required. Format: YYYY-MM-DD.")
        self.venue = QLineEdit(); self.venue.setPlaceholderText("e.g. Aquatic Center"); self.venue.setToolTip("Pool or location where meet is held.")
        self.director = QLineEdit(); self.director.setPlaceholderText("Director's full name"); self.director.setToolTip("Meet director or main contact.")
        for widget in [self.name, self.date, self.venue, self.director]:
            widget.setFont(QFont(FONT_FAMILY, 12))
        save_btn = QPushButton("Save Meet Info")
        save_btn.setFont(QFont(FONT_FAMILY, 12))
        save_btn.setToolTip("Save all meet information and validate required fields.")
        save_btn.clicked.connect(self.save)
        self.setTabOrder(self.name, self.date)
        self.setTabOrder(self.date, self.venue)
        self.setTabOrder(self.venue, self.director)
        self.setTabOrder(self.director, save_btn)
        layout.addRow("Meet Name *", self.name)
        layout.addRow("Date *", self.date)
        layout.addRow("Venue", self.venue)
        layout.addRow("Director", self.director)
        layout.addRow(save_btn)
        self.setLayout(layout)
    def save(self):
        name, date = self.name.text().strip(), self.date.text().strip()
        if not name:
            QMessageBox.warning(self, "Input Error", "Meet name is required.")
            self.name.setFocus()
            return
        if not date or not self.validate_date(date):
            QMessageBox.warning(self, "Input Error", "Valid date (YYYY-MM-DD) is required.")
            self.date.setFocus()
            return
        QMessageBox.information(self, "Info Saved", f"Meet info saved!\nName: {name}\nDate: {date}")
    def validate_date(self, date_str):
        from datetime import datetime
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

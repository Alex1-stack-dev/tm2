from PyQt6.QtWidgets import (
    QWidget, QFormLayout, QLineEdit, QPushButton, QLabel
)
from PyQt6.QtGui import QFont, QPalette, QColor
from PyQt6.QtCore import Qt

FONT_FAMILY = "Arial Rounded MT Bold, Arial, Helvetica, sans-serif"

class FieldValidator:
    def __init__(self, field: QLineEdit, warning: QLabel, rule, error_msg):
        self.field = field
        self.warning = warning
        self.rule = rule
        self.error_msg = error_msg
    def validate(self):
        valid = self.rule(self.field.text())
        self.warning.setVisible(not valid)
        if not valid:
            self.warning.setText(self.error_msg)
        return valid

class MeetTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        layout = QFormLayout()
        # Fields and warnings
        self.name = QLineEdit()
        self.name.setPlaceholderText("e.g. District Championship")
        self.name.setFont(QFont(FONT_FAMILY, 12))
        self.warn_name = QLabel()
        self.warn_name.setStyleSheet("color: red;")
        self.warn_name.hide()

        self.date = QLineEdit()
        self.date.setPlaceholderText("YYYY-MM-DD")
        self.date.setFont(QFont(FONT_FAMILY, 12))
        self.warn_date = QLabel()
        self.warn_date.setStyleSheet("color: red;")
        self.warn_date.hide()

        self.venue = QLineEdit(); self.venue.setPlaceholderText("e.g. Aquatic Center")
        self.venue.setFont(QFont(FONT_FAMILY, 12))
        self.director = QLineEdit(); self.director.setPlaceholderText("Director name")
        self.director.setFont(QFont(FONT_FAMILY, 12))
        self.save_btn = QPushButton("Save Meet Info")
        self.save_btn.clicked.connect(self.save)
        # Central validation
        self.validators = [
            FieldValidator(self.name, self.warn_name, lambda v: bool(v.strip()), "Meet name is required."),
            FieldValidator(self.date, self.warn_date, self.validate_date, "Date must be YYYY-MM-DD."),
        ]
        layout.addRow("Meet Name *", self.name)
        layout.addRow("", self.warn_name)
        layout.addRow("Date *", self.date)
        layout.addRow("", self.warn_date)
        layout.addRow("Venue", self.venue)
        layout.addRow("Director", self.director)
        layout.addRow(self.save_btn)
        self.setLayout(layout)
        # Instant validation on change
        self.name.textChanged.connect(self.validate_fields)
        self.date.textChanged.connect(self.validate_fields)
    def validate_fields(self):
        # Validate all, show errors inline
        valid_all = True
        for val in self.validators:
            valid = val.validate()
            valid_all = valid_all and valid
        return valid_all
    def validate_date(self, v):
        from datetime import datetime
        try:
            datetime.strptime(v, "%Y-%m-%d")
            return True
        except Exception:
            return False
    def save(self):
        if not self.validate_fields():
            return  # Errors are displayed inline
        # Proceed with actual save logic
        print("Saved: ", self.name.text(), self.date.text(), self.venue.text(), self.director.text())


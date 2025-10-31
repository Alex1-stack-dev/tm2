from PyQt6.QtWidgets import (
    QWidget, QFormLayout, QLineEdit, QPushButton, QMessageBox, QMenu, QAction
)
from PyQt6.QtGui import QFont, QKeySequence
from PyQt6.QtCore import Qt
class MeetTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setup_shortcuts()
    def init_ui(self):
        layout = QFormLayout()
        self.name = QLineEdit(); self.name.setPlaceholderText("e.g. District Championship")
        self.date = QLineEdit(); self.date.setPlaceholderText("YYYY-MM-DD")
        self.venue = QLineEdit(); self.venue.setPlaceholderText("e.g. Aquatic Center")
        self.director = QLineEdit(); self.director.setPlaceholderText("Director name")
        for widget in [self.name, self.date, self.venue, self.director]:
            widget.setFont(QFont("Arial Rounded MT Bold", 12))
            widget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
            widget.customContextMenuRequested.connect(self.show_context_menu)
        self.save_btn = QPushButton("Save Meet Info")
        self.save_btn.clicked.connect(self.save)
        layout.addRow("Meet Name *", self.name)
        layout.addRow("Date *", self.date)
        layout.addRow("Venue", self.venue)
        layout.addRow("Director", self.director)
        layout.addRow(self.save_btn)
        # Keyboard tab order
        self.setTabOrder(self.name, self.date)
        self.setTabOrder(self.date, self.venue)
        self.setTabOrder(self.venue, self.director)
        self.setTabOrder(self.director, self.save_btn)
        self.setLayout(layout)
    def setup_shortcuts(self):
        # Ctrl+S saves
        save_action = QAction(self)
        save_action.setShortcut(QKeySequence.Save)
        save_action.triggered.connect(self.save)
        self.addAction(save_action)
        # F1 opens help
        help_action = QAction(self)
        help_action.setShortcut(QKeySequence("F1"))
        help_action.triggered.connect(lambda: self.window().parent().tabs.setCurrentIndex(4)) # Assumes Help tab is index 4
        self.addAction(help_action)
    def show_context_menu(self, point):
        menu = QMenu(self)
        copy_action = menu.addAction("Copy")
        paste_action = menu.addAction("Paste")
        clear_action = menu.addAction("Clear Field")
        act = menu.exec(self.sender().mapToGlobal(point))
        if act == copy_action:
            self.sender().copy()
        elif act == paste_action:
            self.sender().paste()
        elif act == clear_action:
            self.sender().clear()
    def save(self):
        # Your save logic here
        if not self.name.text().strip():
            QMessageBox.warning(self, "Missing info", "Meet name is required.")
            return
        QMessageBox.information(self, "Saved", "Meet info saved.")

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTableWidget, QFileDialog
from models.models import import_athletes_from_csv, get_all_athletes

class MeetTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.import_btn = QPushButton("Import CSV")
        self.import_btn.clicked.connect(self.import_csv)
        self.athlete_table = QTableWidget()
        self.layout.addWidget(self.import_btn)
        self.layout.addWidget(self.athlete_table)
        self.setLayout(self.layout)
    def import_csv(self):
        fname, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv)")
        if fname:
            import_athletes_from_csv(fname)
            self.refresh_table()
    def refresh_table(self):
        data = get_all_athletes()
        # Fill QTableWidget with data

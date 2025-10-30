from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog
from reports.generator import generate_pdf_report, export_csv
from scoring import update_scores

class ResultsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.export_pdf_btn = QPushButton("Export PDF Results")
        self.export_csv_btn = QPushButton("Export CSV Results")
        self.export_pdf_btn.clicked.connect(self.export_pdf)
        self.export_csv_btn.clicked.connect(self.export_csv)
        self.status = QTextEdit()
        self.layout.addWidget(self.export_pdf_btn)
        self.layout.addWidget(self.export_csv_btn)
        self.layout.addWidget(self.status)
        self.setLayout(self.layout)
    def export_pdf(self):
        fname, _ = QFileDialog.getSaveFileName(self, "Save PDF", "results.pdf", "PDF Files (*.pdf)")
        if fname:
            generate_pdf_report(fname)
            self.status.append(f"Exported PDF results to {fname}")
    def export_csv(self):
        fname, _ = QFileDialog.getSaveFileName(self, "Save CSV", "results.csv", "CSV Files (*.csv)")
        if fname:
            export_csv(fname)
            self.status.append(f"Exported CSV results to {fname}")

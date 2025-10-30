from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextBrowser, QPushButton, QLabel, QComboBox
from reports.generator import generate_report

class ResultsTab(QWidget):
    def __init__(self, meet_manager, heats, error_signal):
        super().__init__()
        self.meet_manager = meet_manager
        self.heats = heats
        self.error_signal = error_signal
        layout = QVBoxLayout()
        self.dropdown = QComboBox()
        self.populate_meets()
        self.report_view = QTextBrowser()
        self.error_label = QLabel()
        generate_btn = QPushButton("Show Report")
        generate_btn.clicked.connect(self.show_report)
        layout.addWidget(QLabel("Choose meet for report:"))
        layout.addWidget(self.dropdown)
        layout.addWidget(generate_btn)
        layout.addWidget(self.report_view)
        layout.addWidget(self.error_label)
        self.setLayout(layout)
    def populate_meets(self):
        self.dropdown.clear()
        meets = self.meet_manager.get_meets()
        for m in meets:
            self.dropdown.addItem(f"{m.name} — {m.date.strftime('%Y-%m-%d %H:%M')}", m)
    def show_report(self):
        try:
            idx = self.dropdown.currentIndex()
            meet = self.dropdown.itemData(idx)
            if not meet:
                raise ValueError("No meet selected")
            # For demonstration, show report for all session heats
            html = generate_report(meet, self.heats)
            self.report_view.setHtml(html)
        except Exception as e:
            self.error_label.setText(f"<span style='color:red'>{e}</span>")
            self.error_signal.emit(str(e))

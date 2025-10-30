from fpdf import FPDF
from typing import List
from models import Event, Result
import datetime

class MeetPDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 16)
        self.cell(0, 10, "Swim Meet Results", border=False, ln=1, align="C")
        self.set_font("Arial", '', 10)
        self.cell(0, 10, f"Date: {datetime.date.today().isoformat()}", border=False, ln=1, align="C")
        self.ln(5)

    def event_title(self, event: Event):
        self.set_font("Arial", 'B', 14)
        self.cell(0, 8, f"Event {event.number}: {event.name}", ln=1)
        self.ln(1)

    def results_table(self, results: List[Result]):
        self.set_font("Arial", 'B', 11)
        headings = ["Place", "Name", "Team", "Heat", "Seed", "Result", "DQ", "Splits", "Points"]
        widths = [12, 40, 24, 11, 16, 22, 12, 31, 15]
        for i, heading in enumerate(headings):
            self.cell(widths[i], 8, heading, 1, 0, 'C')
        self.ln()
        self.set_font("Arial", '', 10)
        for res in results:
            data = [
                str(res.place or '-'),
                res.athlete.name,
                res.athlete.team,
                str(res.heat),
                str(res.seed or '-'),
                str(res.result or 'NT'),
                res.dq_code or '',
                ';'.join(res.splits) if res.splits else '',
                str(res.points) if res.points is not None else ''
            ]
            for i, value in enumerate(data):
                self.cell(widths[i], 7, value, 1, 0, 'C')
            self.ln()
        self.ln(2)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')


def export_meet_to_pdf(events: List[Event], filepath: str):
    pdf = MeetPDF()
    pdf.add_page()
    for event in events:
        pdf.event_title(event)
        pdf.results_table(event.results)
    pdf.output(filepath)

# Usage example:
# events = [...]  # List[Event] with result data populated
# export_meet_to_pdf(events, 'meet_results.pdf')

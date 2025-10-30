from fpdf import FPDF
from models.models import get_all_athletes
def export_pdf(fname):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Meet Results')
    pdf.ln(20)
    for athlete in get_all_athletes():
        pdf.cell(0, 10, f"{athlete.name} - {athlete.team}", ln=True)
    pdf.output(fname)

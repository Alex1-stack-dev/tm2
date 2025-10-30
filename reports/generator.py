from exporters.csv_exporter import export_csv
from exporters.pdf_exporter import export_pdf
from exporters.hytek_exporter import export_hytek

def generate_pdf_report(fname):
    export_pdf(fname)
def export_csv(fname):
    export_csv(fname)
def export_hytek(fname):
    export_hytek(fname)

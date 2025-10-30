import csv
from models.models import get_all_athletes
def export_csv(fname):
    with open(fname, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Team'])
        for athlete in get_all_athletes():
            writer.writerow([athlete.name, athlete.team])

import csv
from typing import List
from models import Event, Result

def export_meet_to_csv(events: List[Event], filepath: str):
    headers = [
        "event_number", "event_name", "heat", "athlete", "team",
        "seed", "result", "place", "dq_code", "points", "splits"
    ]
    with open(filepath, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for event in events:
            for res in event.results:
                writer.writerow([
                    event.number,
                    event.name,
                    res.heat,
                    res.athlete.name,
                    res.athlete.team,
                    res.seed or '',
                    res.result or 'NT',
                    res.place or '',
                    res.dq_code or '',
                    res.points if res.points is not None else '',
                    ';'.join(res.splits) if res.splits else ''
                ])

# Usage example:
# events = [...]  # List[Event] with result data populated
# export_meet_to_csv(events, 'meet_results.csv')

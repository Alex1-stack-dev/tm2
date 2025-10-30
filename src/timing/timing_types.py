from dataclasses import dataclass
from typing import Optional, List
import datetime

@dataclass
class TimingEvent:
    event_id: int
    timestamp: datetime.datetime
    status: str  # e.g., 'started', 'stopped'
    lap: Optional[int] = None
    participant_id: Optional[int] = None
    notes: Optional[str] = None

@dataclass
class RaceResult:
    participant_id: int
    finish_time: datetime.timedelta
    place: Optional[int] = None

@dataclass
class Race:
    race_id: int
    name: str
    events: List[TimingEvent]
    results: List[RaceResult]

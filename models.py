from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Athlete:
    id: int
    name: str
    team: str
    dob: Optional[str] = None

@dataclass
class Result:
    athlete: Athlete
    event_number: int
    event_name: str
    heat: int
    seed: Optional[str]
    result: Optional[str]
    place: Optional[int]
    dq_code: Optional[str]
    splits: List[str] = field(default_factory=list)
    points: Optional[float] = None

@dataclass
class Event:
    number: int
    name: str
    entries: List[Athlete]
    results: List[Result] = field(default_factory=list)

from dataclasses import dataclass

@dataclass
class Command:
    command: str
    start: int
    end: int

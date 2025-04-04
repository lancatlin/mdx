from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Expression(ABC):
    start: int
    end: int

    @abstractmethod
    def execute(self) -> str:
        pass

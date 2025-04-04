from dataclasses import dataclass
from .expression import Expression

@dataclass
class Command(Expression):
    command: str

    def execute(self) -> str:
        return f"```\n{self.command}\n```\n"
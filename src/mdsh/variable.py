from dataclasses import dataclass

from .expression import Expression
from .param import Parameter


@dataclass
class Variable(Expression):
    param: Parameter

    def execute(self, _: dict[str, str]) -> str:
        return f"{self.param.value}"

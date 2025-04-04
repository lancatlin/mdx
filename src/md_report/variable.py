from dataclasses import dataclass
from .param import Parameter
from .expression import Expression

@dataclass
class Variable(Expression):
    param: Parameter

    def execute(self, _: dict[str, str]) -> str:
        return f"{self.param.value}"

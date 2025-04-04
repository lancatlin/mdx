from dataclasses import dataclass
from .param import Parameter
from .expression import Expression

@dataclass
class Variable(Expression):
    param: Parameter

    def execute(self) -> str:
        return f"{self.param.value}"

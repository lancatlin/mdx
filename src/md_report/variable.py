from dataclasses import dataclass
from .param import Parameter

@dataclass
class Variable:
    param: Parameter
    start: int
    end: int

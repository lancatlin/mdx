from dataclasses import dataclass
from .frontmatter import FrontMatter
from .command import Command
from .variable import Variable

@dataclass
class Document:
    frontmatter: FrontMatter
    content: str
    commands: list[Command]
    variables: list[Variable]

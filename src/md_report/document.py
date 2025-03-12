from dataclasses import dataclass
from md_report.frontmatter import FrontMatter
from .command import Command

@dataclass
class Document:
    frontmatter: FrontMatter
    content: str
    commands: list[Command]

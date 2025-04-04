from dataclasses import dataclass
from .frontmatter import FrontMatter
from .command import Command
from .variable import Variable
from .expression import Expression

@dataclass
class Document:
    frontmatter: FrontMatter
    content: str
    commands: list[Command]
    variables: list[Variable]

    def _get_separates(self) -> list[Expression]:
        separates: list[Expression] = [*self.commands, *self.variables]
        sorted_arr = sorted(separates, key=lambda exp: exp.start)
        print(sorted_arr)
        return sorted_arr

    def execute(self) -> str:
        result = ""
        cursor = 0
        for exp in self._get_separates():
            print(f"cursor: {cursor} start: {exp.start}")
            result += self.content[cursor:exp.start]
            result += exp.execute()
            cursor = exp.end
        result += self.content[cursor:]
        return result
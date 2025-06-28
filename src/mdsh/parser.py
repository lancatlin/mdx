import re

from .command import Command
from .document import Document
from .frontmatter import FrontMatter
from .variable import Variable


class Parser:
    def __init__(self, data: str):
        self.data = data

    def parse(self) -> Document:
        (front_data, content) = self._split_data()
        self.frontmatter = FrontMatter.from_yaml(front_data)
        commands = self._parse_command(content)
        variables = self._parse_variables(content)
        return Document(self.frontmatter, content, commands, variables)

    def _split_data(self) -> tuple[str, str]:
        pattern = re.compile(r'^---\n(.*?)---\n+(.*?)$', re.DOTALL)
        match = pattern.search(self.data)
        if match is None:
            raise Exception("Frontmatter not found")
        return (match.group(1), match.group(2))

    @staticmethod
    def _parse_command(content: str) -> list[Command]:
        pattern = re.compile(r'\{\{(.*?)\}\}')
        commands = []
        for match in pattern.finditer(content):
            command = Command(match.start(0), match.end(0), match.group(1))
            commands.append(command)
        return commands

    def _parse_variables(self, content: str) -> list[Variable]:
        pattern = re.compile(r'(?<!\{)\{([^{}]*?)\}(?!\})')
        variables = []
        for match in pattern.finditer(content):
            name = match.group(1)
            param = self.frontmatter.params.get(name)
            if param is None:
                raise Exception(f'Undefined variable: {name}')
            variables.append(Variable(match.start(0), match.end(0), param))
        return variables

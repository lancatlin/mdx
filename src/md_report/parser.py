import re
from .frontmatter import FrontMatter
from .command import Command
from .variable import Variable
from .document import Document

class Parser:
    def __init__(self, data: str):
        self.data = data

    def parse(self) -> Document:
        (front_data, content) = self._split_data()
        self.frontmatter = FrontMatter.from_yaml(front_data)
        commands = self._parseCommand(content)
        variables = self._parseVariables(content)
        return Document(self.frontmatter, content, commands, variables)

    def _split_data(self) -> tuple[str, str]:
        pattern = re.compile(r'^---\n(.*?)---\n+(.*?)$', re.DOTALL)
        match = pattern.search(self.data)
        if match == None:
            raise Exception("Frontmatter not found")
        return (match.group(1), match.group(2))

    @staticmethod
    def _parseCommand(content: str) -> list[Command]:
        pattern = re.compile(r'\{\{(.*?)\}\}')
        commands = []
        for match in pattern.finditer(content):
            command = Command(match.start(0), match.end(0), match.group(1))
            commands.append(command)
        return commands

    def _parseVariables(self, content: str) -> list[Variable]:
        pattern = re.compile(r'(?<!\{)\{([^{}]*?)\}(?!\})')
        variables = []
        for match in pattern.finditer(content):
            print(match.group(0))
            name = match.group(1)
            param = self.frontmatter.params.get(name)
            if param is None:
                raise Exception(f'Undefined variable: {name}')
            variables.append(Variable(match.start(0), match.end(0), param))
        return variables

import re
from md_report.frontmatter import FrontMatter
from .command import Command
from .document import Document

class Parser:
    def __init__(self, data: str):
        self.data = data

    def parse(self) -> Document:
        (front_data, content) = self._split_data()
        frontmatter = FrontMatter.from_yaml(front_data)
        commands = self._parseCommand()
        return Document(frontmatter, content, commands)

    def _split_data(self) -> tuple[str, str]:
        pattern = re.compile(r'^---\n(.*?)---\n+(.*?)$', re.DOTALL)
        match = pattern.search(self.data)
        if match == None:
            raise Exception("Frontmatter not found")
        return (match.group(1), match.group(2))

    def _parseCommand(self) -> list[Command]:
        command_pattern = re.compile(r'\{\{(.*?)\}\}')
        commands = []
        for match in command_pattern.finditer(self.data):
            command = Command(match.group(1), match.start(0), match.end(0))
            commands.append(command)
        return commands

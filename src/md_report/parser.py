import re
from dataclasses import dataclass
from md_report.frontmatter import FrontMatter
from .command import Command

@dataclass
class Parser:
    frontmatter: FrontMatter
    content: str
    commands: list[Command]

    @classmethod
    def from_content(cls, data_input: str) -> 'Parser':
        pattern = re.compile(r'^---\n(.*?)---\n+(.*?)$', re.DOTALL)
        match = pattern.search(data_input)
        if match == None:
            raise Exception("Frontmatter not found")
        frontmatter = FrontMatter.from_yaml(match.group(1))
        content = match.group(2)
        return cls(frontmatter, content, Parser.parseCommand(content))

    @staticmethod
    def parseCommand(content: str) -> list[Command]:
        command_pattern = re.compile(r'\{\{(.*?)\}\}')
        commands = []
        for match in command_pattern.finditer(content):
            command = Command(match.group(1), match.start(0), match.end(0))
            commands.append(command)
        return commands

import argparse
import string
from dataclasses import dataclass

from .command import Command
from .expression import Expression
from .frontmatter import FrontMatter
from .variable import Variable


@dataclass
class Document:
    frontmatter: FrontMatter
    content: str
    commands: list[Command]
    variables: list[Variable]
    env: dict[str, str] | None = None

    def _get_expressions(self) -> list[Expression]:
        separates: list[Expression] = [*self.commands, *self.variables]
        sorted_arr = sorted(separates, key=lambda exp: exp.start)
        return sorted_arr

    def execute(self) -> str:
        result = ""
        cursor = 0
        if self.env is None:
            raise Exception('Environment is not defined')

        for exp in self._get_expressions():
            result += self.content[cursor:exp.start]
            result += exp.execute(self.env)
            cursor = exp.end
        result += self.content[cursor:]
        return result

    def parse_arg(self, filename: str, args: list[str]) -> None:
        parser = argparse.ArgumentParser(
            prog=f"mdsh {filename}",
            description="Executing Markdown Template",
        )
        for _, param in self.frontmatter.params.items():
            parser.add_argument(
                f'--{param.name}',
                required=param.required,
                default=param.default
            )
        argv = vars(parser.parse_args(args))
        for _, param in self.frontmatter.params.items():
            value = argv[param.name]
            param.set(value)
        self.env = argv

    def get_filename(self) -> str:
        if self.env is None:
            return self.frontmatter.name
        filename = string.Template(self.frontmatter.name).substitute(self.env)
        return filename

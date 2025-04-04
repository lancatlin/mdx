import argparse
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
    env: dict[str, str] | None = None

    def _get_expressions(self) -> list[Expression]:
        separates: list[Expression] = [*self.commands, *self.variables]
        sorted_arr = sorted(separates, key=lambda exp: exp.start)
        print(sorted_arr)
        return sorted_arr

    def execute(self) -> str:
        result = ""
        cursor = 0
        if self.env is None:
            raise Exception('Environment is not defined')

        for exp in self._get_expressions():
            print(f"cursor: {cursor} start: {exp.start}")
            result += self.content[cursor:exp.start]
            result += exp.execute(self.env)
            cursor = exp.end
        result += self.content[cursor:]
        return result

    def parse_arg(self, args: list[str]) -> None:
        parser = argparse.ArgumentParser(
            prog="mdx",
            description="Executing Markdown Template",
        )
        for _, param in self.frontmatter.params.items():
            print(param)
            parser.add_argument(
                f'--{param.name}', 
                required=param.required, 
                default=param.default
            )
        argv = vars(parser.parse_args(args))
        print(argv)
        for _, param in self.frontmatter.params.items():
            value = argv[param.name]
            param.set(value)
        self.env = argv
        
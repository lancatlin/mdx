import string
import subprocess
from dataclasses import dataclass

from .expression import Expression


@dataclass
class Command(Expression):
    command: str

    def execute(self, argv: dict[str, str]) -> str:
        env = {
            **argv,
            'LANG': 'C.UTF-8',  # Set UTF-8 encoding
            'LC_ALL': 'C.UTF-8'
        }
        command = self._substitute(env)
        print(command)
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                env=env,
                check=True,
                encoding='utf-8'
            )
            output = str(result.stdout)
            return f"```\n{output}\n```\n"
        except subprocess.CalledProcessError as e:
            return f"> Failed to execute command '{command}':\n> {e.stderr}"

    def _substitute(self, env: dict[str, str]) -> str:
        template = string.Template(self.command)
        try:
            return template.substitute(env)
        except KeyError as e:
            raise Exception(f'Undefined variable: {e} in command "{self.command}"') \
            from e

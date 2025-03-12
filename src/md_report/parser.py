import re
from dataclasses import dataclass
from md_report.frontmatter import FrontMatter

@dataclass
class Parser:
    frontmatter: FrontMatter
    content: str

    @classmethod
    def parse(cls, data_input: str) -> 'Parser':
        pattern = re.compile(r'^---\n(.*?)---\n+(.*?)$', re.DOTALL)
        match = pattern.search(data_input)
        if match == None:
            raise Exception("Frontmatter not found")
        frontmatter = FrontMatter.from_yaml(match.group(1))
        content = match.group(2)
        return cls(frontmatter, content)

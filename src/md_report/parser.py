import re
import yaml
from io import StringIO
from md_report.frontmatter import FrontMatter

class Parser:
    def __init__(self, content: str):
        self.content = content
        self.frontmatter = self.parseFrontMatter()
    
    def parseFrontMatter(self) -> FrontMatter | None:
        pattern = re.compile(r'---\n(.*?)---\n', re.DOTALL)
        match = pattern.search(self.content)
        if match == None:
            return None
        data: str = match.group(1)
        print(data)
        frontmatter = FrontMatter.from_yaml(data)
        print(frontmatter)
        return None

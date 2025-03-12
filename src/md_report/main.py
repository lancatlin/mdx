from .parser import Parser

def main() -> None:
    filename = "ledger.md"
    with open(filename, 'r') as file:
        content = file.read()
        parser = Parser(content)
        doc = parser.parse()
        print(doc)

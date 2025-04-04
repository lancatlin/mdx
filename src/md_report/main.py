from .parser import Parser

def main() -> None:
    filename = "ledger.md"
    with open(filename, 'r') as file:
        content = file.read()
        parser = Parser(content)
        doc = parser.parse()
        doc.parse_arg(['--from', '2024-01-01', '--to', '2024-12-31'])
        print(doc.execute())

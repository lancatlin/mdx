from .parser import Parser

def main() -> None:
    filename = "ledger.md"
    with open(filename, 'r') as rfile:
        content = rfile.read()

    parser = Parser(content)
    doc = parser.parse()
    doc.parse_arg(['--from', '2024-01-01', '--to', '2024-12-31'])
    output = doc.execute()
    with open(doc.get_filename(), "w") as wfile:
        wfile.write(output)

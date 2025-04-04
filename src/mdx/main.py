from .parser import Parser
import sys

def main() -> None:
    filename = "ledger.md"
    with open(filename, 'r') as rfile:
        content = rfile.read()

    parser = Parser(content)
    doc = parser.parse()
    doc.parse_arg(sys.argv[1:])
    output = doc.execute()
    with open(doc.get_filename(), "w") as wfile:
        wfile.write(output)

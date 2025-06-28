from .parser import Parser
import sys

def main() -> None:
    if len(sys.argv) < 2:
        print("markdown template file is required")
        print("mdsh [markdown template]")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, 'r') as rfile:
        content = rfile.read()

    parser = Parser(content)
    doc = parser.parse()
    doc.parse_arg(filename, sys.argv[2:])
    output = doc.execute()
    with open(doc.get_filename(), "w") as wfile:
        wfile.write(output)

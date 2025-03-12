from md_report.parser import Parser

def main() -> None:
    filename = "ledger.md"
    with open(filename, 'r') as file:
        content = file.read()
        parser = Parser(content)
        parser.parseFrontMatter()

if __name__ == '__main__':
    main()

from md_report.parser import Parser

def main() -> None:
    filename = "ledger.md"
    with open(filename, 'r') as file:
        content = file.read()
        parser = Parser.from_content(content)
        print(parser)

if __name__ == '__main__':
    main()

import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
          description="A dead simple file reader in CLI"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    read_parser = subparsers.add_parser("read", help="Read a text file")
    read_parser.add_argument("filename")

    args = parser.parse_args()

    if args.command == "read":
        file = Path(args.filename)
        
        if file.suffix.lower() != ".txt":
                    parser.error("Error: Only text files are supported for now")
        
        if not file.exists():
            parser.error(f"Error: The File '{args.filename}' does not exist")
            return
        try:   
            content = file.read_text(encoding="utf-8")

            print(content, end="")
        except OSError as e:
            parser.error(f"Cannot read file: {e}")

if __name__ == "__main__":
    main()
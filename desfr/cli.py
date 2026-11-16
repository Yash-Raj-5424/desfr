import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("command")
    parser.add_argument("filename")

    args = parser.parse_args()

    if args.command == "read":
        file = Path(args.filename)
        
        if file.suffix.lower() != ".txt":
                    print("Error: Only text files are supported for now")
                    return
        
        if not file.exists():
            print(f"Error: The File '{args.filename}' does not exist")
            return
            
        content = file.read_text(encoding="utf-8")
        print(content)
    else:
        print(f"Unknown command: '{args.command}'")
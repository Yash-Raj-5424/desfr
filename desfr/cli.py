import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("command")
    parser.add_argument("filename")

    args = parser.parse_args()

    if args.command == "read":
        file = Path(args.filename)
        content = file.read_text(encoding="utf-8")
        print(content)
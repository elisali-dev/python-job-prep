import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--input",
                     type = Path,
                     required=True)
args = parser.parse_args()

print(args)
print(args.input)
print(type(args.input))
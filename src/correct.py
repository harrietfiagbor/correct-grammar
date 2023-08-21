import argparse
from spellchecker import SpellChecker

parser = arparse.ArgumentParser()
parser.add_argument("--file-path", default='./sample-docs/text-1.txt', type=pathlib.Path )
parser.add_argument("--lang", default="en")
args = parser.parse_args()

with open(args.file_path, 'r') as file:
    input_text = file.read()

print(f"Unformatted text {}".format(input_text))

if args.lang == "detect":
    lang = detect(text=input_text, low_memory=False)['lang']
    print(f"Detected language, {lang}")

check_spelling = SpellChecker(language=lang)



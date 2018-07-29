# Markdown Parser

A markdown parser written in Python 3.

## Usage:
```sh
python3 parser.py source
    
    source : A path to the Markdown source file, e.g. /path/to/source.md
```
The output is an HTML file generated from Markdown. If the input is "source.md", it writes to "source_output.html", overwriting existing file if one exists.

## Currently parses:
1. Headings
2. Bold
3. Italics

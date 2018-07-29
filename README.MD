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
4. Links
5. Images
6. GitHub extensions (coming soon)

## Screenshots
![Mockito README](https://i.gyazo.com/e3b862236ef99601ea88944d474d8f0c.png)
After image support was added (still gets confused by the GitHube extension syntax)
![Mockito README with image](https://i.gyazo.com/883fba1b2a84baf3b6e805b0e1309d59.png)

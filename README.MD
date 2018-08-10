# Markdown Parser

A markdown parser written in Python 3.

## Usage
```sh
python3 parser.py source
    
    source : A path to the Markdown source file, e.g. /path/to/source.md
```

## Notes
The output is an HTML file generated from Markdown. If the input is "source.md", it writes to "source_output.html", overwriting if a file with that absolute file path exists.

The regular expression matching for links and images is *greedy* (will be made *lazy* in the future), so it consumes as much text as possible, combining multiple links into one.

## Currently parses
1. Headings
2. Bold
3. Italics
4. Links
5. Images

## Planned features
1. GitHub extensions (coming soon)

## Screenshots
![Link support](https://i.gyazo.com/e3b862236ef99601ea88944d474d8f0c.png)
After image support was added (it gets confused by the syntax of the GitHub extensions to Markdown).
![Link + Image support](https://i.gyazo.com/883fba1b2a84baf3b6e805b0e1309d59.png)

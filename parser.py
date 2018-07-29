import sys
import re

def getParagraphs(input):
    return input.split("\n\n")


def processParagraph(p):
    p = processHeading(p)
    p = processBold(p)
    p = processItalics(p)
    return p


def processHeading(p):
    countHeadingLevel = calcHeadingLevel(p)

    if p.startswith("%") or p.startswith("#"):
        p = "<h{}>{}</h{}>".format(countHeadingLevel,
                                   p[countHeadingLevel + 1:], countHeadingLevel)
    
    return p


def processBold(p):
    for match in re.findall(r"\*\*.*\*\*", p):
        boldedText = "<b>{}</b>".format(match[1:-1])
        p = p.replace(match, boldedText)
    return p
    


def processItalics(p):
    for match in re.findall(r"\*.*\*", p):
        boldedText = "<i>{}</i>".format(match[1:-1])
        p = p.replace(match, boldedText)
    return p


def calcHeadingLevel(p):
    count = 0
    for char in p:
        if char != "%" and char != "#":
            break
        count += 1
    return count


def parse(input):
    paragraphs = getParagraphs(input)
    paragraphs = [processParagraph(paragraph) for paragraph in paragraphs]
    joined = "\n\n".join(paragraphs)
    output = "<html><body>{}</body></html>".format(joined)
    return output


if __name__ == "__main__":
    filename = sys.argv[1]
    outputFilename = "{}_output.html".format(filename.split(".")[0])
    with open(filename, "r") as input, open(outputFilename, "w") as output:
        parsed = parse(input.read())
        output.write(parsed)

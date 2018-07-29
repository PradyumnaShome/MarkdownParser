import sys
import re


def getParagraphs(input):
    return input.split("\n\n")


def processParagraph(p):
    p = processHeading(p)
    # Italics
    p = processLabel(p, "*", "i")
    # Bold
    p = processLabel(p, "**", "b")
    # Code
    p = processLabel(p, "`", "code")
    return p


def processHeading(p):
    countHeadingLevel = calcHeadingLevel(p)

    if p.startswith("%") or p.startswith("#"):
        p = "<h{}>{}</h{}>".format(countHeadingLevel,
                                   p[countHeadingLevel + 1:], countHeadingLevel)

    return p

def escapeIdentifier(identifier):
    escapeIdentifier = ""
    for char in identifier:
        escapeIdentifier += fr"\{char}"
    return escapeIdentifier

def shouldIdentifierBeEscaped(identifier):
    return identifier.startswith("*")

def processLabel(p, identifier, tagname):
    if shouldIdentifierBeEscaped(identifier):
        identifier = escapeIdentifier(identifier)
    regexp = fr"{identifier}.*{identifier}"
    for match in re.findall(regexp, p):
        print(f"Match: {match}")
        # Remove surrounding symbols
        textWithoutIdentifier = match[1:-1]
        parsedText = f"<{tagname}>{textWithoutIdentifier}</{tagname}>"
        print(parsedText)
        p = p.replace(match, parsedText)
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

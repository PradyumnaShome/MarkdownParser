import sys
import re


def getParagraphs(input):
    return input.split("\n\n")


def isHeading(p):
    return p.startswith("%") or p.startswith("#")


def processParagraph(p):
    if(isHeading(p)):
        p = processHeading(p)
    else:
        p = processPlaintext(p)
        # Bold
        p = processLabel(p, "**", "strong")
        # Italics
        p = processLabel(p, "*", "em")
        # Underlines
        p = processLabel(p, "_", "u")
        # Code
        p = processLabel(p, "`", "code")
        # Images
        p = processImages(p)
        # Links
        p = processLinks(p)
    return p


def processLinks(p):
    regexp = r"\[(?P<linkText>.*)\]\((?P<linkUrl>.*)\)"
    link = re.search(regexp, p)
    while link != None:
        linkUrl = link.group("linkUrl")
        linkText = link.group("linkText")

        parsedLink = f'<a href="{linkUrl}">{linkText}</a>'
        print(f"Link: {parsedLink}")
        p = p.replace(link[0], parsedLink)
        link = re.search(regexp, p)
    return p


def processImages(p):
    regexp = r"!\[(?P<imageText>.*)\]\((?P<imageUrl>.*)\)"
    image = re.search(regexp, p)
    while image != None:
        imageUrl = image.group("imageUrl")
        imageText = image.group("imageText")

        parsedImage = f'<img src="{imageUrl}" title="{imageText}"/>'
        print(f"Image: {parsedImage}")
        p = p.replace(image[0], parsedImage)
        image = re.search(regexp, p)
    return p


def processPlaintext(p):
    p = f"<p>{p}</p>"
    return p


def processHeading(p):
    countHeadingLevel = calcHeadingLevel(p)
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
        escapedIdentifier = escapeIdentifier(identifier)
        regexp = fr"{escapedIdentifier}.*{escapedIdentifier}"
    else:
        regexp = fr"{identifier}.*{identifier}"

    for match in re.findall(regexp, p):
        print(f"Match: {match}")
        # Remove surrounding symbols
        textWithoutIdentifier = match[len(
            identifier): len(match) - len(identifier)]
        parsedText = f"<{tagname}>{textWithoutIdentifier}</{tagname}>"
        print(f"{tagname}: {parsedText}")
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
    output = f"""<html>\n\t<body>\n\t{joined}\n\t</body>\n</html>"""
    return output


if __name__ == "__main__":
    filename = sys.argv[1]
    outputFilename = "{}_output.html".format(filename.split(".")[0])
    with open(filename, "r") as input, open(outputFilename, "w") as output:
        parsed = parse(input.read())
        output.write(parsed)

import codecs
import random
import string
import xml.etree.ElementTree as ElementTree

from bs4 import BeautifulSoup


def random_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=36))


# noinspection DuplicatedCode
def main():
    file = codecs.open("./input.txt", "r", "utf-8").readlines()
    file = [line.replace("\n", ".").replace("\r", "").replace("|", "") for line in file]

    separators = [[i for i, letter in enumerate(line) if letter == "." or letter == "?"] for line in file]

    tree = ElementTree.parse("html/empty.html")
    root = tree.getroot()

    root[0][1].text = file[0].replace("#", "")
    root[1][0][0][1].text = file[0].replace("#", "")

    for i, line in enumerate(file):
        if "!" in line:
            separator = ElementTree.SubElement(root[1][0][1], "hr")
            separator.set("id", random_id())

            subtitle = ElementTree.SubElement(root[1][0][1], "p")
            subtitle.set("id", random_id())
            subtitle.set("class", "")
            subtitle.text = line.replace("!", "")

        elif len(separators[i]) >= 2:
            toggle = ElementTree.SubElement(root[1][0][1], "ul")
            toggle.set("id", random_id())
            toggle.set("class", "toggle")

            li = ElementTree.SubElement(toggle, "li")
            details = ElementTree.SubElement(li, "details")
            details.set("open", "")

            summary = ElementTree.SubElement(details, "summary")
            summary.text = line[0:separators[i][0] + 1]

            answer = ElementTree.SubElement(details, "p")
            answer.set("id", random_id())
            answer.set("class", "")
            answer.text = line[separators[i][0] + 1:len(line)]

    file = codecs.open("{}.html".format(file[0].replace("#", "").replace(".", "")), "w+", "utf-8")
    file.write(
        BeautifulSoup(ElementTree.tostring(root, 'utf-8'), 'lxml').prettify())
    file.close()


if __name__ == '__main__':
    main()

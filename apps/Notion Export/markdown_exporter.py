import codecs

toggle = """<details>
<summary>{0}</summary>
<p>{1}</p>
</details>
"""

hr = """
---
"""

subtitle = "### {0} \n"


# noinspection DuplicatedCode
def main():
    file = codecs.open("./input.txt", "r", "utf-8").readlines()
    raw = [line.replace("\n", ".").replace("\r", "").replace("|", "") for line in file]
    separators = [[i for i, letter in enumerate(line) if letter == "." or letter == "?"] for line in raw]

    output = codecs.open("./{0}.md".format(raw[0].replace("#", "").replace(".", "")), "a+", "utf-8")

    for i, line in enumerate(raw):
        if "!" in line:
            output.write("\n{0}\n".format(hr))
            output.write(subtitle.format(line.replace("!", "")))

        elif len(separators[i]) >= 2:
            question = line[0:separators[i][0] + 1]
            answer = line[separators[i][0] + 1:len(line) - 1]

            if not answer.lower().islower():
                answer = ""

            output.write(toggle.format(question, answer))

    output.close()


if __name__ == '__main__':
    main()

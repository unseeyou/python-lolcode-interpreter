import re


def get_lexemes(lexeme_array, lines, line, index):
    if len(re.findall(".+OBTW", line)) != 0:
        lexeme_info = [line, "Invalid"]
        lexeme_array.append(lexeme_info)
        lines.remove(line)
        lines.insert(index, "")
        return
    elif len(re.findall(".+ TLDR.*", line)) != 0:
        comment = re.sub(" TLDR.*", "", line)
        lexeme_array.append([comment, "comment"])
        lexeme_array.append(["TLDR", "keyword"])

        remain = re.sub(".*TLDR", "", line).strip()
        if remain != "":
            lexeme_array.append([remain, "Invalid"])

        lines.remove(line)
        lines.insert(index, "")
        return
    elif len(re.findall("^TLDR .*", line)) != 0:
        lexeme_array.append(["TLDR", "keyword"])
        remain = re.sub("TLDR", "", line)
        if remain != "":
            lexeme_array.append([remain, "Invalid"])
        lines.remove(line)
        lines.insert(index, "")
        return

    if len(re.findall('^"[^"]*"', line)) != 0:
        exact = re.findall('"[^"]*"', line)[0]
        exact2 = re.sub('"', "", exact)

        lexeme_info2 = ['"', "String Delimiter"]
        lexeme_info = [exact2, "YARN Literal"]
        lexeme_array.append(lexeme_info2)
        lexeme_array.append(lexeme_info)
        lexeme_array.append(lexeme_info2)

        num_exact = len(exact)
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^WIN", line)) != 0:
        lexeme_info = ["WIN", "TROOF Literal"]
        lexeme_array.append(lexeme_info)

        num_exact = len("WIN")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^FAIL", line)) != 0:
        lexeme_info = ["FAIL", "TROOF Literal"]
        lexeme_array.append(lexeme_info)

        num_exact = len("FAIL")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^NUMBR", line)) != 0:
        lexeme_info = ["NUMBR", "TYPE Literal"]
        lexeme_array.append(lexeme_info)

        num_exact = len("NUMBR")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^NUMBAR", line)) != 0:
        lexeme_info = ["NUMBAR", "TYPE Literal"]
        lexeme_array.append(lexeme_info)

        num_exact = len("NUMBAR")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^YARN", line)) != 0:
        lexeme_info = ["YARN", "TYPE Literal"]
        lexeme_array.append(lexeme_info)

        num_exact = len("YARN")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^TROOF", line)) != 0:
        lexeme_info = ["TROOF", "TYPE Literal"]
        lexeme_array.append(lexeme_info)

        num_exact = len("TROOF")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^HAI", line)) != 0:
        lexeme_info = ["HAI", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("HAI")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^KTHXBYE", line)) != 0:
        lexeme_info = ["KTHXBYE", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("KTHXBYE")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^TLDR$", line)) != 0:
        lexeme_info = ["TLDR", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("TLDR")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, "")

    elif len(re.findall("^OBTW", line)) != 0:
        lexeme_info = ["OBTW", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("OBTW")
        new = line[num_exact : len(line)].strip()
        if new != "":
            lexeme_array.append([new, "comment"])
        lexeme_array.append(["<linebreak>", "linebreak"])

        index2 = index + 1
        while len(re.findall("(^TLDR )|( TLDR )|(^TLDR$)|(TLDR$)", lines[index2])) == 0:
            lexeme_array.append([lines[index2], "comment"])
            lines.remove(lines[index2])
            lines.insert(index2, "")
            lexeme_array.append(["<linebreak>", "linebreak"])
            index2 += 1

        # comment = new.strip() + "\n"

        # print(comment)
        lines.remove(line)
        lines.insert(index, "")

    elif len(re.findall("^I HAS A", line)) != 0:
        lexeme_info = ["I HAS A", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("I HAS A")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^ITZ", line)) != 0:
        lexeme_info = ["ITZ", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("ITZ")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^SUM OF", line)) != 0:
        lexeme_info = ["SUM OF", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("SUM OF")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^DIFF OF", line)) != 0:
        lexeme_info = ["DIFF OF", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("DIFF OF")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^PRODUKT OF", line)) != 0:
        lexeme_info = ["PRODUKT OF", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("PRODUKT OF")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^QUOSHUNT OF", line)) != 0:
        lexeme_info = ["QUOSHUNT OF", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("QUOSHUNT OF")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^MOD OF", line)) != 0:
        lexeme_info = ["MOD OF", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("MOD OF")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^BIGGR OF", line)) != 0:
        lexeme_info = ["BIGGR OF", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("BIGGR OF")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^SMALLR OF", line)) != 0:
        lexeme_info = ["SMALLR OF", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("SMALLR OF")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^BOTH OF", line)) != 0:
        lexeme_info = ["BOTH OF", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("BOTH OF")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^EITHER OF", line)) != 0:
        lexeme_info = ["EITHER OF", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("EITHER OF")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^WON OF", line)) != 0:
        lexeme_info = ["WON OF", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("WON OF")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^NOT", line)) != 0:
        lexeme_info = ["NOT", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("NOT")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^ANY OF", line)) != 0:
        lexeme_info = ["ANY OF", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("ANY OF")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^ALL OF", line)) != 0:
        lexeme_info = ["ALL OF", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("ALL OF")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^BOTH SAEM", line)) != 0:
        lexeme_info = ["BOTH SAEM", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("BOTH SAEM")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^DIFFRINT", line)) != 0:
        lexeme_info = ["DIFFRINT", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("DIFFRINT")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^SMOOSH", line)) != 0:
        lexeme_info = ["SMOOSH", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("SMOOSH")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^MAEK", line)) != 0:
        lexeme_info = ["MAEK", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("MAEK")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^IS NOW A", line)) != 0:
        lexeme_info = ["IS NOW A", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("IS NOW A")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^VISIBLE", line)) != 0:
        lexeme_info = ["VISIBLE", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("VISIBLE")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^GIMMEH", line)) != 0:
        lexeme_info = ["GIMMEH", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("GIMMEH")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^O RLY\?", line)) != 0:
        lexeme_info = ["O RLY?", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("O RLY?")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^MEBBE", line)) != 0:
        lexeme_info = ["MEBBE", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("MEBBE")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^YA RLY", line)) != 0:
        lexeme_info = ["YA RLY", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("YA RLY")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^NO WAI", line)) != 0:
        lexeme_info = ["NO WAI", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("NO WAI")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^OIC", line)) != 0:
        lexeme_info = ["OIC", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("OIC")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^WTF\?", line)) != 0:
        lexeme_info = ["WTF?", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("WTF?")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^OMGWTF", line)) != 0:
        lexeme_info = ["OMGWTF", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("OMGWTF")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^OMG", line)) != 0:
        lexeme_info = ["OMG", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("OMG")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^IM IN YR", line)) != 0:
        lexeme_info = ["IM IN YR", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("IM IN YR")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^UPPIN", line)) != 0:
        lexeme_info = ["UPPIN", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("UPPIN")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^NERFIN", line)) != 0:
        lexeme_info = ["NERFIN", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("NERFIN")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^MKAY", line)) != 0:
        lexeme_info = ["MKAY", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("MKAY")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^YR", line)) != 0:
        lexeme_info = ["YR", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("YR")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^TIL", line)) != 0:
        lexeme_info = ["TIL", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("TIL")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^WILE", line)) != 0:
        lexeme_info = ["WILE", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("WILE")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^IM OUTTA YR", line)) != 0:
        lexeme_info = ["IM OUTTA YR", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("IM OUTTA YR")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^AN", line)) != 0:
        lexeme_info = ["AN", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("AN")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^BTW", line)) != 0:
        lexeme_info = ["BTW", "keyword"]

        comment = re.sub(".*BTW ", "", line)
        lexeme_info2 = [comment, "comment"]

        lexeme_array.append(lexeme_info)
        lexeme_array.append(lexeme_info2)

        new = re.sub("BTW.*", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^A", line)) != 0:
        lexeme_info = ["A", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("A")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^R", line)) != 0:
        lexeme_info = ["R", "keyword"]
        lexeme_array.append(lexeme_info)

        num_exact = len("R")
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^[A-Za-z]+\w*", line)) != 0:
        exact = re.findall("[A-Za-z]+\w*", line)[0]
        lexeme_info = [exact, "Variable Identifier"]
        lexeme_array.append(lexeme_info)

        num_exact = len(exact)
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^-?\d+\.\d+", line)) != 0:
        exact = re.findall("-?\d+\.\d+", line)[0]
        lexeme_info = [exact, "NUMBAR Literal"]
        lexeme_array.append(lexeme_info)

        num_exact = len(exact)
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    elif len(re.findall("^-?\d+", line)) != 0:
        exact = re.findall("-?\d+", line)[0]
        lexeme_info = [exact, "NUMBR Literal"]
        lexeme_array.append(lexeme_info)

        num_exact = len(exact)
        new = line[num_exact : len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())

    else:
        lexeme_info = [line, "invalid"]

        lexeme_array.append(lexeme_info)

        lines.remove(line)
        lines.insert(index, "")


def lex_analyze(the_long_string):
    lexeme_arr = []  # empty

    # split every line of the string to an array
    lines = the_long_string.split("\n")

    # new string array for removed trailing lines and tabs
    lines2 = []
    for line in lines:
        if line != "":
            lines2.append(line.strip())

    for i in range(0, len(lines2)):
        while lines2[i] != "":
            get_lexemes(lexeme_arr, lines2, lines2[i], i)

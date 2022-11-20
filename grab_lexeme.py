import re

def get_lexemes(lexemeArr, lines, line, index):
    
    if(len(re.findall("^\"[^\"]*\"", line)) != 0):
        exact = re.findall("\"[^\"]*\"", line)[0]
        exact2 = re.sub("\"", "", exact)
        # print(exact2)

        lexeme_info2 = ["\"", "String Delimeter"]
        lexeme_info = []
        lexeme_info.append(exact2)
        lexeme_info.append("YARN Literal")
        lexemeArr.append(lexeme_info2)
        lexemeArr.append(lexeme_info)
        lexemeArr.append(lexeme_info2)
        
        new = re.sub(exact, "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
        
    elif(len(re.findall("^WIN", line)) != 0):
        lexeme_info = []
        lexeme_info.append("WIN")
        lexeme_info.append("TROOF Literal")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("WIN", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^FAIL", line)) != 0):
        lexeme_info = []
        lexeme_info.append("FAIL")
        lexeme_info.append("TROOF Literal")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("FAIL", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^NUMBR", line)) != 0):
        lexeme_info = []
        lexeme_info.append("NUMBR")
        lexeme_info.append("TYPE Literal")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("NUMBR", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^NUMBAR", line)) != 0):
        lexeme_info = []
        lexeme_info.append("NUMBAR")
        lexeme_info.append("TYPE Literal")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("NUMBAR", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^YARN", line)) != 0):
        lexeme_info = []
        lexeme_info.append("YARN")
        lexeme_info.append("TYPE Literal")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("YARN", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^TROOF", line)) != 0):
        lexeme_info = []
        lexeme_info.append("TROOF")
        lexeme_info.append("TYPE Literal")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("TROOF", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())

    elif(len(re.findall("^HAI", line)) != 0):
        lexeme_info = []
        lexeme_info.append("HAI")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("HAI", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^KTHXBYE", line)) != 0):
        lexeme_info = []
        lexeme_info.append("KTHXBYE")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("KTHXBYE", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^OBTW", line)) != 0):
        lexeme_info = []
        lexeme_info.append("OBTW")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("OBTW", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())

    elif(len(re.findall("^TLDR", line)) != 0):
        lexeme_info = []
        lexeme_info.append("TLDR")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("TLDR", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())

    elif(len(re.findall("^I HAS A", line)) != 0):
        lexeme_info = []
        lexeme_info.append("I HAS A")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("I HAS A", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^ITZ", line)) != 0):
        lexeme_info = []
        lexeme_info.append("ITZ")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("ITZ", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())


    
    elif(len(re.findall("^SUM OF", line)) != 0):
        lexeme_info = []
        lexeme_info.append("SUM OF")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("SUM OF", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^DIFF OF", line)) != 0):
        lexeme_info = []
        lexeme_info.append("DIFF OF")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("DIFF OF", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^PRODUKT OF", line)) != 0):
        lexeme_info = []
        lexeme_info.append("PRODUKT OF")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("PRODUKT OF", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^QUOSHUNT OF", line)) != 0):
        lexeme_info = []
        lexeme_info.append("QUOSHUNT OF")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("QUOSHUNT OF", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^MOD OF", line)) != 0):
        lexeme_info = []
        lexeme_info.append("MOD OF")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("MOD OF", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^BIGGR OF", line)) != 0):
        lexeme_info = []
        lexeme_info.append("BIGGR OF")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("BIGGR OF", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^SMALLR OF", line)) != 0):
        lexeme_info = []
        lexeme_info.append("SMALLR OF")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("SMALLR OF", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^BOTH OF", line)) != 0):
        lexeme_info = []
        lexeme_info.append("BOTH OF")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("BOTH OF", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^EITHER OF", line)) != 0):
        lexeme_info = []
        lexeme_info.append("EITHER OF")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("EITHER OF", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^WON OF", line)) != 0):
        lexeme_info = []
        lexeme_info.append("WON OF")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("WON OF", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^NOT", line)) != 0):
        lexeme_info = []
        lexeme_info.append("NOT")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("NOT", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^ANY OF", line)) != 0):
        lexeme_info = []
        lexeme_info.append("ANY OF")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("ANY OF", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^ALL OF", line)) != 0):
        lexeme_info = []
        lexeme_info.append("ALL OF")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("ALL OF", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^BOTH SAEM", line)) != 0):
        lexeme_info = []
        lexeme_info.append("BOTH SAEM")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("BOTH SAEM", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^DIFFRINT", line)) != 0):
        lexeme_info = []
        lexeme_info.append("DIFFRINT")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("DIFFRINT", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())

    elif(len(re.findall("^SMOOSH", line)) != 0):
        lexeme_info = []
        lexeme_info.append("SMOOSH")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("SMOOSH", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^MAEK", line)) != 0):
        lexeme_info = []
        lexeme_info.append("MAEK")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("MAEK", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    
    
    elif(len(re.findall("^IS NOW A", line)) != 0):
        lexeme_info = []
        lexeme_info.append("IS NOW A")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("IS NOW A", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^VISIBLE", line)) != 0):
        lexeme_info = []
        lexeme_info.append("VISIBLE")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("VISIBLE", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^GIMMEH", line)) != 0):
        lexeme_info = []
        lexeme_info.append("GIMMEH")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("GIMMEH", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^O RLY\?", line)) != 0):
        lexeme_info = []
        lexeme_info.append("O RLY?")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("O RLY\?", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())

    elif(len(re.findall("^MEBBE", line)) != 0):
        lexeme_info = []
        lexeme_info.append("MEBBE")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("MEBBE", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())

    elif(len(re.findall("^NO WAI", line)) != 0):
        lexeme_info = []
        lexeme_info.append("NO WAI")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("NO WAI", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())

    elif(len(re.findall("^OIC", line)) != 0):
        lexeme_info = []
        lexeme_info.append("OIC")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("OIC", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())

    elif(len(re.findall("^WTF\?", line)) != 0):
        lexeme_info = []
        lexeme_info.append("WTF?")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("WTF\?", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^OMG", line)) != 0):
        lexeme_info = []
        lexeme_info.append("OMG")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("OMG", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())

    elif(len(re.findall("^OMGWTF", line)) != 0):
        lexeme_info = []
        lexeme_info.append("OMGWTF")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("OMGWTF", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())

    elif(len(re.findall("^IM IN YR", line)) != 0):
        lexeme_info = []
        lexeme_info.append("IM IN YR")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("IM IN YR", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())

    elif(len(re.findall("^UPPIN", line)) != 0):
        lexeme_info = []
        lexeme_info.append("UPPIN")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("UPPIN", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())

    elif(len(re.findall("^NERFIN", line)) != 0):
        lexeme_info = []
        lexeme_info.append("NERFIN")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("NERFIN", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())

    elif(len(re.findall("^YR", line)) != 0):
        lexeme_info = []
        lexeme_info.append("YR")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("YR", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())

    elif(len(re.findall("^TIL", line)) != 0):
        lexeme_info = []
        lexeme_info.append("TIL")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("TIL", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())

    elif(len(re.findall("^WILE", line)) != 0):
        lexeme_info = []
        lexeme_info.append("WILE")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("WILE", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())

    elif(len(re.findall("^IM OUTTA YR", line)) != 0):
        lexeme_info = []
        lexeme_info.append("IM OUTTA YR")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("IM OUTTA YR", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())

    elif(len(re.findall("^AN", line)) != 0):
        lexeme_info = []
        lexeme_info.append("AN")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("AN", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())

    elif(len(re.findall("^BTW", line)) != 0):
        lexeme_info = []
        lexeme_info.append("BTW")
        lexeme_info.append("keyword")
    
        comment = re.sub(".*BTW ", "", line)
        lexeme_info2 = [comment, "comment"]
    
        lexemeArr.append(lexeme_info)
        lexemeArr.append(lexeme_info2)
    
        new = re.sub("BTW.*", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())
    
    elif(len(re.findall("^A", line)) != 0):
        lexeme_info = []
        lexeme_info.append("A")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("A", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())

    elif(len(re.findall("^R", line)) != 0):
        lexeme_info = []
        lexeme_info.append("R")
        lexeme_info.append("keyword")
        lexemeArr.append(lexeme_info)
        
        new = re.sub("R", "", line)
        lines.remove(line)
        lines.insert(index, new.strip())


    elif(len(re.findall("^[A-Za-z]+[\w]*", line)) != 0):
        exact = re.findall("[A-Za-z]+[\w]*", line)[0]
        lexeme_info = []
        lexeme_info.append(exact)
        lexeme_info.append("Variable Identifier")
        lexemeArr.append(lexeme_info)
        
        new = re.sub(exact, "", line)
        lines.remove(line)
        lines.insert(index, new.strip())

    elif(len(re.findall("^-?[\d]+\.[\d]+", line)) != 0):
        exact = re.findall("-?[\d]+\.[\d]+", line)[0]
        lexeme_info = []
        lexeme_info.append(exact)
        lexeme_info.append("NUMBAR Literal")
        lexemeArr.append(lexeme_info)
        

        num_exact = len(exact)
        new = line[num_exact:len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())



    elif(len(re.findall("^-?\d+", line)) != 0):
        exact = re.findall("-?\d+", line)[0]
        lexeme_info = []
        lexeme_info.append(exact)
        lexeme_info.append("NUMBR Literal")
        lexemeArr.append(lexeme_info)
        
        num_exact = len(exact)
        new = line[num_exact:len(line)]
        lines.remove(line)
        lines.insert(index, new.strip())


    else:
        lexeme_info = []
        lexeme_info.append(line)
        lexeme_info.append("invalid")

        lexemeArr.append(lexeme_info)

        lines.remove(line)
        lines.insert(index, "")
    
    
    

        



def lex_analyze(the_long_string):
    lexemeArr = [] #empty

    #split every line of the string to an array
    lines = the_long_string.split("\n")

    #new string array for removed trailing lines and tabs
    lines2 = []
    for line in lines:
        if(line != ""):
            lines2.append(line.strip())    


    for i in range(0, len(lines2)):
        while(lines2[i] != ''):
            get_lexemes(lexemeArr, lines2, lines2[i], i)
        
    
    # for i in lexemeArr:
    #     print(i)
    # print(lines2)

    







x = """BTW start of the program
O RLY?

HAI
    BTW variable dec
    I HAS A monde
    I HAS A num ITZ 17
    I HAS A name ITZ "seventeen"
    I HAS A fnum ITZ 17.0
    I HAS A flag ITZ WIN

    VISIBLE "declarations"
    VISIBLE MONDE BTW should be NOOB
    VISIBLE num
    VISIBLE name
    VISIBLE fnum
    VISIBLE flag

    I HAS A sum ITZ SUM OF num AN 13
    I HAS A diff ITZ DIFF OF sum AN 17
    I HAS A prod ITZ PRODUKT OF 3 AN 4
    I HAS A quo ITZ QUOSHUNT OF 4 AN 5

    VISIBLE sum
    VISIBLE diff
    VISIBLE prod
    VISIBLE quo
5.5
3.4
KTHXBYE"""
# lex_analyze(x)
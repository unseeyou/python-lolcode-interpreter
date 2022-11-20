import grab_lexeme

lexemeArr = []

def check_syntax(lexemeArr):
    testing_list = []

    for i in lexemeArr:
        testing_list.append(i)

    

    while(True):
        change = False
        index = 0

        # ---------------------------------------
        for i in testing_list:
            if(i[1] in ["NUMBR Literal", "NUMBAR Literal", "YARN Literal"]):
                del testing_list[index]
                testing_list.insert(index, "literal")
                change = True
            elif(i[1] == "Variable Identifier"):    
                del testing_list[index]
                testing_list.insert(index, "varident")
                change = True
            elif(i[0] in ["SUM OF"] and testing_list[index+1] == "literal" and testing_list[index+2][0] == "AN" and testing_list[index+3] == "literal"):
                del testing_list[index:(index+4)]
                testing_list.insert(index, "expr")
                change = True
            index += 1

        # ---------------------------------------

        if(len(testing_list)==1):
            print(True) # to be changed to return later
            break

        if(change == False):
            print(False) # to be changed to return later
            break
                

    for i in testing_list:
        print(i)





def lex_analyze(lexemeArr, the_long_string):
    lexemeArr.clear()

    lines = the_long_string.split("\n")

    lines2 = []
    for line in lines:
        if(line != ""):
            lines2.append(line.strip())    

    for i in range(0, len(lines2)):
        while(lines2[i] != ''):
            grab_lexeme.get_lexemes(lexemeArr, lines2, lines2[i], i)
    
    # for i in lexemeArr:
    #     print(i)

    check_syntax(lexemeArr)

x = """BTW start of the program
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
KTHXBYE"""


y = "I HAS A sum ITZ SUM OF num AN 13"
lex_analyze(lexemeArr, y)
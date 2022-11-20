import grab_lexeme

lexemeArr = []

def check_syntax(lexemeArr):
    testing_list = []

    for i in lexemeArr:
        testing_list.append(i)

    for i in testing_list:
        print(i)

    # while(len(testing_list) != 1)





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


y = "I HAS A sum ITZ SUM OF 5 AN 5"
lex_analyze(lexemeArr, y)
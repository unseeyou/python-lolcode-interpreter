import grab_lexeme

lexemeArr = []

def check_syntax(lexemeArr):
    testing_list = []

    for i in lexemeArr:
        # print(i)
        testing_list.append(i)

    # for i in testing_list:
    #     print(i)

    
    
    while(True):
        change = False
        index = 0
        
        # print("-----------------------------------------")
        # for i in testing_list:
        #     print(i)


        # ---------------------------------------
        for i in testing_list:
            #Literals
            if(i[1] in ["NUMBR Literal", "NUMBAR Literal", "YARN Literal", "TROOF Literal"]):
                del testing_list[index]
                testing_list.insert(index, "literal")
                change = True
            if(i[1] == "String Delimiter" and (index+2) < len(testing_list)):
                if(testing_list[index+1] == "literal" and testing_list[index+2][1] == "String Delimiter"):
                    del testing_list[index:(index+3)]
                    testing_list.insert(index, "literal")
                    change = True

            #Variable Identifier
            if(i[1] == "Variable Identifier"):    
                del testing_list[index]
                testing_list.insert(index, "varident")
                change = True

            #Input statement
            if(i[0] == "GIMMEH" and (index+1)<len(testing_list)):
                if(testing_list[index+1] == "varident"):
                    del testing_list[index:(index+2)]
                    testing_list.insert(index, "input")
                    change = True

            #Variable initialization 
            if(i[0] == "I HAS A" and (index+2)<len(testing_list)): # ***
                if(testing_list[index+1] == "varident" and testing_list[index+2][0] != "ITZ"):
                    del testing_list[index:(index+2)]
                    testing_list.insert(index, "varinit")
                    change = True

            #Variable assignment
            if(i == "varident" and (index+1)<len(testing_list)):
                if(testing_list[(index+1)][0] == "R"):
                    del testing_list[index:(index+2)]
                    testing_list.insert(index, "varassignstart")
                    change = True

            #String concatenation (Expression)
            if(i[0] == "SMOOSH" and (index+3)<len(testing_list)):
                if(testing_list[index+1] in ["literal", "varident", "concats"] and testing_list[index+2][0] == "AN" and testing_list[index+3] in ["literal", "varident"]):
                    del testing_list[(index+1):(index+4)]
                    testing_list.insert((index+1), "concats")
                    change = True

            #Typecasting
            if(i[0] == "MAEK" and (index+3)<len(testing_list)):
                if(testing_list[index+1] == "varident" and testing_list[index+2][0] == "A" and testing_list[index+3][1] == "TYPE Literal"):
                    del testing_list[index:(index+4)]
                    testing_list.insert(index, "typecast")
                    change = True
            if(i[0] == "MAEK" and (index+2)<len(testing_list)):
                if(testing_list[index+1] == "varident" and testing_list[index+2][1] == "TYPE Literal"):
                    del testing_list[index:(index+3)]
                    testing_list.insert(index, "typecast")
                    change = True
            if(i == "varident" and (index+2)<len(testing_list)):
                if(testing_list[index+1][0] == "IS NOW A" and testing_list[index+2][1] == "TYPE Literal"):
                    del testing_list[index:(index+3)]
                    testing_list.insert(index, "typecast")
                    change = True

            # break
            if(i[0] == "GTFO"):
                del testing_list[index]
                testing_list.insert(index, "break")
                change = True
            
            #Comment
            if(i[0] == "OBTW" or i[1] == "comment" or i[0] == "TLDR" or i[0] == "BTW"):
                del testing_list[index]
                change = True

            #Invalid
            if(i[1] == "Invalid"):
                print("Invalid Syntax")
                return(False)
            index += 1

        if(change == False):
            print("Phase 1 Complete (No Statement Introduction)") 
            break

    for i in testing_list:
        print(i)


    # ---------------------------------------            
    while(True):
        change = False
        index = 0

        for i in testing_list:
            # More String concatenation
            if(i[0] == "SMOOSH" and (index+1)<len(testing_list)):
                if(testing_list[index+1] == "concats"):
                    del testing_list[index:(index+2)]
                    testing_list.insert(index, "expr")
                    change = True
            #Print statement 
            if(i[0] == "VISIBLE" and (index+2)<len(testing_list)):
                if(testing_list[index+1] in ["printblock", "expr", "literal", "varident"] and testing_list[index+2] in ["expr", "literal", "varident"]):
                    del testing_list[(index+1):(index+3)]
                    testing_list.insert((index+1), "printblock")
                    change = True
                if(testing_list[index+1] in ["expr", "literal", "varident"] and testing_list[index+2][0] not in ["expr", "literal", "varident"]):
                    del testing_list[(index+1)]
                    testing_list.insert((index+1), "printblock")
                    change = True

            if(i[0] == "VISIBLE" and (index+3)<len(testing_list)):
                if(testing_list[index+1] in ["printblock", "expr", "literal", "varident"] and testing_list[index+2][0] == "AN" and testing_list[index+3] in ["expr", "literal", "varident"]):
                    del testing_list[(index+1):(index+4)]
                    testing_list.insert((index+1), "printblock")
                    change = True

            #Variable assignment
            if(i == "varassignstart" and (index+1)<len(testing_list)):
                if(testing_list[index+1] in ["literal", "varident", "expr", "typecast"]):
                    del testing_list[index:(index+2)]
                    testing_list.insert(index, "varassign")
                    change = True
            
            # Variable initialization 2
            if(i[0] == "I HAS A" and (index+3)<len(testing_list)):
                if(testing_list[index+1] == "varident" and testing_list[index+2][0] == "ITZ" and testing_list[index+3] in ["literal", "expr"]):
                    del testing_list[index:(index+4)]
                    testing_list.insert(index, "varinit")
                    change = True
            

            #Operations (Expression)
            if(i[0] in ["SUM OF", "DIFF OF", "PRODUKT OF", "QUOSHUNT OF", "MOD OF", "BIGGR OF", "SMALLR OF", "BOTH SAEM", "DIFFRINT"] and (index+3)<len(testing_list)):
                if(testing_list[index+1] in ["literal", "varident", "expr"] and testing_list[index+2][0] == "AN" and testing_list[index+3] in ["literal", "varident", "expr"]):
                    del testing_list[index:(index+4)]
                    testing_list.insert(index, "expr")
                    change = True

            # Boolean operations (expression)
            if(i[0] == "NOT" and (index+1)<len(testing_list)):
                if(testing_list[index+1] in ["literal", "varident", "expr", "boolop"]):
                    del testing_list[index:(index+2)]
                    testing_list.insert(index, "boolop")
                    change = True
            if(i[0] in ["BOTH OF", "EITHER OF", "WON OF"] and (index+3)<len(testing_list)):
                if(testing_list[index+1] in ["literal", "varident", "expr", "boolop"] and testing_list[index+2][0] == "AN" and testing_list[index+3] in ["literal", "varident", "expr", "boolop"]):
                    del testing_list[index:(index+4)]
                    testing_list.insert(index, "boolop")
                    change = True
            if(i in ["boolop", "varident", "literal"] and (index+3)<len(testing_list)):
                if(testing_list[index+1][0] == "AN" and testing_list[index+2] in ["boolop", "infstatement", "varident", "literal"] and testing_list[index+3][0] == "MKAY"):
                    del testing_list[index:(index+3)]
                    testing_list.insert(index, "infstatement")
                    change = True
            if(i[0] in ["ANY OF", "ALL OF"] and (index+2)<len(testing_list)):
                if(testing_list[index+1] == "infstatement" and testing_list[index+2][0] == "MKAY"):
                    del testing_list[index:(index+3)]
                    testing_list.insert(index, "expr")
                    change = True
            # print("------------------------------------")
            # for i in testing_list:
            #     print(i)
            
            
            

            index += 1

        if(change == False):
            print("Phase 2 Complete (Loops and other big structs)") 
            break
    
    # for i in testing_list:
    #     print(i)
    
    # while(True):
    #     change = False
    #     index = 0

    #     for i in testing_list:
    #         if(i == "boolop"):
    #             del testing_list[index]
    #             testing_list.insert(index, "expr")
    #             change = True
    #         index += 1

    #     if(change == False):
    #         print("Phase 2.4 WAHHHHHHHHHHHHHHHHH") 
    #         break
    
    # for i in testing_list:
    #     print(i)
    
    # ---------------------------------------            
    while(True):
        change = False
        index = 0

        for i in testing_list:
            if(i == "boolop"):
                del testing_list[index]
                testing_list.insert(index, "expr")
                change = True
            if(i[0] == "VISIBLE" and (index+1)<len(testing_list)):
                if(testing_list[index+1] == "printblock"):
                    del testing_list[index:(index+2)]
                    testing_list.insert(index, "print")
                    change = True

            if(i[0] == "VISIBLE" and (index+2)<len(testing_list)):
                if(testing_list[index+1] in ["printblock", "expr", "literal", "varident"] and testing_list[index+2] in ["expr", "literal", "varident"]):
                    del testing_list[(index+1):(index+3)]
                    testing_list.insert((index+1), "printblock")
                    change = True
                if(testing_list[index+1] in ["expr", "literal", "varident"] and testing_list[index+2][0] not in ["expr", "literal", "varident"]):
                    del testing_list[(index+1)]
                    testing_list.insert((index+1), "printblock")
                    change = True
            #if-else
            if(i[0] in ["YA RLY", "NO WAI"] and (index+2)<len(testing_list)):
                if(testing_list[index+1] in ["expr", "ifelseStatement", "print", "input", "typecast", "varassign"] and testing_list[index+2] in ["expr", "print", "input", "typecast", "varassign"]):
                    del testing_list[(index+1):(index+3)]
                    testing_list.insert((index+1), "ifelseStatement")
                    change = True
            if(i[0] == "YA RLY" and (index+2)<len(testing_list)):
                if(testing_list[index+1] in ["expr", "print", "input", "typecast", "varassign"] and testing_list[index+2][0] in ["OIC", "NO WAI"]):
                    del testing_list[index+1]
                    testing_list.insert((index+1), "ifelseStatement")
                    change = True
            if(i[0] == "NO WAI" and (index+2)<len(testing_list)):
                if(testing_list[index+1] in ["expr", "print", "input", "typecast", "varassign"] and testing_list[index+2][0] == "OIC"):
                    del testing_list[index+1]
                    testing_list.insert((index+1), "ifelseStatement")
                    change = True
            if(i[0] == "O RLY?" and (index+3)<len(testing_list)):
                if(testing_list[index+1][0] == "YA RLY" and testing_list[index+2] == "ifelseStatement" and testing_list[index+3][0] == "OIC"):
                    del testing_list[index:(index+4)]
                    testing_list.insert(index, "ifelse")
                    change = True
            if(i[0] == "O RLY?" and (index+5)<len(testing_list)):
                if(testing_list[index+1][0] == "YA RLY" and testing_list[index+2] == "ifelseStatement" and testing_list[index+3][0] == "NO WAI" and testing_list[index+4] == "ifelseStatement" and testing_list[index+5][0] == "OIC"):
                    del testing_list[index:(index+6)]
                    testing_list.insert(index, "ifelse")
                    change = True
            #Switch-case statements
            if(i[0] == "OMG" and (index+1)<len(testing_list)):
                if(testing_list[index+1] == "literal"):
                    del testing_list[index:(index+2)]
                    testing_list.insert(index, "case")
                    change = True
            if(i[0] == "OMGWTF"):
                del testing_list[index]
                testing_list.insert(index, "case")
                change = True
            if(i == "case" and (index+2)<len(testing_list)):
                if(testing_list[index+1] in ["expr", "caseblock", "input", "print", "typecast", "print", "break", "varassign"] and testing_list[index+2] in ["expr", "input", "print", "typecast", "print", "break", "varassign"]):
                    del testing_list[(index+1):(index+3)]
                    testing_list.insert((index+1), "caseblock")
                    change = True
                if(testing_list[index+1] in ["input", "print", "typecast", "print", "break"] and (testing_list[index+2][0] == "OIC" or testing_list[index+2] == "case")):
                    del testing_list[index+1]
                    testing_list.insert((index+1), "caseblock")
                    change = True
            #loops
            if(i[0] in ["TIL", "WILE"] and (index+1)<len(testing_list)):
                if(testing_list[index+1] == "expr"):
                    del testing_list[index:(index+2)]
                    testing_list.insert(index, "tilwhile")
                    change = True
            if(i[0] == "IM IN YR" and (index+5)<len(testing_list)):
                if(testing_list[index+1] == "varident" and testing_list[index+2][0] in ["UPPIN", "NERFIN"] and testing_list[index+3][0] == "YR" and testing_list[index+4] == "varident" and testing_list[index+5] == "tilwhile"):
                    del testing_list[index:(index+6)]
                    testing_list.insert(index, "loopstart")
                    change = True
            if(i[0] == "IM OUTTA YR" and (index+1)<len(testing_list)):
                if(testing_list[index+1] == "varident"):
                    del testing_list[index:(index+2)]
                    testing_list.insert(index, "loopend")
                    change = True
            if(i == "loopstart" and (index+2)<len(testing_list)):
                if(testing_list[index+1] in ["loopblock", "expr", "print", "input", "typecast", "varassign"] and testing_list[index+2] in ["loopblock", "expr", "print", "input", "typecast", "varassign"]):
                    del testing_list[(index+1):(index+3)]
                    testing_list.insert((index+1),"loopblock")
                    change = True
                if(testing_list[index+1] in ["expr", "print", "input", "typecast", "varassign"] and testing_list[index+2] == "loopend"):
                    del testing_list[(index+1)]
                    testing_list.insert((index+1),"loopblock")
                    change = True

                if(testing_list[index+1] == "loopblock" and testing_list[index+2] == "loopend"):
                    del testing_list[index:(index+3)]
                    testing_list.insert(index,"loop")
                    change = True
            index += 1

        if(change == False):
            print("Phase 2.5 WAHHHHHHHHHHHHHHHHH") 
            break
    
    for i in testing_list:
        print(i)

    # ---------------------------------------            
    while(True):
        change = False
        index = 0

        for i in testing_list:
            # Switch case 2
            if(i == "case" and (index+1)<len(testing_list)):
                if(testing_list[index+1] == "caseblock"):
                    del testing_list[index:(index+2)]
                    testing_list.insert(index, "casestatement")
                    change = True
            if(i[0] == "WTF?" and (index+2)<len(testing_list)):
                if(testing_list[index+1] == "casestatement" and testing_list[index+2] == "casestatement"):      
                    del testing_list[(index+1):(index+3)]
                    testing_list.insert((index+1), "casestatement")
                    change = True
                if(testing_list[index+1] == "casestatement" and testing_list[index+2][0] == "OIC"):      
                    del testing_list[index:(index+3)]
                    testing_list.insert((index+1), "switchcase")
                    change = True
            index += 1

        if(change == False):
            print("Phase 2.6 WAHHHHHHHHHHHHHHHHH") 
            break
    
    # for i in testing_list:
    #     print(i)


    # ---------------------------------------            
    
    while(True):
        change = False
        index = 0

        # print("-----------------------------------------")
        # for i in testing_list:
        #     print(i)
        
        
        for i in testing_list:
            #Chunky parts
            if(i == "statement" and (index+1) < len(testing_list)):
                if(testing_list[index+1] == "statement"):
                    del testing_list[index:(index+2)]
                    testing_list.insert(index, "statement")
                    change=True
            if(i in ["varinit", "statement2"]):
                del testing_list[index]
                testing_list.insert(index, "statement")
                change = True
            if(i in ["print", "input", "varassign", "ifelse", "expr", "switchcase", "loop", "typecast"]):
                del testing_list[index]
                testing_list.insert(index, "statement2")
                change = True
            
            if(i[0] == "HAI" and len(testing_list) == 3):
                if(testing_list[index+1] == "statement" and testing_list[index+2][0] == "KTHXBYE"):
                    del testing_list[index:(index+3)]
                    testing_list.insert(index, "program")
                    change = True
                    print(True)

                    for i in testing_list:
                        print(i)
                    return(True)
            index += 1

        if(change == False):
            
            print("Phase 3 Complete (finishing touches)")
            # for i in testing_list:
            #     print(i)
            
            print(False) 
            return(False)
            break






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

x = """HAI

	I HAS A choice
	I HAS A input

	BTW if w/o MEBBE, 1 only, everything else is invalid
	VISIBLE "1. Compute age"
	VISIBLE "2. Compute tip"
	VISIBLE "3. Compute square area"
	VISIBLE "0. Exit"

	VISIBLE "Choice: "
	GIMMEH choice

	BOTH SAEM choice AN 1
	O RLY?
		YA RLY
			VISIBLE "Enter birth year: "
			GIMMEH input
			VISIBLE DIFF OF 2022 AN input
OBTW
	BTW uncomment this portion if you have MEBBE
	BTW else, this portion should be ignored

		MEBBE BOTH SAEM choice AN 2
			VISIBLE "Enter bill cost: "
			GIMMEH input
			VISIBLE "Tip: " PRODUCKT OF input AN 0.1
		MEBBE BOTH SAEM choice AN 3
			VISIBLE "Enter width: "
			GIMMEH input
			VISIBLE "Square Area: " PRODUCKT OF input AN input
		MEBBE BOTH SAEM choice AN 0
			VISIBLE "Goodbye"
TLDR
		NO WAI
			VISIBLE "Invalid Input!"
	OIC

	DIFFRINT BIGGR OF 3 AN choice AN 3
	O RLY?
		YA RLY
			VISIBLE "Invalid input is > 3."
	OIC

KTHXBYE"""


y = """BOTH SAEM choice AN 1
	O RLY?
		YA RLY
			I HAS A monde
			GIMMEH input
			VISIBLE DIFF OF 2022 AN input"""

z = "SMOOSH monde AN \"bruh\" AN 123"
a = "ANY OF NOT x AN BOTH OF y AN z AN EITHER OF x AN y MKAY"
b = "BOTH SAEM x AN BIGGR OF x AN y"
c = "MAEK var1 YARN"
d = """O RLY?
		YA RLY
			VISIBLE "Enter birth year: "
            bruh R bruh
        NO WAI
            VISIBLE bruh
	OIC
    I HAS A MONDE
    I HAS A MONDE
    I HAS A MONDE
    I HAS A MONDE
    I HAS A MONDE"""
e = """GIMMEH bruh
GIMMEH bruh
GIMMEH bruh
GIMMEH bruh
GIMMEH bruh
SUM OF x AN Y
SUM OF x AN Y
SUM OF x AN Y
SUM OF x AN Y
I HAS A MONDE
KTHXBYE"""

f = """WTF?
		OMG 1
			VISIBLE "Enter birth year: " SMOOSH x AN x AN x AN y AN y
			bruh R SMOOSH x AN x AN x AN y AN y
            GIMMEH input
			VISIBLE DIFF OF 2022 AN input
			GTFO
		OMG 2
			VISIBLE "Enter bill cost: "
			GIMMEH input
			VISIBLE "Tip: " PRODUKT OF input AN 0.1
			GTFO
		OMG 3
			VISIBLE "Enter width: "
			GIMMEH input
			VISIBLE "Square Area: " PRODUKT OF input AN input
            bruh IS NOW A NUMBR
			GTFO
            SMOOSH x AN x AN x AN y AN y
		OMG 0
			VISIBLE "Goodbye"
		OMGWTF
			VISIBLE "Invalid Input!"
	OIC"""



h = """HAI
    BTW variable dec
    I HAS A x
    I HAS A y
    
    VISIBLE "Hello! Please enter two strings:"
    VISIBLE "String 1: "
    GIMMEH x
    VISIBLE "String 2: "
    GIMMEH y

    VISIBLE SMOOSH x AN y

    VISIBLE SMOOSH x AN x AN x AN y AN y

    x R SMOOSH x AN y
    y R 100
    VISIBLE x AN 52615 AN y AN MOD OF 10 AN 6 AN "End!"

    VISIBLE 10 AN y
    y IS NOW A NUMBAR
    VISIBLE 10 AN y

    y R 0
    y R MAEK y TROOF
    VISIBLE y
KTHXBYE
"""

g = """HAI
    BTW variable dec
    I HAS A x
    I HAS A y
    
    VISIBLE "x:" WIN ", y:" WIN
    x R WIN
    y R WIN

    VISIBLE BOTH OF x AN y
    VISIBLE EITHER OF x AN y
    VISIBLE WON OF x AN y
    VISIBLE NOT x
    VISIBLE ALL OF x AN x AN x AN y MKAY
    VISIBLE ANY OF y AN y AN y AN 0 MKAY
    VISIBLE ANY OF BOTH OF x AN EITHER OF NOT x AN y AN y AN NOT y MKAY
    VISIBLE BOTH OF x AN EITHER OF NOT x AN y

    VISIBLE "x:" FAIL ", y:" WIN
    x R FAIL

    VISIBLE BOTH OF x AN y
    VISIBLE EITHER OF x AN y
    VISIBLE WON OF x AN y
    VISIBLE NOT x
    VISIBLE ALL OF x AN x AN x AN y MKAY
    VISIBLE ANY OF y AN y AN y AN 0 MKAY
    
    VISIBLE BOTH OF x AN EITHER OF NOT x AN y

    VISIBLE "x:" FAIL ", y:" FAIL
    y R FAIL

    VISIBLE BOTH OF x AN y
    VISIBLE EITHER OF x AN y
    VISIBLE WON OF x AN y
    VISIBLE NOT x
    VISIBLE ALL OF x AN x AN x AN y MKAY
    VISIBLE ANY OF y AN y AN y AN 0 MKAY
    VISIBLE ANY OF BOTH OF x AN EITHER OF NOT x AN y AN y AN NOT y MKAY
    VISIBLE BOTH OF x AN EITHER OF NOT x AN y
KTHXBYE

"""

x = """ANY OF BOTH OF x AN EITHER OF NOT x AN y AN y AN NOT y MKAY"""
# BOTH OF x AN EITHER OF NOT x AN y AN y AN NOT y
# BOTH OF x AN EITHER OF x AN y AN y AN NOT y
# BOTH OF x AN EITHER OF x AN y AN y AN y
lex_analyze(lexemeArr, g)

# VISIBLE x "-" y " = " DIFF OF x AN y
#     VISIBLE x "*" y " = " PRODUKT OF x AN y
#     VISIBLE x "/" y " = " QUOSHUNT OF x AN y
#     VISIBLE x "%" y " = " MOD OF x AN y
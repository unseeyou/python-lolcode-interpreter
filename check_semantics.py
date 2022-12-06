# Semantics Analyzer Implementation
import grab_lexeme

lexemeArr = []
symbolTable = []

# temp


def print_symbolTable(symbolTable):
    for i in symbolTable:
        print(i)


def grab_identifiers(symbolTable):
    identifiers = []

    for i in symbolTable:
        identifiers.append(i[0])

    return identifiers

# function that checks if identifier already exists. If not, append. If existing, update the symbol table


def insertToTable(testing_list, symbolTable, index, data_type, new_identifier, new_value):
    if new_identifier not in grab_identifiers(symbolTable):
        symbolTable.append([new_identifier, new_value, data_type])
    else:
        dupIndex = grab_identifiers(symbolTable).index(
            new_identifier)
        del symbolTable[dupIndex]
        symbolTable.insert(
            dupIndex, [new_identifier, new_value, data_type])


def findValue(symbolTable, identifier):
    identifiers = grab_identifiers(symbolTable)
    if identifier in identifiers:
        index = identifiers.index(identifier)

    for i, content in enumerate(symbolTable):
        if symbolTable[i][0] == identifier:
            # return value and identifier
            return [symbolTable[i][1], symbolTable[i][2]]

    return False


# as of 12-07, evaluates just the same
def typecast_compute(value1, type1, value2, type2, op):
    result_type = ""

    if type1 == type2:
        if type1 == "NUMBR Literal":
            value1 = int(value1)
            value2 = int(value2)
            result_type = "NUMBR Literal"
        elif type1 == "NUMBAR Literal":
            value1 = float(value1)
            value2 = float(value2)
            result_type = "NUMBAR Literal"
        elif type1 == "TROOF Literal":
            if value1 == "WIN":
                value1 = 1
            else:
                value1 = 0

            if value2 == "WIN":
                value1 = 1
            else:
                value1 = 0
            result_type = "NUMBR Literal"

        elif type1 == "NOOB":
            value1 = 0  # translate to TROOF which FAIL (0)
            value2 = 0
            result_type = "NUMBR Literal"
        # elif type1 = "YARN Literal":  Note: How does typecasting works for YARN?
        #     value = ASCII

    # else: different operations
    #     if type1 == "NUMBAR Literal" or type2 == "NUMBAR Literal":
    #         if type1 == "NUMBAR Literal":
    #             value1 = float(value1)
    #         else:
    #             value2 = float(value2)

    if op == "SUM OF":
        # returns the final value with its type
        return [value1 + value2, result_type]
    elif op == "DIFF OF":
        return [value1 - value2, result_type]
    elif op == "PRODUKT OF":
        return [value1 * value2, result_type]
    elif op == "QUOSHUNT OF":
        # if result_type == "NUMBR Literal":
        #     final_value = value1 / value2
        #     return [int(final_value), result_type]
        # else:
        #     # NOTE: To add: Shift data type to NUMBAR if result has decimals
        return [value1 / value2, result_type]
    elif op == "MOD OF":
        return [value1 % value2, result_type]
    elif op == "BIGGR OF":
        return [max(value1, value2), result_type]
    elif op == "SMALLR OF":
        return [min(value1, value2), result_type]


def grab_symbol_table(lexemeArr):
    testing_list = []
    error_prompt = ""  # variale to be replaced with the error encountered
    output_arr = []  # arr to hold all the strings to be output in terminal

    # lexemes identifier
    typecast_elig = ["NUMBR Literal", "NUMBAR Literal",
                     "YARN Literal", "TROOF Literal", "NOOB"]
    arithmetic_op = ["SUM OF", "DIFF OF", "PRODUKT OF",
                     "QUOSHUNT OF", "MOD OF", "BIGGR OF", "SMALLR OF"]

    for i in lexemeArr:
        testing_list.append(i)

    for index, i in enumerate(testing_list):
        # Variable initialization
        if (i[0] == "I HAS A" and (index+1) < len(testing_list)):
            if testing_list[index+1][1] == "Variable Identifier":
                if (index + 2) < len(testing_list):
                    if testing_list[index+2][0] != "ITZ":
                        insertToTable(testing_list, symbolTable,
                                      index, "NOOB", testing_list[index+1][0], "NOOB")
                elif (index + 2) == len(testing_list):
                    insertToTable(testing_list, symbolTable,
                                  index, "NOOB", testing_list[index+1][0], "NOOB")

        # Variable assignment (Case 1.1: Literal is NUMBR, NUMBAR, TROOF)
        if (i[0] == "I HAS A" and (index+3) < len(testing_list)):
            if (testing_list[index+1][1] == "Variable Identifier" and testing_list[index+2][0] == "ITZ"):
                if testing_list[index+3][1] in ["NUMBR Literal", "NUMBAR Literal", "TROOF Literal"]:
                    insertToTable(testing_list, symbolTable,
                                  index, testing_list[index+3][1], testing_list[index+1][0], testing_list[index+3][0])
        # Variable assignment (Case 1.2: YARN Literal)
        if (i[0] == "I HAS A" and (index+5) < len(testing_list)):
            if (testing_list[index+1][1] == "Variable Identifier" and testing_list[index+2][0] == "ITZ"):
                if testing_list[index+3][1] == "String Delimiter" and testing_list[index+4][1] == "YARN Literal" and testing_list[index+5][1] == "String Delimiter":
                    insertToTable(testing_list, symbolTable, index, testing_list[index+1][1],
                                  testing_list[index+1][0], testing_list[index+4][0])
        # Variable assignment (Case 1.3: Var Identifier)
        if (i[0] == "I HAS A" and (index+3) < len(testing_list)):
            if (testing_list[index+1][1] == "Variable Identifier" and testing_list[index+2][0] == "ITZ") and testing_list[index+3][1] == "Variable Identifier":
                new_value = findValue(symbolTable, testing_list[index+3][0])

                if new_value != False:  # if variable is not initialized
                    insertToTable(testing_list, symbolTable, index, new_value[1],
                                  testing_list[index+1][0], new_value[0])
                else:
                    error_prompt = "SemanticsError: variable identifier \'" + \
                        testing_list[index+3][0] + "\' is not defined"
                    return [False, error_prompt, symbolTable, output_arr]

        # Variable assignment (Case 1.4: Simple Expression)
        if (i[0] == "I HAS A" and (index+5) < len(testing_list)):
            if (testing_list[index+1][1] == "Variable Identifier" and testing_list[index+2][0] == "ITZ" and testing_list[index+3][0] in arithmetic_op):
                # Case 1: OPERATION literal AN literal
                if testing_list[index+4][1] in typecast_elig and testing_list[index+5][0] == "AN" and testing_list[index+6][1] in typecast_elig:
                    result = typecast_compute(testing_list[index+4][0], testing_list[index+4][1],
                                              testing_list[index+6][0], testing_list[index+6][1], testing_list[index+3][0])
                    result_value = result[0]
                    result_type = result[1]
                    insertToTable(testing_list, symbolTable, index, result_type,
                                  testing_list[index+1][0], result_value)
                # Case 2: OPERATION varident AN literal
                if testing_list[index+4][1] in "Variable Identifier" and testing_list[index+5][0] == "AN" and testing_list[index+6][1] in typecast_elig:

                    new_value = findValue(
                        symbolTable, testing_list[index+4][0])

                    if new_value != False:  # if variable is initialized
                        result = typecast_compute(new_value[0], new_value[1],
                                                  testing_list[index+6][0], testing_list[index+6][1], testing_list[index+3][0])
                        result_value = result[0]
                        result_type = result[1]
                        insertToTable(testing_list, symbolTable, index, result_type,
                                      testing_list[index+1][0], result_value)
                    else:
                        error_prompt = "SemanticsError: variable identifier \'" + \
                            testing_list[index+4][0] + "\' is not defined"
                        return [False, error_prompt, symbolTable, output_arr]

            # Case 2: OPERATION varident AN literal
            # Case 3: OPERATION literal AN varident
            # Case 3: OPERATION varident AN varident

        # Variable assignment (Case 1.5: Compex Expression)

        # Visible for YARN Literal
        if i[0] == "VISIBLE" and (index+3) < len(testing_list):
            if testing_list[index+1][1] == "String Delimiter" and testing_list[index+2][1] == "YARN Literal" and testing_list[index+3][1] == "String Delimiter":
                insertToTable(testing_list, symbolTable, index,
                              'temp', 'IT', testing_list[index+2][0])

                # add output in terminal format
                output_arr.append(testing_list[index+2][0])

        # Variable Case 1.1: VISIBLE varident format
        if i[0] == "VISIBLE" and (index+1) < len(testing_list):
            if testing_list[index+1][1] == "Variable Identifier":
                new_value = findValue(symbolTable, testing_list[index+1][0])

                if new_value != False:
                    insertToTable(testing_list, symbolTable, index, new_value[1],
                                  "IT", new_value[0])

                    output_arr.append(new_value[0])
                else:  # if variable is not initialized
                    error_prompt = "SemanticsError: variable identifier \'" + \
                        testing_list[index+1][0] + "\' is not defined"
                    return [False, error_prompt, symbolTable, output_arr]

    return [True, error_prompt, symbolTable, output_arr]


def lex_analyze(lexemeArr, the_long_string):
    lexemeArr.clear()

    lines = the_long_string.split("\n")

    lines2 = []
    for line in lines:
        if (line != ""):
            lines2.append(line.strip())

    for i in range(0, len(lines2)):
        while (lines2[i] != ''):
            grab_lexeme.get_lexemes(lexemeArr, lines2, lines2[i], i)

    grab_symbol_table(lexemeArr)


# temp: test cases
k = "HAI I HAS A monde KTHXBYE"
g = """HAI
    I HAS A monde
    I HAS A num ITZ 17
    I HAS A num ITZ 18
    I HAS A name ITZ "seventeen"
    I HAS A fnum ITZ 17.0
    I HAS A flag ITZ WIN
    I HAS A dup ITZ num

    I HAS A sum ITZ SUM OF num AN 13
    I HAS A diff ITZ DIFF OF sum AN 17
    I HAS A prod ITZ PRODUKT OF 3 AN 4
    I HAS A quo ITZ QUOSHUNT OF 4 AN 5

KTHXBYE"""
h = """HAI

    I HAS A monde
    I HAS A num ITZ 17
    I HAS A name ITZ "seventeen"
    I HAS A fnum ITZ 17.0
    I HAS A flag ITZ WIN

KTHXBYE
"""

#lex_analyze(lexemeArr, g)

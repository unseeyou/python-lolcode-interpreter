# Semantics Analyzer Implementation
import grab_lexeme
import re
from operator import xor
from tkinter import simpledialog
import copy
import math

lexemeArr = []


def get_input(value):
    input_promt = "Input value of " + value + " :"
    x = simpledialog.askstring(title="GIMMEH", prompt=input_promt)
    if len(x) == 0:
        x = x.replace(x, "\"\"")
    return [x, "YARN Literal"]


def print_symbolTable(symbolTable):
    for i in symbolTable:
        print(i)


def grab_identifiers(symbolTable):
    identifiers = []

    for i in symbolTable:
        identifiers.append(i[0])

    return identifiers


def truncate(number, digits):
    nbDecimals = len(str(number).split('.')[1])
    if nbDecimals <= digits:
        return number
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


def insertInSymbolTable(symbolTable, new_identifier, new_value, data_type):
    print("Adding " + new_identifier + "")
    if new_identifier not in grab_identifiers(symbolTable):
        symbolTable.append([new_identifier, new_value, data_type])
    else:
        dupIndex = grab_identifiers(symbolTable).index(
            new_identifier)
        del symbolTable[dupIndex]
        symbolTable.insert(
            dupIndex, [new_identifier, new_value, data_type])


def findValue(symbolTable, identifier):
    for i in range(len(symbolTable)):
        if symbolTable[i][0] == identifier:
            # return value and identifier
            return [symbolTable[i][1], symbolTable[i][2]]
    return False


def boolean_not(value1, type1):
    if type1 == "TROOF Literal":
        if value1 == "WIN":
            value1 = 1
        else:
            value1 = 0
    elif type1 != "TROOF Literal":
        if value1 == "\"\"":
            value1 = 0
        elif int(value1) == 0:
            value1 = 0
        else:
            value1 = 1

    print("Not", value1)

    if value1 == 0:
        return [True, "WIN", "TROOF Literal"]
    else:
        return [True, "FAIL", "TROOF Literal"]


def boolean_op(value1, type1, value2, type2, op):

    # The empty string (“”) and numerical zero values are cast to FAIL.
    # All other values, except those mentioned above, are cast to WIN.

    print("Initial v1", value1)
    print("Initial v2", value2)
    # typecast to TROOF
    if type1 == "TROOF Literal":
        if value1 == "WIN":
            value1 = 1
        else:
            value1 = 0
    if type2 == "TROOF Literal":
        if value2 == "WIN":
            value2 = 1
        else:
            value2 = 0

    if type1 != "TROOF Literal":
        if value1 == "\"\"":
            value1 = 0
        elif int(value1) == 0:
            value1 = 0
        else:
            value1 = 1

        type1 = type1.replace(type1, "TROOF Literal")

    if type2 != "TROOF Literal":
        if value2 == "\"\"":
            value2 = 0
        elif int(value2) == 0:
            value2 = 0
        else:
            value2 = 1

        print("Value2", value2)
        type2 = type2.replace(type2, "TROOF Literal")

    print(value1, "vs", value2)

    if op == "BOTH OF":
        result = value1 and value2
        print("Result:", result)

        if result == 1:
            return [True, "WIN", "TROOF Literal"]
        else:
            return [True, "FAIL", "TROOF Literal"]
    elif op == "EITHER OF":
        result = value1 or value2

        if result == 1:
            return [True, "WIN", "TROOF Literal"]
        else:
            return [True, "FAIL", "TROOF Literal"]
    elif op == "WON OF":
        result = xor(bool(value1), bool(value2))

        if result == 1:
            return [True, "WIN", "TROOF Literal"]
        else:
            return [True, "FAIL", "TROOF Literal"]


def comparison_op(value1, type1, value2, type2, op):
    # there is no typecasting for BOTH SAEM and DIFFRINT
    error_prompt = ""
    result_type = ""

    if type1 not in ["NUMBR Literal", "NUMBAR Literal"]:
        errorPrompt = "SemanticsError: no automatic typecast of " + \
            str(type1) + " \"" + str(value1) + \
            "\" to NUMBR Literal/NUMBAR Literal"
        print(errorPrompt)
        return [False, errorPrompt]

    if type2 not in ["NUMBR Literal", "NUMBAR Literal"]:
        errorPrompt = "SemanticsError: no automatic typecast of " + \
            str(type2) + " \"" + str(value2) + \
            "\" to NUMBR Literal/NUMBAR Literal"
        print(errorPrompt)
        return [False, errorPrompt]

    if type1 != type2:
        errorPrompt = "SemanticsError: no automatic typecast for " + \
            str(value1) + " or " + str(value2)
        print(errorPrompt)
        return [False, errorPrompt]
    else:
        if type1 == "NUMBR Literal":
            value1 = int(value1)
            value2 = int(value2)
        else:
            value1 = float(value1)
            value2 = float(value2)

    if op == "BOTH SAEM":
        if value1 == value2:
            return [True, "WIN", "TROOF Literal"]
        else:
            return [True, "FAIL", "TROOF Literal"]
    elif op == "DIFFRINT":
        if value1 != value2:
            return [True, "WIN", "TROOF Literal"]
        else:
            return [True, "FAIL", "TROOF Literal"]


def arithmetic_op(value1, type1, value2, type2, op):
    # check string. If possible, typecast
    errorPrompt = ""

    if type1 == "YARN Literal":
        if (re.search('(^[0-9]+$)', value1)):
            value1 = int(value1)
            type1 = type1.replace(type1, "NUMBR Literal")
        elif (re.search('(^-?\d*\.(\d)+$)', value1)):
            value1 = float(value1)
            type1 = type1.replace(type1, "NUMBAR Literal")
        else:
            errorPrompt = "SemanticsError: invalid implicit typecast of " + \
                str(value1) + " to NUMBR/NUMBAR Literal"
            print(errorPrompt)
            return [False, errorPrompt]
    if type2 == "YARN Literal":
        if (re.search('(^[0-9]+$)', value2)):
            value2 = int(value2)
            type2 = type2.replace(type2, "NUMBR Literal")
        elif (re.search('(^-?\d*\.(\d)+$)', value2)):
            value2 = float(value2)
            type2 = type2.replace(type2, "NUMBAR Literal")
        else:
            errorPrompt = "SemanticsError: invalid implicit typecast of " + \
                str(value2) + " to NUMBR/NUMBAR Literal"
            print(errorPrompt)
            return [False, errorPrompt]

    # typecast to TROOF to numerical
    if type1 == "TROOF Literal":
        if value1 == "WIN":
            value1 = 1
        else:
            value1 = 0
        type1 = type1.replace(type1, "NUMBR Literal")
    if type2 == "TROOF Literal":
        if value2 == "WIN":
            value2 = 1
        else:
            value2 = 0
        type2 = type2.replace(type2, "NUMBR Literal")

    # typecast NOOB to numerical
    if type1 == "NOOB":
        # The empty string (“”) and numerical zero values are cast to FAIL.
        if value1 == "" or value1 == 0:  # convert value1 to TROOF equivalent
            value1 = 0  # FAIL = 0
        else:
            value1 = 1  # WIN = 1
        type1 = type1.replace(type1, "NUMBR Literal")
    if type2 == "NOOB":
        if value2 == "" or value2 == 0:  # convert value1 to TROOF equivalent
            value2 = 0  # FAIL = 0
        else:
            value2 = 1  # WIN = 1
        type2 = type2.replace(type2, "NUMBR Literal")

    # compare the two data types
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
    else:
        value1 = float(value1)
        value2 = float(value2)
        result_type = "NUMBAR Literal"

    # compute with the final data types
    if op == "SUM OF":
        return [True, value1 + value2, result_type]
    elif op == "DIFF OF":
        return [True, value1 - value2, result_type]
    elif op == "PRODUKT OF":
        return [True, value1 * value2, result_type]
    elif op == "QUOSHUNT OF":
        result = value1 / value2
        if value1 % value2 != 0:
            return [True, result, "NUMBAR Literal"]
        else:
            return [True, int(result), result_type]
    elif op == "MOD OF":
        return [True, value1 % value2, result_type]
    elif op == "BIGGR OF":
        return [True, max(value1, value2), result_type]
    elif op == "SMALLR OF":
        return [True, min(value1, value2), result_type]


def typecast(prevVal, prevType, newType):
    newType = newType.replace(newType, newType + " Literal")
    newValue = copy.deepcopy(prevVal)

    if prevType == "NUMBR Literal":
        prevVal = int(prevVal)
        if newType == "NUMBAR Literal":
            newValue = float(prevVal)
        elif newType == "TROOF Literal":
            if prevVal == 0:
                newValue = "FAIL"
            else:
                newValue = "WIN"
        elif newType == "YARN Literal":
            newValue = str(prevVal)
    elif prevType == "NUMBAR Literal":
        prevVal = float(prevVal)
        if newType == "NUMBR Literal":
            newValue = int(prevVal)
        elif newType == "TROOF Literal":
            if prevVal == 0.0:
                newValue = "FAIL"
            else:
                newValue = "WIN"
        elif newType == "YARN Literal":
            # casting NUMBARs to YARN will truncate the decimal portion up to two decimal places.
            return [True, truncate(prevVal, 2), newType]
    elif prevType == "TROOF Literal":
        if newType == "NUMBR Literal":
            if prevVal == "FAIL":
                return [True, 0, newType]
            elif prevVal == "WIN":
                return [True, 1, newType]
        if newType == "NUMBAR Literal":
            if prevVal == "FAIL":
                return [True, 0, newType]
            elif prevVal == "WIN":
                return [True, 1.0, newType]
        if newType == "YARN Literal":
            return [True, prevVal, newType]
    elif prevType == "YARN Literal":
        if newType == "NUMBR Literal":
            if (re.search('(^[0-9]+$)', prevVal)):
                return [True, int(prevVal), newType]
            elif (re.search('(^-?\d*\.(\d)+$)', prevVal)):
                prevValFloat = float(prevVal)
                #prevValInt = prevValFoat - (prevValFoat % 0.01)
                return [True, int(prevValFloat), newType]
            else:
                error_prompt = "SemanticsError: cannot typecast " + \
                    str(prevVal) + " to NUMBR Literal"
                return [False, error_prompt]
        if newType == "NUMBAR Literal":
            if (re.search('(^-?\d*\.(\d)+$)', prevVal)) or (re.search('(^[0-9]+$)', prevVal)):
                return [True, float(prevVal), newType]
            else:
                error_prompt = "SemanticsError: cannot typecast " + \
                    str(prevVal) + " to NUMBAR Literal"
                return [False, error_prompt]
        if newType == "TROOF Literal":
            if prevVal == "\"\"" or prevVal == "0":
                return [True, "FAIL", newType]
            else:
                return [True, "WIN", newType]

    return [True, newValue, newType]


def smoosh(datatypes_arr, to_eval_list):
    # convert non-yarn to yarn
    for index, i in enumerate(to_eval_list):
        if i[1] in datatypes_arr and i[1] != "YARN Literal":
            i[0] = str(i[0])
            i[1] = "YARN Literal"

    # concatenate the expressions
    while (True):
        change = False
        for index, i in enumerate(to_eval_list):
            if i[1] == "YARN Literal" and (index + 2) < len(to_eval_list):
                if to_eval_list[index+1][0] == "AN" and to_eval_list[index + 2][1] == "YARN Literal":
                    newStr = i[0] + " " + to_eval_list[index + 2][0]

                    del to_eval_list[index: index + 3]
                    to_eval_list.insert(index, [newStr, "YARN Literal"])

                    change = True

        if change == False:
            print("SMOOSH Phase 2")
            break

    return to_eval_list[0]


def grab_symbol_table(lexemeArr):
    testing_list = []
    error_prompt = ""
    output_arr = []
    symbolTable = []

    for i in lexemeArr:
        testing_list.append(i)

    operations_arr = ["SUM OF", "DIFF OF", "PRODUKT OF",
                      "QUOSHUNT OF", "MOD OF", "BIGGR OF", "SMALLR OF", "BOTH SAEM", "DIFFRINT", "NOT", "BOTH OF", "EITHER OF", "WON OF"]
    arithmetic_arr = ["SUM OF", "DIFF OF", "PRODUKT OF",
                      "QUOSHUNT OF", "MOD OF", "BIGGR OF", "SMALLR OF"]
    comparison_arr = ["BOTH SAEM", "DIFFRINT"]
    boolean_arr = ["BOTH OF", "EITHER OF", "WON OF"]
    boolean_start = ["ALL OF", "ANY OF"]
    datatypes_arr = ["NUMBR Literal", "NUMBAR Literal",
                     "YARN Literal", "TROOF Literal", "NOOB"]

    while (True):
        change = False

        for index, i in enumerate(testing_list):
            # remove quotation marks
            if i[0] == "\"" and (index + 2) < len(testing_list):
                if testing_list[index+1][1] == "YARN Literal" and testing_list[index+2][0] == "\"":
                    temp = testing_list[index+1]
                    del testing_list[index: (index + 3)]
                    testing_list.insert(index, temp)
                    change = True
            # remove optional A (return MAEK varident TYPE)
            if i[0] == "MAEK" and (index + 2) < len(testing_list):
                if testing_list[index+1][1] == "Variable Identifier" and testing_list[index+2][0] == "A" and testing_list[index+3][1] == "TYPE Literal":
                    del testing_list[index+2]
                    change = True

            # number R MAEK number YARN
            if i[1] == "Variable Identifier" and (index + 4) < len(testing_list):
                if testing_list[index+1][0] == "R" and testing_list[index+2][0] == "MAEK" and testing_list[index+3][0] == i[0]:
                    del testing_list[index+1: index+4]
                    testing_list.insert(index+1, ["IS NOW A", 'keyword'])

        if (change == False):
            print("Phase 1")
            print(testing_list)
            break
# ------------------------------------------------------------------------------------------------------------------------------
    while (True):
        change = False

        for index, i in enumerate(testing_list):
            # print(index)

            # single line variable stored in the IT variable
            if (i[1] == "linebreak" and (index+1) < len(testing_list)):
                if (testing_list[index+1][1] in "Variable Identifier" and testing_list[index+2][1] == "linebreak"):
                    value = findValue(symbolTable, testing_list[index+1][0])

                    if value != False:
                        insertInSymbolTable(
                            symbolTable, "IT", value[0], value[1])
                    else:
                        error_prompt = "SemanticsError: variable identifier \'" + \
                            testing_list[index+1][0] + "\' is not defined"
                        return [False, error_prompt, symbolTable, output_arr]

            # single line expressions stored in the IT variable
            if (i[1] == "linebreak" and (index+1) < len(testing_list)):
                if (testing_list[index+1][0] in operations_arr):
                    start_index = index+1
                    j = start_index
                    while testing_list[j][1] != 'linebreak':
                        j = j + 1

                    # get that portion of line then evaluate until only
                    to_eval_list = testing_list[start_index: j]
                    print("----Eval----")
                    print(to_eval_list)
                    print("------------")

                    # replace all variabes first
                    for index, i in enumerate(to_eval_list):
                        if i[1] == "Variable Identifier":
                            value = findValue(
                                symbolTable, to_eval_list[index][0])

                            if value != False:
                                del to_eval_list[index]
                                to_eval_list.insert(index, value)
                            else:
                                error_prompt = "SemanticsError: variable identifier \'" + \
                                    to_eval_list[index][0] + \
                                    "\' is not defined"
                                print(error_prompt)  # temp
                                return [False, error_prompt, symbolTable, output_arr]
                    # evaluate expressions
                    while (True):
                        change1 = False
                        for index, i in enumerate(to_eval_list):
                            if i[0] == "NOT" and (index + 1) < len(to_eval_list):
                                if to_eval_list[index+1][1] in datatypes_arr:
                                    evaluated = boolean_not(
                                        to_eval_list[index+1][0], to_eval_list[index+1][1])

                                    if evaluated[0] != False:
                                        del to_eval_list[(index):(index+2)]
                                        print("---Before-----")
                                        print(to_eval_list)
                                        to_eval_list.insert(
                                            index, evaluated[1:3])
                                        print("---After-----")
                                        print(to_eval_list)
                                        change1 = True
                                    else:
                                        output_arr.append(evaluated[1])
                                        return [False, error_prompt, symbolTable, output_arr]

                            if i[0] in operations_arr and (index + 3) < len(to_eval_list):
                                if to_eval_list[index+1][1] in datatypes_arr and to_eval_list[index+2][0] == "AN" and to_eval_list[index+3][1] in datatypes_arr:
                                    # call function that accepts value1, type1, value2, type2 and operation

                                    if i[0] in arithmetic_arr:  # check if to peform arithmetic
                                        evaluated = arithmetic_op(
                                            to_eval_list[index+1][0], to_eval_list[index+1][1], to_eval_list[index+3][0], to_eval_list[index+3][1], i[0])
                                    elif i[0] in comparison_arr:  # check if to perform comparison
                                        evaluated = comparison_op(
                                            to_eval_list[index+1][0], to_eval_list[index+1][1], to_eval_list[index+3][0], to_eval_list[index+3][1], i[0])
                                    elif i[0] in boolean_arr:  # check if to perform boolean
                                        evaluated = boolean_op(
                                            to_eval_list[index+1][0], to_eval_list[index+1][1], to_eval_list[index+3][0], to_eval_list[index+3][1], i[0])

                                        print(evaluated)

                                    if evaluated[0] != False:
                                        del to_eval_list[(index):(index+4)]
                                        to_eval_list.insert(
                                            index, evaluated[1:3])
                                        change1 = True
                                    else:
                                        output_arr.append(evaluated[1])
                                        return [False, error_prompt, symbolTable, output_arr]

                        if (change1 == False):
                            print("Done evaluating!")
                            print("----Before-----")
                            print(testing_list)

                            print("----After-----")
                            del testing_list[start_index: j]
                            testing_list.insert(start_index, to_eval_list[0])
                            insertInSymbolTable(
                                symbolTable, "IT", to_eval_list[0][0], to_eval_list[0][1])
                            print(testing_list)
                            print("-------------")
                            break

            # if else block
            if (i[0] == "O RLY?"):
                if (testing_list[index+1][1] == "linebreak" and testing_list[index+2][0] == "YA RLY"):
                    print("DRIFTOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
                    start_index = index+4
                    j = start_index
                    while testing_list[j][0] not in ["OIC", "NO WAI"]:
                        j = j + 1
                    print(testing_list[j][0])
                    print(testing_list[j][0] == "OIC")

                    if (testing_list[j][0] == "OIC"):
                        itVal = findValue(symbolTable, "IT")
                        # print(itVal)
                        if (itVal[1] != "TROOF Literal"):
                            itVal = typecast(itVal[0], itVal[1], "TROOF")
                            del itVal[0]
                        # print(itVal)
                        new_testing_list = testing_list[start_index:j]
                        del testing_list[start_index:j]
                        if (itVal[0] == "WIN"):
                            x = grab_symbol_table(new_testing_list)
                            # print(x[0])
                            # print(x[1])
                            # print(x[2])
                            # print(x[3])

                            if (x[0]):
                                for symbolTableVal in x[2]:
                                    symbolTable.append(symbolTableVal)
                                    # print(symbolTableVal)
                                for output_arrVal in x[3]:
                                    output_arr.append(output_arrVal)
                                    # print(output_arrVal)
                    if (testing_list[j][0] == "NO WAI"):
                        start_index2 = j+2
                        k = start_index2
                        while testing_list[k][0] != "OIC":
                            k = k + 1

                        # print(testing_list[k][0])
                        new_testing_list2 = testing_list[start_index2:k]
                        del testing_list[start_index2:k]

                        new_testing_list = testing_list[start_index:j]
                        del testing_list[start_index:j]

                        itVal = findValue(symbolTable, "IT")
                        # print(itVal)
                        if (itVal[1] != "TROOF Literal"):
                            itVal = typecast(itVal[0], itVal[1], "TROOF")
                            del itVal[0]

                        if (itVal[0] == "WIN"):
                            x = grab_symbol_table(new_testing_list)
                        else:
                            x = grab_symbol_table(new_testing_list2)

                        if (x[0]):
                            for symbolTableVal in x[2]:
                                symbolTable.append(symbolTableVal)
                                # print(symbolTableVal)
                            for output_arrVal in x[3]:
                                output_arr.append(output_arrVal)
                                # print(output_arrVal)

                    print("DRIFTOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")

            # variable assignment (I HAS A var)
            if (i[0] == "I HAS A" and (index+1) < len(testing_list)):
                if testing_list[index+1][1] == "Variable Identifier":
                    if (index + 2) < len(testing_list):
                        if testing_list[index+2][0] != "ITZ":
                            insertInSymbolTable(symbolTable, testing_list[index+1][0],
                                                "NOOB", "NOOB")
                    elif (index + 2) == len(testing_list):
                        insertInSymbolTable(symbolTable, testing_list[index+1][0],
                                            "NOOB", "NOOB")

            # Variable assignment (I HAS A var ITZ literal)
            if (i[0] == "I HAS A" and (index+3) < len(testing_list)):
                if testing_list[index+1][1] == "Variable Identifier" and testing_list[index+2][0] == "ITZ" and testing_list[index+3][1] in datatypes_arr:
                    insertInSymbolTable(
                        symbolTable, testing_list[index+1][0], testing_list[index+3][0], testing_list[index+3][1])

            # Variable assignment (I HAS A var ITZ variable)
            if (i[0] == "I HAS A" and (index+3) < len(testing_list)):
                if testing_list[index+1][1] == "Variable Identifier" and testing_list[index+2][0] == "ITZ" and testing_list[index+3][1] == "Variable Identifier":
                    value = findValue(symbolTable, testing_list[index+3][0])

                    if value != False:
                        insertInSymbolTable(
                            symbolTable, testing_list[index+1][0], value[0], value[1])
                    else:
                        error_prompt = "SemanticsError: variable identifier \'" + \
                            testing_list[index+3][0] + "\' is not defined"
                        print(error_prompt)  # temp
                        return [False, error_prompt, symbolTable, output_arr]

            # Variable assignment (I HAS A var ITZ expr)
            if i[0] == "I HAS A" and testing_list[index+1][1] == "Variable Identifier" and testing_list[index+2][0] == "ITZ":
                to_eval_list = []

                if testing_list[index+3][0] in operations_arr:
                    # find the index of the line break
                    start_index = index + 3
                    j = start_index
                    while testing_list[j][1] != 'linebreak':
                        j = j + 1

                    # get that portion of line then evaluate until only
                    to_eval_list = testing_list[start_index: j]
                    print("----Eval----")
                    print(to_eval_list)
                    print("------------")

                    # replace all variabes first
                    for index, i in enumerate(to_eval_list):
                        if i[1] == "Variable Identifier":
                            value = findValue(
                                symbolTable, to_eval_list[index][0])

                            if value != False:
                                del to_eval_list[index]
                                to_eval_list.insert(index, value)
                            else:
                                error_prompt = "SemanticsError: variable identifier \'" + \
                                    to_eval_list[index][0] + \
                                    "\' is not defined"
                                print(error_prompt)  # temp
                                return [False, error_prompt, symbolTable, output_arr]

                    # evaluate expressions
                    while (True):
                        change1 = False
                        for index, i in enumerate(to_eval_list):
                            if i[0] == "NOT" and (index + 1) < len(to_eval_list):
                                if to_eval_list[index+1][1] in datatypes_arr:
                                    evaluated = boolean_not(
                                        to_eval_list[index+1][0], to_eval_list[index+1][1])

                                    if evaluated[0] != False:
                                        del to_eval_list[(index):(index+2)]
                                        print("---Before-----")
                                        print(to_eval_list)
                                        to_eval_list.insert(
                                            index, evaluated[1:3])
                                        print("---After-----")
                                        print(to_eval_list)
                                        change1 = True
                                    else:
                                        output_arr.append(evaluated[1])
                                        return [False, error_prompt, symbolTable, output_arr]

                            if i[0] in operations_arr and (index + 3) < len(to_eval_list):
                                if to_eval_list[index+1][1] in datatypes_arr and to_eval_list[index+2][0] == "AN" and to_eval_list[index+3][1] in datatypes_arr:
                                    # call function that accepts value1, type1, value2, type2 and operation

                                    if i[0] in arithmetic_arr:  # check if to peform arithmetic
                                        evaluated = arithmetic_op(
                                            to_eval_list[index+1][0], to_eval_list[index+1][1], to_eval_list[index+3][0], to_eval_list[index+3][1], i[0])
                                    elif i[0] in comparison_arr:  # check if to perform comparison
                                        evaluated = comparison_op(
                                            to_eval_list[index+1][0], to_eval_list[index+1][1], to_eval_list[index+3][0], to_eval_list[index+3][1], i[0])
                                    elif i[0] in boolean_arr:  # check if to perform boolean
                                        evaluated = boolean_op(
                                            to_eval_list[index+1][0], to_eval_list[index+1][1], to_eval_list[index+3][0], to_eval_list[index+3][1], i[0])

                                        print(evaluated)

                                    if evaluated[0] != False:
                                        del to_eval_list[(index):(index+4)]
                                        to_eval_list.insert(
                                            index, evaluated[1:3])
                                        change1 = True
                                    else:
                                        output_arr.append(evaluated[1])
                                        return [False, error_prompt, symbolTable, output_arr]

                        if (change1 == False):
                            print("Done evaluating!")
                            print("----Before-----")
                            print(testing_list)

                            print("----After-----")
                            del testing_list[start_index: j]
                            testing_list.insert(start_index, to_eval_list[0])
                            insertInSymbolTable(
                                symbolTable, testing_list[start_index-2][0], to_eval_list[0][0], to_eval_list[0][1])
                            print(testing_list)
                            print("-------------")
                            break

            # User input
            if i[0] == "GIMMEH" and (index + 1) < len(testing_list):
                if testing_list[index+1][1] == "Variable Identifier":
                    value = get_input(testing_list[index+1][0])

                    insertInSymbolTable(
                        symbolTable, testing_list[index+1][0], value[0], value[1])

            # User output (VISIBLE literal and single string)
            if i[0] == "VISIBLE" and index + 2 < len(testing_list):
                # Case 1: Visible Literal/String
                if testing_list[index+1][1] in datatypes_arr and testing_list[index+2][0] != "AN":
                    output_arr.append(testing_list[index+1][0])
                    # insertInSymbolTable(
                    #     symbolTable, "IT", testing_list[index+1][0], testing_list[index+1][1])

                # Case 2: VISIBLE variable only
                if testing_list[index+1][1] == "Variable Identifier" and testing_list[index+2][0] != "AN":
                    value = findValue(symbolTable, testing_list[index+1][0])

                    if value != False:
                        output_arr.append(value[0])
                        # insertInSymbolTable(
                        #     symbolTable, "IT", value[0], value[1])

                    else:
                        error_prompt = "SemanticsError: variable identifier \'" + \
                            to_eval_list[index][0] + "\' is not defined"
                        print(error_prompt)  # temp
                        return [False, error_prompt, symbolTable, output_arr]
            # Case 3: VISIBLE expression
            if i[0] == "VISIBLE" and testing_list[index+1][0] in operations_arr:
                start_index = index + 1  # evaluation from lexeme after visible until before line break
                j = start_index
                while testing_list[j][1] != 'linebreak':
                    j = j + 1

                to_eval_list = testing_list[start_index: j]
                print("----Visible Expr Eval----")
                print(to_eval_list)
                print("-------------------------")

                # replace all variabes first
                for index, i in enumerate(to_eval_list):
                    if i[1] == "Variable Identifier":
                        value = findValue(
                            symbolTable, to_eval_list[index][0])

                        if value != False:
                            del to_eval_list[index]
                            to_eval_list.insert(index, value)
                        else:
                            error_prompt = "SemanticsError: variable identifier \'" + \
                                to_eval_list[index][0] + \
                                "\' is not defined"
                            print(error_prompt)  # temp
                            return [False, error_prompt, symbolTable, output_arr]

                # evaluate
                while (True):
                    change1 = False
                    for index, i in enumerate(to_eval_list):
                        if i[0] == "NOT" and (index + 1) < len(to_eval_list):
                            if to_eval_list[index+1][1] in datatypes_arr:
                                evaluated = boolean_not(
                                    to_eval_list[index+1][0], to_eval_list[index+1][1])

                                if evaluated[0] != False:
                                    del to_eval_list[(index):(index+2)]
                                    print("---Before-----")
                                    print(to_eval_list)
                                    to_eval_list.insert(
                                        index, evaluated[1:3])
                                    print("---After-----")
                                    print(to_eval_list)
                                    change1 = True
                                else:
                                    output_arr.append(evaluated[1])
                                    return [False, error_prompt, symbolTable, output_arr]

                        if i[0] in operations_arr and (index + 3) < len(to_eval_list):
                            if to_eval_list[index+1][1] in datatypes_arr and to_eval_list[index+2][0] == "AN" and to_eval_list[index+3][1] in datatypes_arr:
                                # call function that accepts value1, type1, value2, type2 and operation

                                if i[0] in arithmetic_arr:  # check if to peform arithmetic
                                    evaluated = arithmetic_op(
                                        to_eval_list[index+1][0], to_eval_list[index+1][1], to_eval_list[index+3][0], to_eval_list[index+3][1], i[0])
                                elif i[0] in comparison_arr:  # check if to perform comparison
                                    evaluated = comparison_op(
                                        to_eval_list[index+1][0], to_eval_list[index+1][1], to_eval_list[index+3][0], to_eval_list[index+3][1], i[0])
                                elif i[0] in boolean_arr:  # check if to perform boolean
                                    evaluated = boolean_op(
                                        to_eval_list[index+1][0], to_eval_list[index+1][1], to_eval_list[index+3][0], to_eval_list[index+3][1], i[0])

                                    print(evaluated)

                                if evaluated[0] != False:
                                    del to_eval_list[(index):(index+4)]
                                    to_eval_list.insert(
                                        index, evaluated[1:3])

                                    change1 = True
                                else:
                                    output_arr.append(evaluated[1])
                                    return [False, error_prompt, symbolTable, output_arr]

                    if (change1 == False):
                        print("Done evaluating!")
                        print("----Before-----")
                        print(testing_list)

                        print("----After-----")
                        del testing_list[start_index: j]
                        testing_list.insert(start_index, to_eval_list[0])

                        output_arr.append(to_eval_list[0][0])
                        # insertInSymbolTable(
                        #     symbolTable, "IT", to_eval_list[0][0], to_eval_list[0][1])
                        print(testing_list)
                        print("-------------")
                        break
            # Case 4: VISIBLE Strings
            if i[0] == "VISIBLE" and (index + 2) < len(testing_list):
                if testing_list[index+1][0] == "SMOOSH" and testing_list[index+2][1] in datatypes_arr:
                    start_index = index + 2  # evaluation from lexeme after visible until before line break
                    j = start_index
                    while testing_list[j][1] != 'linebreak':
                        j = j + 1

                    to_eval_list = testing_list[start_index: j]
                    print("----Smoosh Expr Eval----")
                    print(to_eval_list)
                    print("-------------------------")

                    # replace all variabes first
                    for index, i in enumerate(to_eval_list):
                        if i[1] == "Variable Identifier":
                            value = findValue(
                                symbolTable, to_eval_list[index][0])

                            if value != False:
                                del to_eval_list[index]
                                to_eval_list.insert(index, value)
                            else:
                                error_prompt = "SemanticsError: variable identifier \'" + \
                                    to_eval_list[index][0] + \
                                    "\' is not defined"
                                print(error_prompt)  # temp
                                return [False, error_prompt, symbolTable, output_arr]

                        # smoosh
                        concatenated = smoosh(datatypes_arr, to_eval_list)
                        # insertInSymbolTable(symbolTable, "IT",
                        #                     concatenated[0], concatenated[1])
                        output_arr.append(concatenated[0])

            # SMOOSH (Format: SMOOSH str1 AN str2 AN ... AN strN)
            if i[0] == "SMOOSH":
                if testing_list[index+1][1] in datatypes_arr:
                    start_index = index + 1  # evaluation from lexeme after visible until before line break
                    j = start_index
                    while testing_list[j][1] != 'linebreak':
                        j = j + 1

                    to_eval_list = testing_list[start_index: j]
                    print("----Smoosh Expr Eval----")
                    print(to_eval_list)
                    print("-------------------------")

                    # replace all variabes first
                    for index, i in enumerate(to_eval_list):
                        if i[1] == "Variable Identifier":
                            value = findValue(
                                symbolTable, to_eval_list[index][0])

                            if value != False:
                                del to_eval_list[index]
                                to_eval_list.insert(index, value)
                            else:
                                error_prompt = "SemanticsError: variable identifier \'" + \
                                    to_eval_list[index][0] + \
                                    "\' is not defined"
                                print(error_prompt)  # temp
                                return [False, error_prompt, symbolTable, output_arr]

                    # smoosh
                    concatenated = smoosh(datatypes_arr, to_eval_list)
                    print(concatenated)

            # Typecasting: Explicit Typecasting
            if i[0] == "MAEK" and (index + 2) < len(testing_list):
                if testing_list[index+1][1] == "Variable Identifier" and testing_list[index+2][1] == "TYPE Literal":
                    prevVal = findValue(symbolTable, testing_list[index+1][0])

                    if prevVal != False:
                        newValue = typecast(
                            prevVal[0], prevVal[1], testing_list[index+2][0])
                        print(newValue)

                        if newValue[0] != False:
                            insertInSymbolTable(
                                symbolTable, "IT", newValue[1], newValue[2])
                        else:
                            error_prompt = newValue[1]
                            return [False, error_prompt, symbolTable, output_arr]
                    else:
                        error_prompt = "SemanticsError: variable identifier \'" + \
                            testing_list[index+1][0] + "\' is not defined"
                        print(error_prompt)  # temp
                        return [False, error_prompt, symbolTable, output_arr]

            # Typecasting: Recasting
            if i[1] == "Variable Identifier" and (index + 2) < len(testing_list):
                if testing_list[index+1][0] == "IS NOW A" and testing_list[index+2][1] == "TYPE Literal":
                    value = findValue(symbolTable, i[0])

                    if value != False:
                        newValue = typecast(
                            value[0], value[1], testing_list[index+2][0])
                        print(newValue)

                        if newValue != False:
                            insertInSymbolTable(
                                symbolTable, i[0], newValue[1], newValue[2])
                        else:
                            error_prompt = newValue[1]
                            return [False, error_prompt, symbolTable, output_arr]
                    else:
                        error_prompt = "SemanticsError: variable identifier \'" + \
                            i[0] + "\' is not defined"
                        print(error_prompt)  # temp
                        return [False, error_prompt, symbolTable, output_arr]

            # Assignment statement (var R literal/variable) (Note: Left var can be uninitialized)
            if i[1] == "Variable Identifier" and (index + 2) < len(testing_list):
                # Case 1: var R literal
                if testing_list[index+1][0] == "R" and testing_list[index+2][1] in datatypes_arr:
                    insertInSymbolTable(
                        symbolTable, i[0], testing_list[index+2][0], testing_list[index+2][1])

                # Case 2: var R variable
                if testing_list[index+1][0] == "R" and testing_list[index+2][1] == "Variable Identifier":
                    value = findValue(symbolTable, testing_list[index+2][0])

                    if value != False:
                        insertInSymbolTable(
                            symbolTable, i[0], value[0], value[1])
                    else:
                        error_prompt = "SemanticsError: variable identifier \'" + \
                            to_eval_list[index][0] + "\' is not defined"
                        print(error_prompt)  # temp
                        return [False, error_prompt, symbolTable, output_arr]

            # Case 3: var R expr
            if i[1] == "Variable Identifier" and (index + 2) < len(testing_list):
                if testing_list[index+1][0] == "R" and testing_list[index+2][0] in operations_arr:
                    # find the index of the line break
                    start_index = index + 2
                    j = start_index
                    while testing_list[j][1] != 'linebreak':
                        j = j + 1

                    # get that portion of line then evaluate until only
                    to_eval_list = testing_list[start_index: j]
                    print("----Eval in Assignment----")
                    print(to_eval_list)
                    print("------------")

                    # replace all variabes first
                    for index, i in enumerate(to_eval_list):
                        if i[1] == "Variable Identifier":
                            value = findValue(
                                symbolTable, to_eval_list[index][0])

                            if value != False:
                                del to_eval_list[index]
                                to_eval_list.insert(index, value)
                            else:
                                error_prompt = "SemanticsError: variable identifier \'" + \
                                    to_eval_list[index][0] + \
                                    "\' is not defined"
                                print(error_prompt)  # temp
                                return [False, error_prompt, symbolTable, output_arr]

                    # evaluate expressions
                    while (True):
                        change1 = False
                        for index, i in enumerate(to_eval_list):
                            if i[0] == "NOT" and (index + 1) < len(to_eval_list):
                                if to_eval_list[index+1][1] in datatypes_arr:
                                    evaluated = boolean_not(
                                        to_eval_list[index+1][0], to_eval_list[index+1][1])

                                    if evaluated[0] != False:
                                        del to_eval_list[(index):(index+2)]
                                        print("---Before-----")
                                        print(to_eval_list)
                                        to_eval_list.insert(
                                            index, evaluated[1:3])
                                        print("---After-----")
                                        print(to_eval_list)
                                        change1 = True
                                    else:
                                        output_arr.append(evaluated[1])
                                        return [False, error_prompt, symbolTable, output_arr]

                            if i[0] in operations_arr and (index + 3) < len(to_eval_list):
                                if to_eval_list[index+1][1] in datatypes_arr and to_eval_list[index+2][0] == "AN" and to_eval_list[index+3][1] in datatypes_arr:
                                    # call function that accepts value1, type1, value2, type2 and operation

                                    if i[0] in arithmetic_arr:  # check if to peform arithmetic
                                        evaluated = arithmetic_op(
                                            to_eval_list[index+1][0], to_eval_list[index+1][1], to_eval_list[index+3][0], to_eval_list[index+3][1], i[0])
                                    elif i[0] in comparison_arr:  # check if to perform comparison
                                        evaluated = comparison_op(
                                            to_eval_list[index+1][0], to_eval_list[index+1][1], to_eval_list[index+3][0], to_eval_list[index+3][1], i[0])
                                    elif i[0] in boolean_arr:  # check if to perform boolean
                                        evaluated = boolean_op(
                                            to_eval_list[index+1][0], to_eval_list[index+1][1], to_eval_list[index+3][0], to_eval_list[index+3][1], i[0])

                                        print(evaluated)

                                    if evaluated[0] != False:
                                        del to_eval_list[(index):(index+4)]
                                        to_eval_list.insert(
                                            index, evaluated[1:3])
                                        change1 = True
                                    else:
                                        output_arr.append(evaluated[1])
                                        return [False, error_prompt, symbolTable, output_arr]

                        if (change1 == False):
                            print("Done evaluating!")
                            print("----Before-----")
                            print(testing_list)

                            print("----After-----")
                            del testing_list[start_index: j]
                            testing_list.insert(start_index, to_eval_list[0])
                            insertInSymbolTable(
                                symbolTable, testing_list[start_index-2][0], to_eval_list[0][0], to_eval_list[0][1])
                            print(testing_list)
                            print("-------------")
                            break

            # Case 4: var R smoosh
            if i[1] == "Variable Identifier" and (index + 3) < len(testing_list):
                if testing_list[index+1][0] == "R" and testing_list[index+2][0] == "SMOOSH" and (testing_list[index+3][1] in datatypes_arr or testing_list[index+3][1] == "Variable Identifier"):

                    start_index = index + 3  # evaluation from lexeme after visible until before line break
                    j = start_index
                    while testing_list[j][1] != 'linebreak':
                        j = j + 1

                    to_eval_list = testing_list[start_index: j]
                    print("----Smoosh Expr Eval----")
                    print(to_eval_list)
                    print("-------------------------")

                    # replace all variabes first
                    for index, i in enumerate(to_eval_list):
                        if i[1] == "Variable Identifier":
                            value = findValue(
                                symbolTable, to_eval_list[index][0])

                            if value != False:
                                del to_eval_list[index]
                                to_eval_list.insert(index, value)
                            else:
                                error_prompt = "SemanticsError: variable identifier \'" + \
                                    to_eval_list[index][0] + \
                                    "\' is not defined"
                                print(error_prompt)  # temp
                                return [False, error_prompt, symbolTable, output_arr]

                        # smoosh (CONTINUE: Find cause of extra AN)
                        concatenated = smoosh(datatypes_arr, to_eval_list)
                        print("ASSIGNMENT SMOOSH")
                        insertInSymbolTable(symbolTable, i[0],
                                            concatenated[0], concatenated[1])

        if (change == False):
            print("Phase 2")
            break

    print(testing_list)
    print(symbolTable)

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
a = '''
I HAS A var ITZ SUM OF 5 AN 3
I HAS A num ITZ "123"
I HAS A sum ITZ SUM OF var AN 2
'''
k = "HAI I HAS A monde KTHXBYE"
n = '''HAI
I HAS A var ITZ 11
I HAS A var1 ITZ "123
var1 R var

SUM OF QUOSHUNT OF PRODUKT OF 3 AN 4 AN 2 AN 1

KTHXBYE
'''

g = """HAI
I HAS A var1 ITZ 12
MAEK var1 A NUMBAR
MAEK var1 YARN

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

# def grab_symbol_table1(lexemeArr):
#     testing_list = []
#     error_prompt = ""  # variale to be replaced with the error encountered
#     output_arr = []  # arr to hold all the strings to be output in terminal

#     # lexemes identifier
#     datatypes_arr = ["NUMBR Literal", "NUMBAR Literal",
#                      "YARN Literal", "TROOF Literal", "NOOB"]
#     arithmetic_op = ["SUM OF", "DIFF OF", "PRODUKT OF",
#                      "QUOSHUNT OF", "MOD OF", "BIGGR OF", "SMALLR OF"]

#     for i in lexemeArr:
#         testing_list.append(i)

#     for index, i in enumerate(testing_list):
#         # Variable initialization
#         if (i[0] == "I HAS A" and (index+1) < len(testing_list)):
#             if testing_list[index+1][1] == "Variable Identifier":
#                 if (index + 2) < len(testing_list):
#                     if testing_list[index+2][0] != "ITZ":
#                         insertToTable(testing_list, symbolTable,
#                                       index, "NOOB", testing_list[index+1][0], "NOOB")
#                 elif (index + 2) == len(testing_list):
#                     insertToTable(testing_list, symbolTable,
#                                   index, "NOOB", testing_list[index+1][0], "NOOB")

#         # Variable assignment (Case 1.1: Literal is NUMBR, NUMBAR, TROOF)
#         if (i[0] == "I HAS A" and (index+3) < len(testing_list)):
#             if (testing_list[index+1][1] == "Variable Identifier" and testing_list[index+2][0] == "ITZ"):
#                 if testing_list[index+3][1] in ["NUMBR Literal", "NUMBAR Literal", "TROOF Literal"]:
#                     insertToTable(testing_list, symbolTable,
#                                   index, testing_list[index+3][1], testing_list[index+1][0], testing_list[index+3][0])
#         # Variable assignment (Case 1.2: YARN Literal)
#         if (i[0] == "I HAS A" and (index+5) < len(testing_list)):
#             if (testing_list[index+1][1] == "Variable Identifier" and testing_list[index+2][0] == "ITZ"):
#                 if testing_list[index+3][1] == "String Delimiter" and testing_list[index+4][1] == "YARN Literal" and testing_list[index+5][1] == "String Delimiter":
#                     insertToTable(testing_list, symbolTable, index, testing_list[index+1][1],
#                                   testing_list[index+1][0], testing_list[index+4][0])
#         # Variable assignment (Case 1.3: Var Identifier)
#         if (i[0] == "I HAS A" and (index+3) < len(testing_list)):
#             if (testing_list[index+1][1] == "Variable Identifier" and testing_list[index+2][0] == "ITZ") and testing_list[index+3][1] == "Variable Identifier":
#                 new_value = findValue(symbolTable, testing_list[index+3][0])

#                 if new_value != False:  # if variable is not initialized
#                     insertToTable(testing_list, symbolTable, index, new_value[1],
#                                   testing_list[index+1][0], new_value[0])
#                 else:
#                     error_prompt = "SemanticsError: variable identifier \'" + \
#                         testing_list[index+3][0] + "\' is not defined"
#                     return [False, error_prompt, symbolTable, output_arr]

#         # Variable assignment (Case 1.4: Simple Expression)
#         if (i[0] == "I HAS A" and (index+5) < len(testing_list)):
#             if (testing_list[index+1][1] == "Variable Identifier" and testing_list[index+2][0] == "ITZ" and testing_list[index+3][0] in arithmetic_op):
#                 # Case 1: OPERATION literal AN literal
#                 if testing_list[index+4][1] in typecast_elig and testing_list[index+5][0] == "AN" and testing_list[index+6][1] in typecast_elig:
#                     result = typecast_compute(testing_list[index+4][0], testing_list[index+4][1],
#                                               testing_list[index+6][0], testing_list[index+6][1], testing_list[index+3][0])
#                     result_value = result[0]
#                     result_type = result[1]
#                     insertToTable(testing_list, symbolTable, index, result_type,
#                                   testing_list[index+1][0], result_value)
#                 # Case 2: OPERATION varident AN literal
#                 if testing_list[index+4][1] in "Variable Identifier" and testing_list[index+5][0] == "AN" and testing_list[index+6][1] in typecast_elig:

#                     new_value = findValue(
#                         symbolTable, testing_list[index+4][0])

#                     if new_value != False:  # if variable is initialized
#                         result = typecast_compute(new_value[0], new_value[1],
#                                                   testing_list[index+6][0], testing_list[index+6][1], testing_list[index+3][0])
#                         result_value = result[0]
#                         result_type = result[1]
#                         insertToTable(testing_list, symbolTable, index, result_type,
#                                       testing_list[index+1][0], result_value)
#                     else:
#                         error_prompt = "SemanticsError: variable identifier \'" + \
#                             testing_list[index+4][0] + "\' is not defined"
#                         return [False, error_prompt, symbolTable, output_arr]

#                 # Case 3: OPERATION literal AN varident
#                 if testing_list[index+4][1] in typecast_elig and testing_list[index+5][0] == "AN" and testing_list[index+6][1] == "Variable Identifier":
#                     new_value = findValue(
#                         symbolTable, testing_list[index+6][0])

#                     if new_value != False:  # if variable is initialized
#                         result = typecast_compute(
#                             testing_list[index+4][0], testing_list[index+4][1], new_value[0], new_value[1], testing_list[index+3][0])
#                         result_value = result[0]
#                         result_type = result[1]
#                         insertToTable(testing_list, symbolTable, index, result_type,
#                                       testing_list[index+1][0], result_value)
#                     else:
#                         error_prompt = "SemanticsError: variable identifier \'" + \
#                             testing_list[index+4][0] + "\' is not defined"
#                         return [False, error_prompt, symbolTable, output_arr]
#                 # Case 3: OPERATION varident AN varident
#                 if testing_list[index+4][1] == "Variable Identifier" and testing_list[index+5][0] == "AN" and testing_list[index+6][1] == "Variable Identifier":
#                     new_value1 = findValue(
#                         symbolTable, testing_list[index+4][0])
#                     new_value2 = findValue(
#                         symbolTable, testing_list[index+6][0])

#                     if new_value1 != False and new_value2 != False:  # if variable is initialized
#                         result = typecast_compute(
#                             new_value1[0], new_value1[1], new_value2[0], new_value2[1], testing_list[index+3][0])
#                         result_value = result[0]
#                         result_type = result[1]
#                         insertToTable(testing_list, symbolTable, index, result_type,
#                                       testing_list[index+1][0], result_value)
#                     elif new_value1 == False:
#                         error_prompt = "SemanticsError: variable identifier \'" + \
#                             testing_list[index+4][0] + "\' is not defined"
#                         return [False, error_prompt, symbolTable, output_arr]
#                     elif new_value2 == False:
#                         error_prompt = "SemanticsError: variable identifier \'" + \
#                             testing_list[index+6][0] + "\' is not defined"
#                         return [False, error_prompt, symbolTable, output_arr]

#         # Variable assignment (Case 1.5: Complex Expression)

#         # Assignment Statement R
#         if testing_list[index][1] == "Variable Identifier" and testing_list[index + 1][0] == "R":
#             # Case 1: Literal
#             if testing_list[index + 2][1] in typecast_elig:
#                 new_value = findValue(symbolTable, testing_list[index][0])
#                 if new_value != False:
#                     insertToTable(testing_list, symbolTable, index, testing_list[index + 2][1],
#                                   testing_list[index][0], testing_list[index + 2][0])

#                 else:  # if variable is not initialized
#                     error_prompt = "SemanticsError: variable identifier \'" + \
#                         testing_list[index][0] + "\' is not defined"
#                     return [False, error_prompt, symbolTable, output_arr]
#             # Case 2: Variable
#             if testing_list[index + 2][1] == "Variable Identifier":
#                 # check receiving variable
#                 new_value1 = findValue(symbolTable, testing_list[index][0])
#                 new_value2 = findValue(
#                     symbolTable, testing_list[index+2][0])  # check right side

#                 if new_value1 != False and new_value2 != False:
#                     insertToTable(testing_list, symbolTable, index, new_value2[1],
#                                   testing_list[index][0], new_value2[0])
#                     print_symbolTable(symbolTable)
#                 elif new_value1 != False:
#                     error_prompt = "SemanticsError: variable identifier \'" + \
#                         testing_list[index][0] + "\' is not defined"
#                     return [False, error_prompt, symbolTable, output_arr]
#                 elif new_value2 != False:  # if variable is not initialized
#                     error_prompt = "SemanticsError: variable identifier \'" + \
#                         testing_list[index+2][0] + "\' is not defined"
#                     return [False, error_prompt, symbolTable, output_arr]
#             # Case 3: Expression

#         # Visible for YARN Literal`````````````````
#         if i[0] == "VISIBLE" and (index+3) < len(testing_list):
#             if testing_list[index+1][1] == "String Delimiter" and testing_list[index+2][1] == "YARN Literal" and testing_list[index+3][1] == "String Delimiter":
#                 insertToTable(testing_list, symbolTable, index,
#                               'temp', 'IT', testing_list[index+2][0])

#                 # add output in terminal format
#                 output_arr.append(testing_list[index+2][0])

#         # Variable Case 1.1: VISIBLE varident format
#         if i[0] == "VISIBLE" and (index+1) < len(testing_list):
#             if testing_list[index+1][1] == "Variable Identifier":
#                 new_value = findValue(symbolTable, testing_list[index+1][0])

#                 if new_value != False:
#                     insertToTable(testing_list, symbolTable, index, new_value[1],
#                                   "IT", new_value[0])

#                     output_arr.append(new_value[0])
#                 else:  # if variable is not initialized
#                     error_prompt = "SemanticsError: variable identifier \'" + \
#                         testing_list[index+1][0] + "\' is not defined"
#                     return [False, error_prompt, symbolTable, output_arr]

#     return [True, error_prompt, symbolTable, output_arr]

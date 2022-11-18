# LOL Code Interpreter
# Author: Agsao, Coleen Therese & Tuazon, Andre (CMSC 124 - T1L)

import re
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import ttk

def validRE(pattern, string_input):
    x = re.match(pattern, string_input)
    if(x):
        return True
    else:
        return False


def what_lexeme(string_input):
    #keywords
    if (validRE("(^HAI$)|(^KTHXBYE$)", string_input)):
        return "Code Delimiter"
    elif (validRE("(^\"$)", string_input)):
        return "String Delimiter"
    elif (validRE("(^GIMMEH$)", string_input)):
        return "Input Keyword"
    elif (validRE("(^VISIBLE$)", string_input)):
        return "Output Keyword"

    #variables
    elif (validRE("(^I HAS A$)", string_input)):
        return "Variable Declaration"
    elif (validRE("(^ITZ$)", string_input)):
        return "Variable Assignment"

    #if-else
    elif (validRE("(^YA RLY$)|(^NO WAI$)", string_input)):
        return "Conditional Keyword"

    #operations

    #check literals
    elif(validRE("^-?\d+$", string_input)):
        return "NUMBR Literal"
    elif(validRE("(^-?\d+\.(\d)*$)|(^-?\d*\.(\d)+$)", string_input)):
        return "NUMBAR Literal"
    elif(validRE("^\"[^\"]*\"$", string_input)):
         return "YARN Literal"
    elif(validRE("(^WIN$)|(^FAIL$)", string_input)):
         return "TROOF Literal"
    elif(validRE("(^NUMBR$)|^NUMBAR$ |(^YARN$) |(^TROOF$)", string_input)):
         return "TYPE Literal"
    else:
        return "Keyword"
    

def lex_analyze():
    lexemeArr = [] #empty
    the_long_string = my_text.get("1.0", 'end-1c')
    lines = the_long_string.split("\n")

    twoWord = ["SUM", "DIFF", "PRODUKT", "QUOSHUNT", "MOD", "BIGGR", "SMALLR", "BOTH", "EITHER", "WON", "ANY", "ALL", "O", "YA", "NO"]
    twoWordLexemes = ["SUM OF", "DIFF OF", "PRODUKT OF", "QUOSHUNT OF", "MOD OF", "BIGGR OF", "SMALLR OF", "BOTH OF", "EITHER OF", "WON OF", "ANY OF", "ALL OF", "BOTH SAEM", "O RLY?", "YA RLY", "NO WAI"]

    threeWord = ["I", "IS", "IM"]
    threeWordLexemes = ["I HAS A", "IS NOW A", "IM IN YR", "IM OUTTA YR"]
    skipTwice = False
    skippedCount = 0
    skipOnce = False
    skipCount = 0
    tempString = ""

    #properly split
    for line in lines:
        line = re.sub("[\t]", "", line)     #remove the tab
        words = line.split(" ")
        for i, word in enumerate(words):
            #check for string
            if word[0] == "\"":
                lexemeArr.append("\"")
                tempString = word
                for j in range(i + 1, len(words)):

                    if words[j][-1] == "\"":
                        tempString = tempString + " " + words[j][0: len(words[j])]
                        lexemeArr.append(tempString)
                        lexemeArr.append("\"")
                        skipCount += 1
                        skippedCount = 0
                        break
                    else:
                        tempString = tempString + " " + words[j]  #print without "
                        skipCount += 1

            #find the element with " in the end
            # check for three-word lexemes
            if word in threeWord:
                temp = words[i] + " " + words[i + 1] + " " + words[i + 2]
                if temp in threeWordLexemes:
                    lexemeArr.append(temp)
                    skipTwice = True

            # check for two-word lexemes
            if word in twoWord:
                temp = words[i] + " " + words[i + 1]
                if temp in twoWordLexemes:
                    lexemeArr.append(temp)
                    skipOnce = True

            else:
                if skipTwice or skipOnce or skipCount != 0:

                    if (skippedCount == 2 and skipTwice):
                        skippedCount = 0
                        skipTwice= False

                    if (skippedCount == 1 and skipOnce):
                        skippedCount = 0
                        skipOnce = False

                    if (skippedCount == skipCount):
                        skippedCount = 0
                        skipCount = 0

                    skippedCount += 1

                else:
                    lexemeArr.append(word)


    #print(lexemeArr)
    for word in lexemeArr:
        if word == "\"":
            tv.insert('', 'end', text="1", values=(word, what_lexeme(word)))
        elif word[0] == "\"":
            tv.insert('', 'end', text="1", values=(word[1: len(word)-1], what_lexeme(word)))
        else:
            tv.insert('', 'end', text="1", values=(word, what_lexeme(word)))


lexemeArr = []


def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    label_fileExplorer.configure(text="File Opened: "+filename)

    #add reading here   
    # text_editor.insert(INSERT,"Bruh")


# GUI part

# Root Widget
root = Tk()                                                 #
root.title("LOLCode Interpreter (Lexical Analyzer)")
root.state("zoomed")
# root.geometry("1920x960")
# file_icon = PhotoImage(file="icon.png")



label_fileExplorer = Label(root, text="None", font=("Cascade Mono", 12), width=70, bg="white")
label_fileExplorer.grid(row=0,column=0, pady=5)

text_editor = Text(root, width="70", height="27", font=("Cascade Mono", 12), selectbackground = "gray", selectforeground="black", undo=True)
text_editor.grid(row=2, column=0, padx=10, pady=10)

label_fileExplorer_icon = Button(root, text="Open File", bg="white", width=90, command=browseFiles)
label_fileExplorer_icon.grid(row=1, column=0)

#Lexeme Table
lexeme_table_name = Label(root, text="Lexemes", font=("Cascade Mono", 12), pady=10)
lexeme_table_name.grid(row=1, column=1)

tv = ttk.Treeview(root, columns=("Lexemes","Classification", "Value"), show="headings", height="23")
tv.grid(row=2, column=1)
tv.column("# 1", anchor=CENTER)
tv.heading("# 1", text="Lexemes")
tv.column("# 2", anchor=CENTER)
tv.heading("# 2", text="Classification")
tv.column("# 3", anchor=CENTER)
tv.heading("# 3", text="Value")

#Symbol Table
symbol_table_name = Label(root, text="Symbol Table", font=("Cascade Mono", 12), pady=10, anchor=CENTER)
symbol_table_name.grid(row=1, column=2)

tv2 = ttk.Treeview(root, columns=("1","2", "3"), show="headings", height="23")
tv2.grid(row=2, column=2, padx="10")
tv2.column("# 1", anchor=CENTER)
tv2.heading("# 1", text="Identifier")
tv2.column("# 2", anchor=CENTER)
tv2.heading("# 2", text="Value")

execute_button = Button(root,text="execute",command=lex_analyze)
execute_button.grid(row=3, column=0, columnspan=3)

output = Text(root, width="208", height="20", font=("Cascade Mono", 12), selectbackground = "gray", selectforeground="black", undo=True, state=DISABLED)
output.grid(row=4, column=0, columnspan=3, padx=10, pady=5)


root.mainloop()
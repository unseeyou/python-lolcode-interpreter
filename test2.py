#Lexical Analyzer
import re
from tkinter import *
from tkinter import filedialog
from tkinter import font


def validRE(pattern, string_input):
    x = re.match(pattern, string_input)
    if(x):
        return True
    else:
        return False

def ender(test):
    test2 = []
    for i in test:
        if("\n" in i):
            test3 = i.split("\n")
            test2.append(test3[0])
            test2.append("\n")
            test2.append(test3[1])
        else:
            test2.append(i)
    test2.append("\n")
    return test2


def what_lexeme(string_input):
    if(validRE("^[A-Za-z]+[\w]*$", string_input)):
        return "variable_identifier"
    elif(validRE("^-?\d+$", string_input)):
        return "NUMBR_literal"
    # elif(validRE("(^-?\d+\.(\d)*$)|(^-?\d*\.(\d)+$)", string_input)):
    #     return "NUMBAR_literal"
    # elif(validRE("^-?\d+$", string_input)):
    #     return "NUMBR_literal"
    # elif(validRE("^-?\d+$", string_input)):
    #     return "NUMBR_literal"
    

def lex_analyze():
    the_long_string = my_text.get("1.0", 'end-1c')
    x = the_long_string.split("\n")
    print(x)
    # x = ender(x)
    
    # print(x)



# GUI part
root = Tk()
root.geometry("1200x660")

my_frame = Frame(root)
my_frame.pack(pady=5, side=LEFT)

my_text = Text(my_frame, width=50, height=25, font=("Helvetica", 16), selectbackground = "gray", selectforeground="black", undo=True)
my_text.pack(side=LEFT)

submit_button = Button(root,text="validate",command=lex_analyze)
submit_button.pack(side=RIGHT)

root.mainloop()
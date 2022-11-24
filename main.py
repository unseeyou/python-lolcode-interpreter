

# LOL Code Interpreter
# Author: Agsao, Coleen Therese & Tuazon, Andre (CMSC 124 - T1L)

import re
import grab_lexeme
import check_syntax
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import ttk

def lex_analyze(lexemeArr):
    lexemeArr.clear()

    the_long_string = text_editor.get("1.0", 'end-1c')
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

    for item in tv.get_children():
        tv.delete(item)

    for i in lexemeArr:
        tv.insert("", 'end', text="1", values=i)

    if(check_syntax.check_syntax(lexemeArr)):
        output.insert("end", "WIN\n")
    else:
        output.insert("end", "FAIL\n")









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
lexemeArr = []
# Root Widget
root = Tk()                                                 #
root.title("LOLCode Interpreter (Lexical Analyzer)")
root.state("zoomed")


label_fileExplorer = Label(root, text="None", font=("Cascade Mono", 12), width=70, bg="white")
label_fileExplorer.grid(row=0,column=0, pady=5)

text_editor = Text(root, width="70", height="27", font=("Cascade Mono", 12), selectbackground = "gray", selectforeground="black", undo=True)
text_editor.grid(row=2, column=0, padx=10, pady=10)

label_fileExplorer_icon = Button(root, text="Open File", bg="white", width=90, command=browseFiles)
label_fileExplorer_icon.grid(row=1, column=0)

#Lexeme Table
lexeme_table_name = Label(root, text="Lexemes", font=("Cascade Mono", 12), pady=10)
lexeme_table_name.grid(row=1, column=1)

table_width = "25"
tv = ttk.Treeview(root, columns=("Lexemes","Classification"), show="headings", height="23")
tv.grid(row=2, column=1)
tv.column("# 1", anchor=CENTER)
tv.heading("# 1", text="Lexemes")
tv.column("# 2", anchor=CENTER)
tv.heading("# 2", text="Classification")

#Symbol Table
symbol_table_name = Label(root, text="Symbol Table", font=("Cascade Mono", 12), pady=10, anchor=CENTER)
symbol_table_name.grid(row=1, column=2)

tv2 = ttk.Treeview(root, columns=("1","2"), show="headings", height="23")
tv2.grid(row=2, column=2, padx="10")
tv2.column("# 1", anchor=CENTER)
tv2.heading("# 1", text="Identifier")
tv2.column("# 2", anchor=CENTER)
tv2.heading("# 2", text="Value")

execute_button = Button(root,text="execute",command=lambda:lex_analyze(lexemeArr))
execute_button.grid(row=3, column=0, columnspan=3)

output = Text(root, width="208", height="20", font=("Cascade Mono", 12), selectbackground = "gray", selectforeground="black", undo=True)
output.grid(row=4, column=0, columnspan=3, padx=10, pady=5)


root.mainloop()
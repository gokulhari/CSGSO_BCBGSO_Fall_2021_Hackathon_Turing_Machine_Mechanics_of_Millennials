import cv2
import pytesseract
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk
import sys
import os
from antlr4 import *
import numpy as np
from eqSolverVisitor import eqSolverVisitor
from eqSolverListener import eqSolverListener
from eqSolverLexer import eqSolverLexer
from eqSolverParser import eqSolverParser
from MyeqSolverVisitor import MyeqSolverVisitor


class App:
    def __init__(self, root, msg):
        # setting title
        root.title("Editor")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GMessage_182 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_182["font"] = ft
        GMessage_182["fg"] = "#333333"
        GMessage_182["justify"] = "left"
        GMessage_182["text"] = msg
        GMessage_182.place(x=120, y=120, width=500, height=100)

        entry = Entry(root, width=50)
        entry.focus_set()
        entry.pack()

        ttk.Button(root, text="Done", width=20).pack(pady=20)


if __name__ == "__main__":
    img = cv2.imread('simpleEq.png')

    pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/Cellar/tesseract/4.1.1/bin/tesseract'
    # Adding custom options
    custom_config = r'--oem 3 --psm 6'
    result = pytesseract.image_to_string(img, config=custom_config)
    print(result)
    root = tk.Tk()
    app = App(root, result)
    root.mainloop()
    #eqns = open("input.txt").read()
    print("input: \n")
    print(result)
    lexer = eqSolverLexer(InputStream(result))
    stream = CommonTokenStream(lexer)
    parser = eqSolverParser(stream)
    tree = parser.program()
    statements = tree.statement()
    vv = MyeqSolverVisitor(len(statements))
    n = len(statements)
    matrix = np.zeros((n, n))
    vec = np.zeros((n, 1))
    eqno = 0
    for statement in statements:
        vv.visit(statement)
        for key, value in vv.dic.items():
            if key == "x":
                matrix[eqno, 0] = value
            elif key == "y":
                if vv.signs[0] == "+":
                    matrix[eqno, 1] = value
                elif vv.signs[0] == "-":
                    matrix[eqno, 1] = -value
        vec[eqno] = vv.vals
        eqno = eqno + 1

        vv.dict = dict()
        vv.signs = []
    print(matrix)
    print(vec)
    print("\n")
    sol = np.linalg.solve(matrix, vec)
    print(sol)

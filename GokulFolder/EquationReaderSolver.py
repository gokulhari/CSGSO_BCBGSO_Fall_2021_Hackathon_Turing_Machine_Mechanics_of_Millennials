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
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        self.msg = msg
        L1 = Label(root, text=msg)
        L1.pack(side = TOP)
        self.entry = Entry(root)
        self.entry.focus_set()
        self.entry.pack()
        ttk.Button(root, text="Done", command=self.getvalue, width=20).pack(pady=20)
    def getvalue(self):
        res = self.entry.get()
        root.destroy()
        if res != None:
            self.ret = res
        else:
            self.ret = self.msg
    


if __name__ == "__main__":
    os.chdir("/Users/gokul/Nok/Hackathon2021/CSGSO_BCBGSO_Fall_2021_Hackathon_Turing_Machine_Mechanics_of_Millennials/GokulFolder")
    img = cv2.imread('simpleEq2.png')

    pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
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

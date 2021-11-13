#!/usr/bin/env python3

import sys
import os
from antlr4 import *
import numpy as np 
from eqSolverVisitor import eqSolverVisitor
from eqSolverListener import eqSolverListener
from eqSolverLexer import eqSolverLexer
from eqSolverParser import eqSolverParser
from MyeqSolverVisitor import MyeqSolverVisitor

def main():
    os.chdir("/Users/gokul/Nok/Hackathon2021/CSGSO_BCBGSO_Fall_2021_Hackathon_Turing_Machine_Mechanics_of_Millennials/GokulFolder")
    eqns = open("input.txt").read()
    print("input: \n")
    lexer = eqSolverLexer(InputStream(eqns))
    stream = CommonTokenStream(lexer)
    parser = eqSolverParser(stream)
    tree = parser.program()
    statements = tree.statement()
    vv = MyeqSolverVisitor(len(statements))
    n = len(statements)
    matrix = np.zeros((n,n))
    vec = np.zeros((n,1))
    
    eqno = 0
    for statement in statements:
        vv.visit(statement)
        for key, value in vv.dic.items():
            if key == "x":
                matrix[eqno,0] = value        
            elif key == "y":
                if vv.signs[0] == "+":
                    matrix[eqno,1] = value
                elif vv.signs[0] == "-":
                    matrix[eqno, 1] = -value
        vec[eqno] = vv.vals
        eqno = eqno + 1
        
        vv.dict= dict()
        vv.signs = []
    print(matrix)
    print(vec)
    print("\n")
    sol = np.linalg.solve(matrix,vec)
    print(sol)
    

if __name__ == "__main__":
    main()   

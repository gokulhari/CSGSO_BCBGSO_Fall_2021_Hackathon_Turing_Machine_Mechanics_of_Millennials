#!/usr/bin/env python3

import sys
import os
from antlr4 import *
import numpy as np 
from eqSolverVisitor import eqSolverVisitor
from eqSolverListener import eqSolverListener
from eqSolverLexer import eqSolverLexer
from eqSolverParser import eqSolverParser


def main():
    os.chdir("/Users/gokul/Nok/Hackathon2021/CSGSO_BCBGSO_Fall_2021_Hackathon_Turing_Machine_Mechanics_of_Millennials/GokulFolder")
    eqns = open("input.txt").read()
    print("input: \n")
    lexer = eqSolverLexer(InputStream(eqns))
    stream = CommonTokenStream(lexer)
    parser = eqSolverParser(stream)
    tree = parser.program()
    statements = tree.statement()
    
    for statement in statements():
        print(statement[0].getText())
        print("\n")
    

if __name__ == "__main__":
    main()   

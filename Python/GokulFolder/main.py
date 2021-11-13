#!/usr/bin/env python3

import sys
from antlr4 import *
import numpy as np 
from eqSolverVisitor import eqSolverVisitor
from eqSolverListener import eqSolverListener
from eqSolverLexer import eqSolverLexer
from eqSolverParser import eqSolverParser


def main():
    eqns = open("input.txt").read()
    print("input: \n")
    lexer = eqSolverLexer(InputStream(eqns))
    stream = CommonTokenStream(lexer)
    parser = eqSolverParser(stream)
    tree = parser.program()
    statements = tree.statement()

    for statement in statements():
        print(statement.expr().getText())
        print("\n")
    

if __name__ == "__main__":
    main()   

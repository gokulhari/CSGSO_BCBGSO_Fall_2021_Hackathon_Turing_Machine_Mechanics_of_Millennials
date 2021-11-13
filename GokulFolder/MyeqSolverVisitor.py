from eqSolverVisitor import eqSolverVisitor
from eqSolverParser import eqSolverParser
import numpy as np
import sys
import math
import re


class MyeqSolverVisitor(eqSolverVisitor):
    def __init__(self, n = 0, matrix= 1, vector = 2):
        self.matrix = np.zeros((n,n))
        self.vector = np.zeros((n,1))
        self.dic = dict()
        self.eqnum = 0
        self.vals = 0
        self.signs = []
    def visitStatement(self, ctx: eqSolverParser.StatementContext):
        subs = ctx.expr()
        subs2 = subs[0].expr()
        self.vals = float(subs[1].getText())
        children = subs[0].children
        print(children[1].getText())
        self.signs.append(children[1].getText())
        print(subs2[0].getText())
        super().visit(subs2[0])
        super().visit(subs2[1])
        return 0
    
    def visitBuilding_exp(self, ctx: eqSolverParser.Building_expContext):
        subs = ctx.expr()
        children = subs[0].children
        print(children[1].getText())
        self.signs.append(children[1].getText())
        super().visit(subs[0])
        super().visit(subs[1])
        return 0

    
    def visitIden_exp(self, ctx: eqSolverParser.Iden_expContext):
        print(ctx.getText())
        out = re.split('(\d+)', ctx.getText())
        while '' in out:
            out.remove('')
        print(out)
        
        self.dic[out[1]] = float(out[0])
        
            
        return 0

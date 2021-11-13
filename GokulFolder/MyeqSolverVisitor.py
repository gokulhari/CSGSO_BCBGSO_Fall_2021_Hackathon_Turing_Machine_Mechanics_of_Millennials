from eqSolverVisitor import eqSolverVisitor
from eqSolverParser import eqSolverParser
import numpy as np
import sys
import math


class MyeqSolverVisitor(eqSolverVisitor):
    def visitStatement(self, ctx: eqSolverParser.StatementContext):
        subs = ctx.expr()
        print(subs[0].getText())
        print(subs[1].getText())
        subs2 = subs[0].expr()
        children = subs[0].children
        print(children[1].getText())
        if (children[1].getText() == "+"):
            
        return super().visitStatement(ctx)
    def visitBuilding_exp(self, ctx: eqSolverParser.Building_expContext):
        
        print(ctx.Sign.getText())
        if (subs[1].getText() == "+"):
            a = 2    
        return super().visitBuilding_exp(ctx)

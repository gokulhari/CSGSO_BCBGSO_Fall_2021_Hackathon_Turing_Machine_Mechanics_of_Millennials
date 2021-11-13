# Generated from eqSolver.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .eqSolverParser import eqSolverParser
else:
    from eqSolverParser import eqSolverParser

# This class defines a complete generic visitor for a parse tree produced by eqSolverParser.

class eqSolverVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by eqSolverParser#program.
    def visitProgram(self, ctx:eqSolverParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by eqSolverParser#statement.
    def visitStatement(self, ctx:eqSolverParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by eqSolverParser#building_exp.
    def visitBuilding_exp(self, ctx:eqSolverParser.Building_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by eqSolverParser#num_exp.
    def visitNum_exp(self, ctx:eqSolverParser.Num_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by eqSolverParser#paran_exp.
    def visitParan_exp(self, ctx:eqSolverParser.Paran_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by eqSolverParser#iden_exp.
    def visitIden_exp(self, ctx:eqSolverParser.Iden_expContext):
        return self.visitChildren(ctx)



del eqSolverParser
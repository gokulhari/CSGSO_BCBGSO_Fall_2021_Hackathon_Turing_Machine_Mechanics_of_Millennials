# Generated from eqSolver.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .eqSolverParser import eqSolverParser
else:
    from eqSolverParser import eqSolverParser

# This class defines a complete listener for a parse tree produced by eqSolverParser.
class eqSolverListener(ParseTreeListener):

    # Enter a parse tree produced by eqSolverParser#program.
    def enterProgram(self, ctx:eqSolverParser.ProgramContext):
        pass

    # Exit a parse tree produced by eqSolverParser#program.
    def exitProgram(self, ctx:eqSolverParser.ProgramContext):
        pass


    # Enter a parse tree produced by eqSolverParser#statement.
    def enterStatement(self, ctx:eqSolverParser.StatementContext):
        pass

    # Exit a parse tree produced by eqSolverParser#statement.
    def exitStatement(self, ctx:eqSolverParser.StatementContext):
        pass


    # Enter a parse tree produced by eqSolverParser#building_exp.
    def enterBuilding_exp(self, ctx:eqSolverParser.Building_expContext):
        pass

    # Exit a parse tree produced by eqSolverParser#building_exp.
    def exitBuilding_exp(self, ctx:eqSolverParser.Building_expContext):
        pass


    # Enter a parse tree produced by eqSolverParser#num_exp.
    def enterNum_exp(self, ctx:eqSolverParser.Num_expContext):
        pass

    # Exit a parse tree produced by eqSolverParser#num_exp.
    def exitNum_exp(self, ctx:eqSolverParser.Num_expContext):
        pass


    # Enter a parse tree produced by eqSolverParser#paran_exp.
    def enterParan_exp(self, ctx:eqSolverParser.Paran_expContext):
        pass

    # Exit a parse tree produced by eqSolverParser#paran_exp.
    def exitParan_exp(self, ctx:eqSolverParser.Paran_expContext):
        pass


    # Enter a parse tree produced by eqSolverParser#iden_exp.
    def enterIden_exp(self, ctx:eqSolverParser.Iden_expContext):
        pass

    # Exit a parse tree produced by eqSolverParser#iden_exp.
    def exitIden_exp(self, ctx:eqSolverParser.Iden_expContext):
        pass



del eqSolverParser
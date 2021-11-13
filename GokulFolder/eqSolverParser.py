# Generated from eqSolver.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("\'\4\2\t\2\4\3\t\3\4\4\t\4\3\2\7\2\n\n\2\f\2\16\2\r\13")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\5\4\35\n\4\3\4\3\4\3\4\7\4\"\n\4\f\4\16\4%\13\4\3")
        buf.write("\4\2\3\6\5\2\4\6\2\3\3\2\4\5\2\'\2\13\3\2\2\2\4\20\3\2")
        buf.write("\2\2\6\34\3\2\2\2\b\n\5\4\3\2\t\b\3\2\2\2\n\r\3\2\2\2")
        buf.write("\13\t\3\2\2\2\13\f\3\2\2\2\f\16\3\2\2\2\r\13\3\2\2\2\16")
        buf.write("\17\7\2\2\3\17\3\3\2\2\2\20\21\5\6\4\2\21\22\7\3\2\2\22")
        buf.write("\23\5\6\4\2\23\24\7\f\2\2\24\5\3\2\2\2\25\26\b\4\1\2\26")
        buf.write("\35\7\b\2\2\27\35\7\t\2\2\30\31\7\6\2\2\31\32\5\6\4\2")
        buf.write("\32\33\7\7\2\2\33\35\3\2\2\2\34\25\3\2\2\2\34\27\3\2\2")
        buf.write("\2\34\30\3\2\2\2\35#\3\2\2\2\36\37\f\6\2\2\37 \t\2\2\2")
        buf.write(" \"\5\6\4\7!\36\3\2\2\2\"%\3\2\2\2#!\3\2\2\2#$\3\2\2\2")
        buf.write("$\7\3\2\2\2%#\3\2\2\2\5\13\34#")
        return buf.getvalue()


class eqSolverParser ( Parser ):

    grammarFileName = "eqSolver.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "Identifier", "Number", 
                      "Comment", "WS", "NEWLINE" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expr = 2

    ruleNames =  [ "program", "statement", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    Identifier=6
    Number=7
    Comment=8
    WS=9
    NEWLINE=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(eqSolverParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(eqSolverParser.StatementContext)
            else:
                return self.getTypedRuleContext(eqSolverParser.StatementContext,i)


        def getRuleIndex(self):
            return eqSolverParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = eqSolverParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << eqSolverParser.T__3) | (1 << eqSolverParser.Identifier) | (1 << eqSolverParser.Number))) != 0):
                self.state = 6
                self.statement()
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 12
            self.match(eqSolverParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(eqSolverParser.ExprContext)
            else:
                return self.getTypedRuleContext(eqSolverParser.ExprContext,i)


        def NEWLINE(self):
            return self.getToken(eqSolverParser.NEWLINE, 0)

        def getRuleIndex(self):
            return eqSolverParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = eqSolverParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.expr(0)
            self.state = 15
            self.match(eqSolverParser.T__0)
            self.state = 16
            self.expr(0)
            self.state = 17
            self.match(eqSolverParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return eqSolverParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Building_expContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a eqSolverParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(eqSolverParser.ExprContext)
            else:
                return self.getTypedRuleContext(eqSolverParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuilding_exp" ):
                listener.enterBuilding_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuilding_exp" ):
                listener.exitBuilding_exp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBuilding_exp" ):
                return visitor.visitBuilding_exp(self)
            else:
                return visitor.visitChildren(self)


    class Num_expContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a eqSolverParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Number(self):
            return self.getToken(eqSolverParser.Number, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum_exp" ):
                listener.enterNum_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum_exp" ):
                listener.exitNum_exp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum_exp" ):
                return visitor.visitNum_exp(self)
            else:
                return visitor.visitChildren(self)


    class Paran_expContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a eqSolverParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(eqSolverParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParan_exp" ):
                listener.enterParan_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParan_exp" ):
                listener.exitParan_exp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParan_exp" ):
                return visitor.visitParan_exp(self)
            else:
                return visitor.visitChildren(self)


    class Iden_expContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a eqSolverParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(eqSolverParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIden_exp" ):
                listener.enterIden_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIden_exp" ):
                listener.exitIden_exp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIden_exp" ):
                return visitor.visitIden_exp(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = eqSolverParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [eqSolverParser.Identifier]:
                localctx = eqSolverParser.Iden_expContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 20
                self.match(eqSolverParser.Identifier)
                pass
            elif token in [eqSolverParser.Number]:
                localctx = eqSolverParser.Num_expContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 21
                self.match(eqSolverParser.Number)
                pass
            elif token in [eqSolverParser.T__3]:
                localctx = eqSolverParser.Paran_expContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.match(eqSolverParser.T__3)
                self.state = 23
                self.expr(0)
                self.state = 24
                self.match(eqSolverParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 33
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = eqSolverParser.Building_expContext(self, eqSolverParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 28
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 29
                    _la = self._input.LA(1)
                    if not(_la==eqSolverParser.T__1 or _la==eqSolverParser.T__2):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 30
                    self.expr(5) 
                self.state = 35
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         





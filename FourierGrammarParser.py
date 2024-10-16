# Generated from FourierGrammar.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,59,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,22,8,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,5,1,36,8,1,10,1,12,1,39,9,1,1,2,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,1,3,5,3,50,8,3,10,3,12,3,53,9,3,1,3,1,3,1,4,
        1,4,1,4,0,1,2,5,0,2,4,6,8,0,1,1,0,11,12,61,0,10,1,0,0,0,2,21,1,0,
        0,0,4,40,1,0,0,0,6,45,1,0,0,0,8,56,1,0,0,0,10,11,3,2,1,0,11,12,5,
        0,0,1,12,1,1,0,0,0,13,14,6,1,-1,0,14,22,3,4,2,0,15,16,5,1,0,0,16,
        17,3,2,1,0,17,18,5,2,0,0,18,22,1,0,0,0,19,22,5,11,0,0,20,22,5,12,
        0,0,21,13,1,0,0,0,21,15,1,0,0,0,21,19,1,0,0,0,21,20,1,0,0,0,22,37,
        1,0,0,0,23,24,10,6,0,0,24,25,5,3,0,0,25,36,3,2,1,7,26,27,10,5,0,
        0,27,28,5,4,0,0,28,36,3,2,1,6,29,30,10,4,0,0,30,31,5,5,0,0,31,36,
        3,2,1,5,32,33,10,3,0,0,33,34,5,6,0,0,34,36,3,2,1,4,35,23,1,0,0,0,
        35,26,1,0,0,0,35,29,1,0,0,0,35,32,1,0,0,0,36,39,1,0,0,0,37,35,1,
        0,0,0,37,38,1,0,0,0,38,3,1,0,0,0,39,37,1,0,0,0,40,41,5,7,0,0,41,
        42,5,1,0,0,42,43,3,6,3,0,43,44,5,2,0,0,44,5,1,0,0,0,45,46,5,8,0,
        0,46,51,3,8,4,0,47,48,5,9,0,0,48,50,3,8,4,0,49,47,1,0,0,0,50,53,
        1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,
        54,55,5,10,0,0,55,7,1,0,0,0,56,57,7,0,0,0,57,9,1,0,0,0,4,21,35,37,
        51
    ]

class FourierGrammarParser ( Parser ):

    grammarFileName = "FourierGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'+'", "'-'", "'*'", "'/'", 
                     "'Fourier'", "'['", "','", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUMBER", "COMPLEX_NUMBER", 
                      "WS" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_fourierTransform = 2
    RULE_list = 3
    RULE_element = 4

    ruleNames =  [ "program", "expression", "fourierTransform", "list", 
                   "element" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    NUMBER=11
    COMPLEX_NUMBER=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(FourierGrammarParser.ExpressionContext,0)


        def EOF(self):
            return self.getToken(FourierGrammarParser.EOF, 0)

        def getRuleIndex(self):
            return FourierGrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = FourierGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.expression(0)
            self.state = 11
            self.match(FourierGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fourierTransform(self):
            return self.getTypedRuleContext(FourierGrammarParser.FourierTransformContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FourierGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FourierGrammarParser.ExpressionContext,i)


        def NUMBER(self):
            return self.getToken(FourierGrammarParser.NUMBER, 0)

        def COMPLEX_NUMBER(self):
            return self.getToken(FourierGrammarParser.COMPLEX_NUMBER, 0)

        def getRuleIndex(self):
            return FourierGrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = FourierGrammarParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 14
                self.fourierTransform()
                pass
            elif token in [1]:
                self.state = 15
                self.match(FourierGrammarParser.T__0)
                self.state = 16
                self.expression(0)
                self.state = 17
                self.match(FourierGrammarParser.T__1)
                pass
            elif token in [11]:
                self.state = 19
                self.match(FourierGrammarParser.NUMBER)
                pass
            elif token in [12]:
                self.state = 20
                self.match(FourierGrammarParser.COMPLEX_NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 37
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 35
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = FourierGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 23
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 24
                        self.match(FourierGrammarParser.T__2)
                        self.state = 25
                        self.expression(7)
                        pass

                    elif la_ == 2:
                        localctx = FourierGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 26
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 27
                        self.match(FourierGrammarParser.T__3)
                        self.state = 28
                        self.expression(6)
                        pass

                    elif la_ == 3:
                        localctx = FourierGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 29
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 30
                        self.match(FourierGrammarParser.T__4)
                        self.state = 31
                        self.expression(5)
                        pass

                    elif la_ == 4:
                        localctx = FourierGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 32
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 33
                        self.match(FourierGrammarParser.T__5)
                        self.state = 34
                        self.expression(4)
                        pass

             
                self.state = 39
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FourierTransformContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_(self):
            return self.getTypedRuleContext(FourierGrammarParser.ListContext,0)


        def getRuleIndex(self):
            return FourierGrammarParser.RULE_fourierTransform

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFourierTransform" ):
                listener.enterFourierTransform(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFourierTransform" ):
                listener.exitFourierTransform(self)




    def fourierTransform(self):

        localctx = FourierGrammarParser.FourierTransformContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_fourierTransform)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(FourierGrammarParser.T__6)
            self.state = 41
            self.match(FourierGrammarParser.T__0)
            self.state = 42
            self.list_()
            self.state = 43
            self.match(FourierGrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FourierGrammarParser.ElementContext)
            else:
                return self.getTypedRuleContext(FourierGrammarParser.ElementContext,i)


        def getRuleIndex(self):
            return FourierGrammarParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)




    def list_(self):

        localctx = FourierGrammarParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(FourierGrammarParser.T__7)
            self.state = 46
            self.element()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 47
                self.match(FourierGrammarParser.T__8)
                self.state = 48
                self.element()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(FourierGrammarParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(FourierGrammarParser.NUMBER, 0)

        def COMPLEX_NUMBER(self):
            return self.getToken(FourierGrammarParser.COMPLEX_NUMBER, 0)

        def getRuleIndex(self):
            return FourierGrammarParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)




    def element(self):

        localctx = FourierGrammarParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         





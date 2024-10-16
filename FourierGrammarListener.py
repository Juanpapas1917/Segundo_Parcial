# Generated from FourierGrammar.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .FourierGrammarParser import FourierGrammarParser
else:
    from FourierGrammarParser import FourierGrammarParser

# This class defines a complete listener for a parse tree produced by FourierGrammarParser.
class FourierGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by FourierGrammarParser#program.
    def enterProgram(self, ctx:FourierGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by FourierGrammarParser#program.
    def exitProgram(self, ctx:FourierGrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by FourierGrammarParser#expression.
    def enterExpression(self, ctx:FourierGrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by FourierGrammarParser#expression.
    def exitExpression(self, ctx:FourierGrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by FourierGrammarParser#fourierTransform.
    def enterFourierTransform(self, ctx:FourierGrammarParser.FourierTransformContext):
        pass

    # Exit a parse tree produced by FourierGrammarParser#fourierTransform.
    def exitFourierTransform(self, ctx:FourierGrammarParser.FourierTransformContext):
        pass


    # Enter a parse tree produced by FourierGrammarParser#list.
    def enterList(self, ctx:FourierGrammarParser.ListContext):
        pass

    # Exit a parse tree produced by FourierGrammarParser#list.
    def exitList(self, ctx:FourierGrammarParser.ListContext):
        pass


    # Enter a parse tree produced by FourierGrammarParser#element.
    def enterElement(self, ctx:FourierGrammarParser.ElementContext):
        pass

    # Exit a parse tree produced by FourierGrammarParser#element.
    def exitElement(self, ctx:FourierGrammarParser.ElementContext):
        pass



del FourierGrammarParser
import sys
from antlr4 import *
from FourierGrammarLexer import FourierGrammarLexer
from FourierGrammarParser import FourierGrammarParser

def main():
    input_stream = InputStream(input("Ingresa una expresión: "))
    lexer = FourierGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FourierGrammarParser(stream)
    tree = parser.program()

    print("Árbol de parseo:", tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()

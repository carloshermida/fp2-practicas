#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Definición de la función para convertir
de infijo espaciado a postfijo.
"""

from stack import ArrayStack as Stack

def infixToPostfix(infixexpr):
    """Devuelve el postfijo de una expresión infija correctamente
    espaciada. Tiene en cuenta el orden de prioridades."""
    prec = {}
    prec["t"], prec["c"], prec["s"], prec["r"] = 5, 5, 5, 5
    prec["x"], prec["k"], prec["a"] = 5, 5, 5
    prec["**"] = 4
    prec["*"] , prec["/"] = 3, 3
    prec["+"] , prec["-"] = 2, 2
    prec["("] , prec["["], prec["{"] = 1, 1, 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split(" ")
    

    for token in tokenList:
        # Transformamos un número decimal por la fracción de denominador múltiplo de 10 correspondiente
        if "." in token:
            decimal_lista = token.split(".")
            divisor = ("1"+"0"*len(decimal_lista[1]))
            token = str(decimal_lista[0]+decimal_lista[1]+" "+divisor+" /")
            postfixList.append(token)
        else:
            if token.isnumeric():
                postfixList.append(token)
            elif token == '(' or token == '[' or token == '{':
                opStack.push(token)
            elif token == ')' or token == ']' or token == '}':
                topToken = opStack.pop()
                while topToken != '(' and topToken != '[' and topToken != '{':
                    postfixList.append(topToken)
                    topToken = opStack.pop() 
            else:
                while (not opStack.is_empty()) and (prec[opStack.peek()] >= prec[token]):
                    postfixList.append(opStack.pop())
                opStack.push(token)
    while not opStack.is_empty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)
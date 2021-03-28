#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practica 1
Carlos Hermida Clara Lado
Modulo Infijo a Postfijo
"""

from stack import ArrayStack as Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["t"], prec["c"], prec["s"], prec["r"] = 4, 4, 4, 4
    prec["*"] , prec["/"] = 3, 3
    prec["+"] , prec["-"] = 2, 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split(" ")
    

    for token in tokenList:
        if "." in token:
            decimal_lista = token.split(".")
            divisor = ("1"+"0"*len(decimal_lista[1]))
            token = str(decimal_lista[0]+decimal_lista[1]+" "+divisor+" /")
            postfixList.append(token)
        else:
            if token.isnumeric():
                postfixList.append(token)
            elif token == '(':
                opStack.push(token)
            elif token == ')':
                topToken = opStack.pop()
                while topToken != '(':
                    postfixList.append(topToken)
                    topToken = opStack.pop()
            else:
                while (not opStack.is_empty()) and (prec[opStack.peek()] >= prec[token]):
                    postfixList.append(opStack.pop())
                opStack.push(token)
    while not opStack.is_empty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)
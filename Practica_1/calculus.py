#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practica 1
Carlos Hermida Clara Lado
Modulo Calculos
"""

from writingcheck import espaciador, check_brackets
from itp import infixToPostfix
from stack import ArrayStack as Stack

def operador(op, num1, num2):
    if op == "+":
        resultado = num1 + num2
        return resultado
    
    elif op == "-":
        resultado = num1 - num2
        return resultado 
    
    elif op == "*":
        resultado = num1 * num2
        return resultado 
    
    elif op == "/":
        resultado = num1/num2
        return resultado
    
    elif op == "**":
        resultado = num1**num2
        return resultado 
    
    else:
        return "Operando no valido"

def iniciar(): 
    infijo = input("Introduce una expresion infija: ")
    
    if check_brackets(infijo):
        infijo = espaciador(infijo)
        if infijo != "ERROR":
            postfijo = infixToPostfix(infijo)
            lista_postfijo = postfijo.split(" ")
            simbolos = ["+", "-", "*", "/", "**"]
            pila = Stack()
    
            for item in lista_postfijo:
                pila.push(item)
                if item in simbolos:
                    op = pila.pop()
                    num2 = int(pila.pop())
                    num1 = int(pila.pop())
                    pila.push(int(operador(op, num1, num2)))
        
            return(pila.peek())
    
    return("Algo anda mal amigo")
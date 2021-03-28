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
from math import tan, sin, cos, sqrt, asin, acos, atan

def operador(op, num1, num2):
    if op == "+":
        return num1 + num2
    
    elif op == "-":
        return num1 - num2 
    
    elif op == "*":
        return num1 * num2 
    
    elif op == "/":
        return num1/num2
    
    elif op == "**":
        return num1**num2
    
    else:
        return "Operando no valido"

def operador_especial(op, num):
    if op == "t":
        return tan(num)
    
    elif op == "s":
        return sin(num)
    
    elif op == "c":
        return cos(num)
    
    elif op == "r":
        return sqrt(num)
    
    elif op == "x":
         return asin(num)

    elif op == "k":
         return acos(num)

    elif op == "a":
         return atan(num)

def iniciar(): 
    infijo = input("Introduce una expresion infija: ")
    
    if check_brackets(infijo):
        infijo = espaciador(infijo)
        if infijo != "ERROR":
            postfijo = infixToPostfix(infijo)
            print("POSTFIJO", "_"*(30-len("POSTFIJO")), postfijo)
            lista_postfijo = postfijo.split(" ")
            simbolos = ["+", "-", "*", "/", "**"]
            especial = ["t", "c", "s", "r", "x", "k", "a"]
            pila = Stack()
    
            for item in lista_postfijo:
                pila.push(item)
                if item in simbolos:
                    op = pila.pop()
                    num2 = float(pila.pop())
                    if op == "/" and num2 == 0:
                        return "ERROR"
                    num1 = float(pila.pop())
                    pila.push(float(operador(op, num1, num2)))
                
                if item in especial:
                    op = pila.pop()
                    num = float(pila.pop())
                    pila.push(float(operador_especial(op, num)))
        
            return(pila.peek())
    
    return("Algo anda mal amigo")
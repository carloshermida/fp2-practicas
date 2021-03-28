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
import math


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
                # comprueba si el elemento empieza por seno para poder identificarlo
                if (item.startswith("sin(") or item.startswith("sen(")) and item.endswith(")"):
                    # mira en que posicion esta el parentesis de cierre para que coja todo lo de dentro
                    posicion = item.index(")")
                    #se coje todo lo que esta entre ambos aprentesis
                    m = item[4:posicion]
                    # se le aplica la funcion a eso 
                    result = math.sin(m)
                    #cargamos el resultado en la pila
                    pila.push(result)
                elif item.startswith("cos(") and item.endswith(")"):
                    posicion = item.index(")")
                    m = item[4:posicion]
                    result = math.cos(m)
                    pila.push(result)
                elif (item.startswith("tan(") or item.startswith("tg(")) and item.endswith(")"):
                    posicion = item.index(")")
                    m = item[4:posicion]
                    result = math.tan(m)
                    pila.push(result)
                
                if item in simbolos:
                    op = pila.pop()
                    num2 = int(pila.pop())
                    if op == "/" and num2 == 0:
                        return "ERROR"
                    num1 = int(pila.pop())
                    pila.push(int(operador(op, num1, num2)))
        
            return(pila.peek())
    
    return("Algo anda mal amigo")
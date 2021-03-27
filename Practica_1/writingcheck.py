#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practica 1
Carlos Hermida Clara Lado
Modulo Comprobacion de escritura
"""

from itp import infixToPostfix
from stack import ArrayStack as Stack

def check_spaces(infijo):
    """ Función que comprueba la presencia de todos los especios necesarios para separar los caracteres  """
    total = len(infijo)
    caracteres = len(infijo.split())
    if total - caracteres == caracteres - 1:
        return True
    else:
        return False

def check_brackets(expr):
    """Return True if all delimiters are properly match; False otherwise."""
    lefty = '({['               # opening delimiters
    righty = ')}]'              # respective closing delims
    S = Stack()
    for c in expr:
        if c in lefty:
            S.push(c)           # push left delimiter on stack
        elif c in righty:
            if S.is_empty():
                return False    # nothing to match with
            if righty.index(c) != lefty.index(S.pop()):
                return False    # mismatched
    return S.is_empty()         # were all symbols matched?


# PROVISIONAL

def proximity_symbols(infijo):
    """ Función que revisa que los signos matemáticos esten bien puestos """
    simbolos = ["+", "-", "*", "/", "**"]
    infijo = infijo.split()
    if infijo[0] or infijo[-1] in simbolos:
        return False
    else:
        for simbolo in simbolos:
            postfijo = infixToPostfix(infijo)
            lista_postfijo = postfijo.split(" ")
            simbolos = ["+", "-", "*", "/", "**"]
            pila = Stack()
            a = 0
            b = 0
            for item in lista_postfijo:
                
                if item in simbolos:
                    b = a
                    a = item
                    if a == b:
                        return False
            return True
                   

def correct_division(infijo):
     """ Función encargada de """
     postfijo = infixToPostfix(infijo)
     lista_postfijo = postfijo.split(" ")
        
     pila = Stack()
    
     for item in lista_postfijo:
         pila.push(item)
         if item == 0:
             cero = int(pila.pop())
             elemento = pila.pop()
             if elemento == "/":
                 return False
         return True
     
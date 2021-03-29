#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Módulo Cálculos
# Carlos Hermida / Clara Lado

"""
Definición de las funciones encargadas de 
realizar los cálculos y de la función principal.
"""

from writingcheck import espaciador, check_brackets
from itp import infixToPostfix
from stack import ArrayStack as Stack
from math import tan, sin, cos, sqrt, asin, acos, atan

def operador(op, num1, num2):
    """Devuelve el resultado de operaciones matemáticas básicas siendo
    num1 y num2 los dos números y op el operador correspondiente."""
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

def operador_especial(op, num):
    """Devuelve el resultado de operaciones matemáticas avanzadas siendo
    num el número y op el código de operación definido en el manual de usuario."""
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
    """Pide al usuario introducir una expresión infija, y devuelve
    la expresión infija espaciada, la expresión postfija y el resultado
    la operación. En caso de un inadecuado uso del programa, devuelve
    el correspondiente error."""
    infijo = input("Introduce una expresión infija: ")
    
    if check_brackets(infijo):
        infijo = espaciador(infijo)
        # Si espaciador no detecta errores de escritura, continua
        
        if not infijo.startswith("ERROR"):
            # Convertimos el infijo espaciado a postfijo
            postfijo = infixToPostfix(infijo)
            print("POSTFIJO", "_"*(30-len("POSTFIJO")), postfijo)
            # Dividimos el postfijo por espacios
            lista_postfijo = postfijo.split(" ")
            simbolos = ["+", "-", "*", "/", "**"]
            especial = ["t", "c", "s", "r", "x", "k", "a"]
            pila = Stack()
    
            for item in lista_postfijo:
                # Añadimos todos los elementos a una pila
                pila.push(item)
                
                # Si es un símbolo, realizamos la operación deseada con los dos números anteriores
                if item in simbolos:
                    op = pila.pop()
                    num2 = float(pila.pop())
                    # En caso de división entre 0, devolvemos error
                    if op == "/" and num2 == 0:
                        return "ERROR / División entre cero"
                    num1 = float(pila.pop())
                    # Cargamos en la pila el resultado
                    pila.push(float(operador(op, num1, num2)))
                    
                # Si es un simbolo especial, realizamos la operación deseada con el número anterior
                if item in especial:
                    op = pila.pop()
                    num = float(pila.pop())
                    # Cargamos en la pila el resultado
                    pila.push(float(operador_especial(op, num)))
                
                # Si el simbolo pertenece a una operación no soportada, devolvemos error
                if not item.isnumeric() and item not in especial and item not in simbolos:
                    return("ERROR / Operación no soportada")
            
            # Devolvemos el resultado final
            return(pila.peek())
        
    else:
        # Devuelve el error de check_brackets
        return("ERROR / Delimitadores desemparejados")
    
    # Devuelve un error de espaciador
    return(infijo)
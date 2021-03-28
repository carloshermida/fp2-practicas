#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practica 1
Carlos Hermida Clara Lado
Modulo Comprobacion de escritura
"""

#from itp import infixToPostfix
from stack import ArrayStack as Stack

def espaciador(infijo: str) -> str:
    """Devuelve el infijo espaciado si esta correctamente escrito"""
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    delimitadores = ["(", ")", "{", "}", "[", "]"]
    simbolos = ["+", "-", "*", "/"]
    especial = ["t", "c", "s", "r"]
    pila = Stack()
    infijo_espaciado_pila = Stack()
    # Comprobamos que el primer elemento no sea un operador o espacio
    if infijo[0] not in numeros and infijo[0] not in delimitadores and infijo[0] not in especial:
        return "ERROR"
    # Cargamos todo en la pila
    for caracter in infijo:
        pila.push(caracter)
    
    ultimo = pila.peek()
    # Comprobamos que el ultimo elemento no sea un operador o espacio
    if ultimo in numeros or ultimo in delimitadores:
        while pila.__len__() != 1:
            anterior = pila.pop()
            infijo_espaciado_pila.push(anterior)
            infijo_espaciado_pila.push(" ")
            actual = pila.peek()
            
            if anterior in numeros and (actual not in numeros and actual not in simbolos and actual not in delimitadores and actual != "."):
                return "ERROR"
            
            elif anterior in ["(", "[", "{"] and (actual not in delimitadores and actual not in numeros and actual not in simbolos and actual not in especial):
                return "ERROR"
            
            elif anterior in [")", "]", "}"] and (actual not in delimitadores and actual not in numeros):
                return "ERROR"
            
            elif anterior in ["+", "-", "/"] and actual not in numeros and actual not in delimitadores:
                return "ERROR"
            
            elif anterior == "*" and actual not in numeros and actual != "*" and actual not in delimitadores:
                return "ERROR"
           
            elif anterior == "." and actual not in numeros:
                return "ERROR"
            
            elif anterior in especial and actual not in delimitadores and actual not in simbolos:
                return "ERROR"
            
            if anterior in numeros and (actual in numeros or actual == "."):
                infijo_espaciado_pila.pop()
            
            if anterior == "." and actual in numeros:
                infijo_espaciado_pila.pop()
            
            if anterior == "*" and actual == "*":
                infijo_espaciado_pila.pop()
            
            if anterior == "-" and actual == "(":
                infijo_espaciado_pila.push("0")
                infijo_espaciado_pila.push(" ")
             
             
        infijo_espaciado_pila.push(actual)
        infijo_espaciado_cadena = str("")
        while infijo_espaciado_pila.__len__() != 0:
            infijo_espaciado_cadena += str(infijo_espaciado_pila.pop())
        print("\nINFIJO", "_"*(30-len("INFIJO")), infijo_espaciado_cadena)
        return infijo_espaciado_cadena
    
    return "ERROR" 
   

def check_brackets(infijo):
    """Devuelve verdaero si los delimitadores estan bien emparejados"""
    lefty = '({['               # delimitadores abiertos
    righty = ')}]'              # delimitadores cerrados
    stack = Stack()
    for caracter in infijo:
        if caracter in lefty:
            stack.push(caracter)           # añade un delimitador abierto a la pila
        elif caracter in righty:
            if stack.is_empty():
                return False    # nada para emparejar
            if righty.index(caracter) != lefty.index(stack.pop()):
                return False    # desemparejado
    return stack.is_empty()     # devuleve verdadero si la pila esta vacia (todos emparejados)

 
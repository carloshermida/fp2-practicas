#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Definición de las funciones encargadas de 
verificar la correcta escritura del infijo.
"""

from stack import ArrayStack as Stack

def espaciador(infijo: str) -> str:
    """Devuelve el infijo espaciado si esta correctamente escrito."""
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    delimitadores = ["(", ")", "{", "}", "[", "]"]
    simbolos = ["+", "-", "*", "/"]
    especial = ["t", "c", "s", "r", "x", "k", "a"]
    pila = Stack()
    infijo_espaciado_pila = Stack()
    
    # Comprobamos que el primer elemento no sea un operador o espacio
    if infijo[0] not in numeros and infijo[0] not in delimitadores and infijo[0] not in especial:
        return "ERROR / Primer elemento es un operador, un espacio o un número (negativo o decimal) mal expresado"
    
    # Cargamos todo en la pila
    for caracter in infijo:
        pila.push(caracter)
    
    # Comprobamos que el ultimo elemento no sea un operador o espacio
    ultimo = pila.peek()
    if ultimo in numeros or ultimo in delimitadores:
        # Comporbamos que el infijo está bien escrito
        while pila.__len__() != 1:
            anterior = pila.pop()
            infijo_espaciado_pila.push(anterior)
            infijo_espaciado_pila.push(" ")
            actual = pila.peek()
            
            if anterior in numeros and (actual not in numeros and actual not in simbolos and actual not in delimitadores and actual != "."):
                return "ERROR / Espacios, caracteres no soportados o incorrecta escritura de operaciones especiales"
            
            elif anterior in ["(", "[", "{"] and (actual not in delimitadores and actual not in numeros and actual not in simbolos and actual not in especial):
                return "ERROR / Espacios o caracteres no soportados antes de un delimitador abierto"
            
            elif anterior in [")", "]", "}"] and (actual not in delimitadores and actual not in numeros):
                return "ERROR / Espacios, caracteres no soportados o operadores antes de un delimitador cerrado"
            
            elif anterior in ["+", "-", "/"] and actual not in numeros and actual not in delimitadores:
                return "ERROR / Espacios o caracteres no soportados antes de operadores o operadores duplicados"
            
            elif anterior == "*" and actual not in numeros and actual != "*" and actual not in delimitadores:
                return "ERROR / Espacios, caracteres no soportados o operador antes de multiplicación"
           
            elif anterior == "." and actual not in numeros:
                return "ERROR / Número decimal mal expresado o caracteres no soportados antes del punto"
            
            elif anterior in especial and actual not in ["(", "[", "{"] and actual not in simbolos:
                return "ERROR / Espacios, caracteres no soportados, números o delimitadores cerrados antes de operador especial"
            
            if anterior in numeros and (actual in numeros or actual == "."):
                infijo_espaciado_pila.pop()
            
            if anterior == "." and actual in numeros:
                infijo_espaciado_pila.pop()
            
            if anterior == "*" and actual == "*":
                infijo_espaciado_pila.pop()
            
            # Transformamos un número negativo por la resta de 0 - (el valor absoluto del número)
            if anterior == "-" and actual in ["(", "[", "{"]:
                infijo_espaciado_pila.push("0")
                infijo_espaciado_pila.push(" ")
             
        
        # Cargamos el último elemento
        infijo_espaciado_pila.push(actual)
        # Convertimos la pila en cadena
        infijo_espaciado_cadena = str("")
        while infijo_espaciado_pila.__len__() != 0:
            infijo_espaciado_cadena += str(infijo_espaciado_pila.pop())
        print("\nINFIJO", "_"*(30-len("INFIJO")), infijo_espaciado_cadena)
        return infijo_espaciado_cadena
    
    return "ERROR / Último elemento es un operador, un espacio o caracteres no soportados" 
   

def check_brackets(infijo):
    """Devuelve verdadero si los delimitadores estan bien emparejados."""
    lefty = '({['
    righty = ')}]'
    stack = Stack()
    for caracter in infijo:
        if caracter in lefty:
            # Añade un delimitador abierto a la pila
            stack.push(caracter)
        elif caracter in righty:
            if stack.is_empty():
                # Nada para emparejar
                return False
            if righty.index(caracter) != lefty.index(stack.pop()):
                 # Desemparejado
                return False
    return stack.is_empty()

 
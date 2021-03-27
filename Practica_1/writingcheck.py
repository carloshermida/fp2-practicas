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
    print("Pasa por la f espaciador")
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    delimitadores = ["(", ")", "{", "}", "[", "]"]
    simbolos = ["+", "-", "*", "/", "**"]
    
    #convierto infijo en una lista que separe todos los caraceres que la forman 
    cadena = infijo
    listainfijo = list(cadena)
    stack = Stack()
    
    # que el primer elemento sea o un numero o un delimitador
    primelem = listainfijo[0]
    if primelem not in numeros and primelem not in delimitadores:
        return "ERROR"
        print("2")
    infijo_espaciado_pila = Stack()
    
    # carga todo en la pila
    for caracter in listainfijo:
        stack.push(caracter)
    
    
    ultimo = stack.peek()
    # que el ultimo elemento no sea un operador o espacio
    if ultimo in numeros or ultimo in delimitadores:
        while True:
            anterior = stack.peek()
            infijo_espaciado_pila.push(anterior)
            stack.pop()
            if stack.is_empty:
                break
            infijo_espaciado_pila.push(" ")
            actual = stack.peek()
            
            if anterior in numeros and (actual not in numeros and actual not in simbolos and actual not in delimitadores):
                print("3")
                return "ERROR"
            
            elif anterior in delimitadores and (actual not in delimitadores and actual not in numeros):
                print("4")
                return "ERROR"
            
            elif anterior in ["+", "-", "*", "/"] and actual not in numeros:
                print("5")
                return "ERROR"
        
        infijo_espaciado_cadena = str("")
        while not infijo_espaciado_pila.is_empty:
            infijo_espaciado_cadena += str(infijo_espaciado_pila.pop())
        
        return infijo_espaciado_cadena
    print("6")
    return "ERROR" 
   

def check_brackets(infijo):
    """Devuelve verdaero si los delimitadores estan bien emparejados"""
    print("Pasa por la f check_brackets")
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
    return stack.is_empty()         # devuleve verdadero si la pila esta vacia (todos emparejados)

"""

def correct_division(infijo):
     Función encargada de
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
"""     
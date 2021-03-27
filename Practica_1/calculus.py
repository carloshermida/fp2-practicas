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
        print("Infijo: ",infijo)
        
        
        # ERROR     sale de la funcion espaciador vacio Y NI IDEA
        infijo2 = espaciador(infijo)
        
        
        
        print("Infijo2: ", infijo2)
        if infijo != "ERROR":
            postfijo = infixToPostfix(infijo2)
            lista_postfijo = postfijo.split(" ")
            simbolos = ["+", "-", "*", "/", "**"]
            pila = Stack()
            print("Pasa por aqqu")
            print(lista_postfijo)
            for item in lista_postfijo:
                pila.push(item)
                print("Pasa por aca")
                if item=="-" or item=="+" or item=="*" or item=="**" or item=="/":
                    op = pila.pop()
                    num2 = int(pila.pop())
                    if op == "/" and num2 == 0:
                        return "ERROR"
                    num1 = int(pila.pop())
                    pila.push(int(operador(op, num1, num2)))
                    print("Pasa por l")
            return(pila.peek())
        else:
            print("hAY UN PROBLEMA EN LA FUNCION ESPACIADOR")
        
    return("Algo anda mal amigo")
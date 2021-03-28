#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practica 1
Carlos Hermida Clara Lado
Main
"""

from calculus import iniciar

if __name__ == "__main__":
    
    print("*"*20, "CALCULADORA", "*"*30, "\n\n1) Iniciar\n2) Manual de usuario")
    opcion = int(input("> "))
    if opcion == 1:
        print("RESULTADO", "_"*(30-len("RESULTADO")), iniciar())
    elif opcion == 2:
        print("="*35, "\n", "\t\tManual de usuario", "\n", "="*35, "\n", sep="")
      
        # Manual de usuario:
        print("\
Para calcular el resultado de una expresión debe escribirla\n\
sin espacios.1")
   
    
    else:
        print("Opción no válida")
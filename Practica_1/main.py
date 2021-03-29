#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practica 1
Carlos Hermida Clara Lado
"""

from calculus import iniciar
from manual import mostrar_manual

if __name__ == "__main__":
    
    # Menú Principal
    print("*"*20, "CALCULADORA", "*"*30, "\n\n1) Iniciar\n2) Manual de usuario")
    opcion = int(input("> "))
    
    # Iniciar programa
    if opcion == 1:
        resultado = iniciar()
        if type(resultado) == float:
            print("RESULTADO", "_"*(30-len("RESULTADO")), resultado)
        else:
            print(resultado)
    
    # Manual de usuario
    elif opcion == 2:
        mostrar_manual()
    
    else:
        print("ERROR / Opción no válida")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Main
# Carlos Hermida / Clara Lado

"""
Código principal de la Práctica 1.
Contiene el menú principal.
"""

from calculus import iniciar
from manual import mostrar_manual

if __name__ == "__main__":
    
    # Menú Principal
    print("*"*20, "CALCULADORA", "*"*20, "\n\n1) Iniciar\n2) Manual de usuario")
    opcion = int(input("> "))
    
    # Iniciar el programa
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
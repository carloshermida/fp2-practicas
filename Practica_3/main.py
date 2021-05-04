#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Main
# Carlos Hermida / Clara Lado

"""
Código principal de la Práctica 3.
"""

from countries import country
import random 


def start():
    
    lista_paises = []
    ascii_code = 65
    
    for i in range(15):
        name = chr(ascii_code)
        globals()[name] = country(name) 
        ascii_code += 1
        lista_paises.append(name)
    
    return lista_paises
        


if __name__ == "__main__":
    
    print("CONCURSANTES: ")
    lista = start()
    print(lista)
    random.shuffle(lista)
    print(lista)
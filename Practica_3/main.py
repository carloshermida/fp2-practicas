#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Main
# Carlos Hermida / Clara Lado

"""
Código principal de la Práctica 3.
"""
#importo los módulos necesarios para trabajar
from countries import country
import random 
from ballot import votacion


def inicio_participantes():
    """Función que creara una lista de participantes"""
    #creamos una lista vacia donde se iran añadiendo los participantes de eurovision
    lista_paises = []
    ascii_code = 65
    #creamos un bucle que para que añada los participantes necesarios, como se nombraran letras sucesivas desde la A
    #hacemos que automaticamente vaya nombrandolos por defecto la siguiente letra
    for i in range(15):
        name = chr(ascii_code)
        globals()[name] = country(name)
        ascii_code += 1
        lista_paises.append(globals()[name])
    
    return lista_paises
        
def inicio_participantes_2():
    """Función que creara una lista de participantes"""
    
    lista_paises = ["España","Australia","Francia","Inglaterra","Portugal","Belgica","Israel","Suiza","Holanda","Chipre","Rusia","Montenegro","Bielorrusia","Noruega","Alemania"]
    for i in range(15):
        name = lista_paises[0]
        globals()[name] = country(name)
        lista_paises.append(globals()[name])
        lista_paises.pop(0)
    
    return lista_paises



if __name__ == "__main__":
    
    print("CONCURSANTES: ")
    lista = inicio_participantes_2()
    print(lista)
    print("RANDOM: ")
    random.shuffle(lista)
    print(lista)
    print("-"*30)
    votacion(lista)
    print("fin")
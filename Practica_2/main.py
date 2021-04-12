#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Main
# Carlos Hermida / Clara Lado

"""
Código principal de la Práctica 2.
"""

import sys
import array_queue
import random

def llegadadosis(x, y, z):
#"""
#Funcion encargada de dar un numero de vacunas de cada tipo
#"""
    #creo una cola vacia para cada vacuna, perdon no se crear colaas
    dosis_a = __init__() #para mayores de 70
    dosis_b = __init__() #para entre 50 y 70
    dosis_c = __init__() #para menores de 50
    #hago un bucle para que cada cola se llene del numero de vacunas llegadas
    for i in range(x):
        dosis_a.enqueue(1)

    for i in range(y):
        dosis_b.enqueue(1)
    
    for i in range(z):
        dosis_c.enqueue(1)

def personas(p):
   #intento crear una cola de personas con edades aleatorias
   
   a=random.randint(1, 100)

def seleccionadorvacuna(edad):
    #creo una funcion en la que se le introducira la edad de la persona y esta dira que vacuna le toca
    #el parametro a es la edad que estaria en la pila
    if edad < 50:
      dosis_c.dequeue()
      #elimino una vacuna de tipo c
    elif eda=>50 and edad<=70:
         dosis_b.dequeue()
    else:
         dosis_a.dequeue()
         
         
if __name__ == "__main__":
   
    print("sys: ", sys.argv)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Módulo Añadir
# Carlos Hermida / Clara Lado

"""
Definición de las funciones para añadir
vacunas, personas
"""
from array_queue import ArrayQueue as Queue
import random

dosis_a = Queue()
dosis_b = Queue()
dosis_c = Queue()
pacientes = Queue()

def llegadadosis(x, y, z, dosis_a, dosis_b, dosis_c):
    """Funcion encargada de dar un numero
    de vacunas de cada tipo."""
   
    #hago un bucle para que cada cola se llene del numero de vacunas llegadas
    for i in range(x):
        dosis_a.enqueue(1)

    for i in range(y):
        dosis_b.enqueue(1)
    
    for i in range(z):
        dosis_c.enqueue(1)

def llegadapersonas(npers, pacientes):
   """Funcion encargada de crear la cola de gente de edades aleatorias uniformemente"""
   #creo una cola de personas con edades aleatorias
   
   for i in range(npers):
       pacientes.enqueue(random.randint(0, 100))
         
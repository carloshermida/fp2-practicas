#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Módulo Añadir
# Carlos Hermida / Clara Lado

"""
Definición de las funciones para añadir
vacunas, personas
"""
from categories import Vacuna
from array_queue import ArrayQueue as Queue
import random

dosis_a = Queue()
dosis_b = Queue()
dosis_c = Queue()
pacientes = Queue()

def llegadadosis(vac_a, vac_b, vac_c, dosis_a, dosis_b, dosis_c):
    """Funcion encargada de dar un numero
    de vacunas de cada tipo."""
   
    #hago un bucle para que cada cola se llene del numero de vacunas llegadas
    for i in range(vac_a.getEntrada()):
        dosis_a.enqueue(1)

    for i in range(vac_b.getEntrada()):
        dosis_b.enqueue(1)
    
    for i in range(vac_c.getEntrada()):
        dosis_c.enqueue(1)
    
    vac_a.setStock(len(dosis_a))
    vac_b.setStock(len(dosis_b))
    vac_c.setStock(len(dosis_c))
    
    
def llegadapersonas(personas_dia, pacientes):

   """Funcion encargada de crear la cola de gente de edades aleatorias uniformemente"""
   #creo una cola de personas con edades aleatorias
   
   for i in range(personas_dia):
       pacientes.enqueue(random.randint(0, 100))

    # aqui hay que hacer camios para implementar sample.py
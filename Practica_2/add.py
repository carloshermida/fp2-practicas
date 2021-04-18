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

def llegadadosis(*arg):
    """Funcion encargada de dar un numero
    de vacunas de cada tipo."""
    
    # Tras recibir una tupla con un número indefinido de variables, 
    # las almacenamos en la lista var, para poder trabajar cómodamente
    var = []
    for item in arg:
        var.append(item)
    
    # Ejcutamos tantas veces como vacunas existan
    for i in range(len(var)//2):
        # La vacuna será el primer elemento y su cola de dosis correspondiente
        # será el siguiente elemento (según lo deifinimos en el string cadena_var
        # en el main)
        vac = var[0]
        dosis = var[1]
        
        # Añadimos a la cola de dosis las unidades especificadas en la entrada
        # diaria de cada vacuna
        for j in range(vac.getEntrada()):
            dosis.enqueue(1)
        
        # Actualizamos el Stock de cada vacuna
        vac.setStock(len(dosis))
        #Eliminamos de la lista de variables el par de vacuna - dosis ya utilizado
        var.pop(0)
        var.pop(0)
   
    
    
def llegadapersonas(personas_dia, pacientes):

   """Funcion encargada de crear la cola de
   gente de edades aleatorias uniformemente."""
   
   # Creamos una cola de personas con edades aleatorias
   for i in range(personas_dia):
       pacientes.enqueue(random.randint(0, 100))

    # aqui hay que hacer camios para implementar sample.py
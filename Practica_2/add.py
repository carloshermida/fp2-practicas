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
from sample import distribucion_aleatoria, distribucion_galicia
import sys

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
   
    
    
def selector_muestreo(personas_dia, pacientes, choose):
   """Funcion encargada de seleccionar el muestreo"""
   
   if choose == "U" or choose == "u":
       distribucion_aleatoria(personas_dia, pacientes)
   
   elif choose == "G" or choose == "g":
       distribucion_galicia(personas_dia, pacientes)
       
   else:
       print("Muestreo no válido")
       sys.exit()
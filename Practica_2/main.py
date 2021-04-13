#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Main
# Carlos Hermida / Clara Lado

"""
Código principal de la Práctica 2.
"""

import sys
from array_queue import ArrayQueue as Queue
import random

#creo una cola vacia para cada vacuna, perdon no se crear colaas
dosis_a = Queue() #para mayores de 70
dosis_b = Queue() #para entre 50 y 70
dosis_c = Queue() #para menores de 50
pacientes = Queue()
espera = Queue()

def llegadadosis(x, y, z):
    """Funcion encargada de dar un numero
    de vacunas de cada tipo."""
   
    #hago un bucle para que cada cola se llene del numero de vacunas llegadas
    for i in range(x):
        dosis_a.enqueue(1)

    for i in range(y):
        dosis_b.enqueue(1)
    
    for i in range(z):
        dosis_c.enqueue(1)

def personas(p):
   #intento crear una cola de personas con edades aleatorias
   
   for i in range(p):
       pacientes.enqueue(random.randint(1, 100))

def seleccionadorvacuna(pacientes):

    for i in range(len(pacientes)): 
        
        paciente = pacientes.first()
        
        if paciente < 50:
            if dosis_c.is_empty():
                espera.enqueue(paciente)
                print("NO HAY C")
            else:  
                print("JOVEN VACUNADO")
                dosis_c.dequeue()
            pacientes.dequeue()
               
            
        elif paciente>=50 and paciente<=70:
            if dosis_b.is_empty():
                espera.enqueue(paciente)
                print("NO HAY B")
            else:  
                print("ADULTO VACUNADO")
                dosis_b.dequeue()
            pacientes.dequeue()
        
        else:
            if dosis_a.is_empty():
                espera.enqueue(paciente)
                print("NO HAY A")
            else:  
                print("VIEJO VACUNADO")
                dosis_a.dequeue()
            pacientes.dequeue()
         
         
if __name__ == "__main__":
   
    llegadadosis(10,10,10)
    personas(30)
    seleccionadorvacuna(pacientes)
    
    print("ESPERA")
    for i in range(len(espera)): 
        
        print(espera.dequeue())
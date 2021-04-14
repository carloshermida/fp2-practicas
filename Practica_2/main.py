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
import sys

#creo una cola vacia para cada vacuna, para la lista de espera y los llamados en ese dia para ser vacunados
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
   """Funcion encargada de crear la cola de gente de edades aleatorias uniformemente"""
   #creo una cola de personas con edades aleatorias
   
   for i in range(p):
       pacientes.enqueue(random.randint(1, 100))

def seleccionadorvacuna(pacientes):
    """ Función que determina que clase de vacuna necesita cada uno y de 
    vacunarlos o mandarlos a la lista de espera """
    #creo un bucle que se repita tantas veces como personas en la lista
    for i in range(len(pacientes)): 
        #se analiza la primera edad de la lista
        paciente = pacientes.first()
        #dependiendo de su franja de edad se enviara a una u otra
        if paciente < 50:
            #en el caso de que no queden vacunas de ese tipo se enviara a la persona a una lista de espera
            if dosis_c.is_empty():
                espera.enqueue(paciente)
                print("NO HAY C")
            else:  
                print("JOVEN VACUNADO")
                dosis_c.dequeue()
                #en el caso de que queden dosis se elimina una 
            pacientes.dequeue()
            #se elimina a esa persona de la lista del dia y se comprueba la siguiente
        #repetimos lo mismo en los diferentes casos   
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
         
def main():
    #intento que lo solicite en el orden dosis A, B, C y Nº de pers
    
    if len(sys.argv) != 5:
        print(" pasa por aqui ")
        sys.exit()
        #si no se aportan todos los argumentos que se cierre
    try:
        #identifico cada elemento introducido
        vac_a = int(sys.argv[1])
        vac_b = int(sys.argv[2])    
        vac_c = int(sys.argv[3])
        npers = int(sys.argv[4])
        #llamo a las funciones para crear las colas
        llegadadosis(vac_a, vac_b, vac_c)
        personas(npers)
        seleccionadorvacuna(pacientes)
    finally:
        print("Hola")
         
if __name__ == "__main__":
   
    main()
    print("ESPERA")
    for i in range(len(espera)): 
        
        print(espera.dequeue())
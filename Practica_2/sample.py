#!/usr/bin/env python3
# -- coding: utf-8 --

# Módulo Muestra
# Carlos Hermida / Clara Lado

"""
Definición de las funciones
para el muestreo
"""

import random
from array_queue import ArrayQueue as Queue

pacientes = Queue()

def distribucion_galicia(personas_dia, pacientes):
    """Función que añade personas de edad aleatoria según la probabilidad gallega"""
    
    # Se abre el archivo con los datos de la población gallega y se lee su contenido
    with open("galicia_data.txt", 'r') as f:
        contenido = f.read()
    
    # Se divide en lineas el contenido
    data = contenido.split("\n")  
    
    # Se elimina el primer elemento que no aporta nada
    data.pop(0)
    
    # Se almacena el numero total de personas en una constante para trabajar con el posteriormente
    total = int(data.pop(0))
    
    # Creamos una lista con las edades y otra con las probabilidades
    edades = []
    probabilidades = []
    i = 0
    j = 1
    
    # Creamos un bucle que vaya recorriendo todo el archivo
    while len(edades) < 101:
        edades.append(int(data[i]))
        probabilidades.append(int(data[j])/total)
        i += 2
        j +=2

    # Añadimos el número de personas requerido
    for i in range(personas_dia):
        pacientes.enqueue((random.choices(edades, probabilidades)[0]))

def distribucion_aleatoria(personas_dia, pacientes):
    """Función que añade personas de edad aleatoria equiprobables"""
    
    # Añadimos el número de personas requerido
    for i in range(personas_dia):
        pacientes.enqueue(random.randint(0, 100))

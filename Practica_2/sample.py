#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Módulo Muestra
# Carlos Hermida / Clara Lado

"""
Definición de las funciones
para el muestreo
"""

def galicia_sample():

    with open("galicia_data.txt", 'r') as f:
        contenido = f.read()
 
    data = contenido.split("\n")  

    data.pop(0)
    total = int(data.pop(0))

    probability = dict()
    i = 0
    j = 1

    while len(probability) < 101:
        probability[int(data[i])] = int(data[j])/total
        i += 2
        j +=2
    
    return probability



# No está acabada la función, ahora que tenemos las probbilidades de cada edad hay que 
#escoger gente seun los datos

if __name__ == "__main__":
    
    prob = galicia_sample()
    print(prob)
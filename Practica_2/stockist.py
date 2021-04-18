#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Módulo distribuidor
# Carlos Hermida / Clara Lado

"""
Definición de las funciones para 
repartir según la edad y cantidad de dosis
"""

from array_queue import ArrayQueue as Queue
from categories import Vacuna

#creamos una cola para cada vacuna y la lista de espera
dosis_a = Queue()
dosis_b = Queue()
dosis_c = Queue()
pacientes = Queue()

def seleccionadorvacuna(dosis_a, dosis_b, dosis_c, pacientes, day, vac_a, vac_b, vac_c):
    """ Función que determina que clase de vacuna necesita cada uno y de 
    vacunarlos o mandarlos a la lista de espera """
    
    #creamos un bucle que se repita tantas veces como personas en la cola de vacunación haya
    for i in range(len(pacientes)): 
        
        #extraemos el primer elemento de cada vez de la cola
        paciente = pacientes.first()
        
        #contemplamos que edad tiene el paciente y por lo tanto en que rango entraria para poder seleccionar la vacuna adecuada
        for vac in [vac_a, vac_b, vac_c]:

            if paciente in range(vac.getLim_inf(), vac.getLim_sup()+1):

                if vac.getStock() > 0:
                    vac.setVacunados(vac.getVacunados() + 1)
                    vac.setStock(vac.getStock() - 1) 
                    
                     # se elimina una dosis de la cola de la vacuna seleccionada para dicho paciente
                    if vac == vac_a:
                        dosis_a.dequeue()
                    elif vac == vac_b:
                        dosis_b.dequeue()
                    elif vac == vac_c:
                        dosis_c.dequeue()
                
                else:
                    #en el caso de que no queden vacunas para esa persona se le volvera a añadir a la cola para que asi el dia siguiente pueda volver a intentar ponerse la dosis que le toca
                    pacientes.enqueue(paciente)
                    vac.setNoVacunados(vac.getNoVacunados() + 1)
                
                pacientes.dequeue()
            

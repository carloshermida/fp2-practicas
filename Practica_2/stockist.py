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

dosis_a = Queue()
dosis_b = Queue()
dosis_c = Queue()
pacientes = Queue()

def seleccionadorvacuna(dosis_a, dosis_b, dosis_c, pacientes, day, vac_a, vac_b, vac_c):
    """ Función que determina que clase de vacuna necesita cada uno y de 
    vacunarlos o mandarlos a la lista de espera """
    
    for i in range(len(pacientes)): 
        
        paciente = pacientes.first()
        
        for vac in [vac_a, vac_b, vac_c]:

            if paciente in range(vac.getLim_inf(), vac.getLim_sup()+1):

                if vac.getStock() > 0:
                    vac.setVacunados(vac.getVacunados() + 1)
                    vac.setStock(vac.getStock() - 1) 
                    
                    if vac == vac_a:
                        dosis_a.dequeue()
                    elif vac == vac_b:
                        dosis_b.dequeue()
                    elif vac == vac_c:
                        dosis_c.dequeue()
                
                else:
                    pacientes.enqueue(paciente)
                    vac.setNoVacunados(vac.getNoVacunados() + 1)
                
                pacientes.dequeue()
            

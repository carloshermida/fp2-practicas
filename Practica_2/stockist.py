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
import numpy as np

pacientes = Queue()

def seleccionadorvacuna(*arg):
    """ Función que determina que clase de vacuna necesita cada uno y
    valora si se puede vacunar o debe esperar. El último día, imprime por
    pantalla las estadísticas"""
    
    # Tras recibir una tupla con un número indefinido de variables, 
    # que sigue la forma "(pacientes, day, days, vac1, dosis1, vac2, dosis2 ...)",
    # las almacenamos en la lista var, para poder trabajar cómodamente
    
    var = []
    
    for item in arg:
        var.append(item)
    
    # Asignamos un nombre a cada parámetro
    pacientes = var[0]
    day = var[1]
    days = var[2]
    
    vac_lista = []
    dosis_lista = []
    i = 3
        
    # Creamos una lista de vacunas y otra lista de dosis
    while i < len(var):
        vac_lista.append(var[i])
        dosis_lista.append(var[i+1])
        i += 2
    
    # Inicializamos la cantidad de vacunados y no vacunados diarios
    for vac in vac_lista:
        vac.setVacunados(0)
        vac.setNoVacunados(0)
    
    # Ejecutamos el bucle por cada paciente que haya en este día
    for i in range(len(pacientes)): 
        
        # Obtenemos la edad del primer paciente
        paciente = pacientes.first()
        
        # Probamos todas las vacunas hasta encontrar la que se ajusta a su perfil
        for vac in vac_lista:
            
            # Continua si su edad  está comprendida en los rangos de aplicación de la vacuna
            if paciente in range(vac.getLim_inf(), vac.getLim_sup()+1):
                
                # Comprobamos que hay unidades de es vacuna
                if vac.getStock() > 0:
                    # Aumentamos el contador de vacunados de esa vacuna
                    vac.setVacunados(vac.getVacunados() + 1)
                    # Disminuimos el Stock de esa vacuna
                    vac.setStock(vac.getStock() - 1) 
                    
                    # Eliminamos una unidad de la cola de dosis de esa vacuna
                    # (su dosis correspondiente es la que está inmediatamente despues
                    # el la lista de variables)
                    
                    dosis = var[var.index(vac) + 1] 
                    dosis.dequeue()
                    
                # Si no quedan dosis, se le añade al final de la cola para
                # intentarlo el próximo día
                else:
                    pacientes.enqueue(paciente)
                    vac.setNoVacunados(vac.getNoVacunados() + 1)
                # Se haya vacunado o no, lo eliminamos del principio de la cola de pacientes
                pacientes.dequeue()
    
    
    # Actualizamos el contador global y las listas para la media y desviacion típica
    for vac in vac_lista:
        vac.setVacunados_total(vac.getVacunados_total()+vac.getVacunados())
        vac.set_lista_vac(vac.getVacunados())
        vac.set_lista_no_vac(vac.getNoVacunados())
    
    
    
    # Si es el último día, mostramos el resumen
    if day == days:

        print("-"*30, "\n\t\tRESUMEN\n","-"*30, "\n\n", sep="")
        
        total_vac = 0
        total_no_vac = 0
        
        # Mostramos las estadísticas para cada vacuna
        
        for vac in vac_lista:
            print("\t{} VACUNADOS: {} \tMEDIA: {} \tDESVIACIÓN TÍPICA: {}\n\t{} NO VACUNADOS: {}\
 \tMEDIA: {} \tDESVIACIÓN TÍPICA: {}\n".format(vac.getNombre(), vac.getVacunados_total(),
round(np.mean(vac.get_lista_vac())), round(np.std(vac.get_lista_vac())), vac.getNombre(), vac.getNoVacunados(),
round(np.mean(vac.get_lista_no_vac())),round(np.std(vac.get_lista_no_vac()))))
            
            total_vac += vac.getVacunados_total()
            total_no_vac += vac.getNoVacunados()
            
        print("\n\n\tTOTAL VACUNADOS: {}\n\tTOTAL NO VACUNADOS: {}".format(total_vac, total_no_vac))
        print("\n\n\tVACUNAS SOBRANTES:")
        
        for vac in vac_lista:
            print("\t\t{}: {}".format(vac.getNombre(), vac.getStock()))
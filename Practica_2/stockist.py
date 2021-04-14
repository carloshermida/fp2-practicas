#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Módulo distribuidor
# Carlos Hermida / Clara Lado

"""
Definición de las funciones para 
repartir según la edad y cantidad de dosis
"""

from array_queue import ArrayQueue as Queue

dosis_a = Queue()
dosis_b = Queue()
dosis_c = Queue()
pacientes = Queue()

def seleccionadorvacuna(dosis_a, dosis_b, dosis_c, pacientes, day, resumen_final):
    """ Función que determina que clase de vacuna necesita cada uno y de 
    vacunarlos o mandarlos a la lista de espera """
    #creo un bucle que se repita tantas veces como personas en la lista
    
    resumen = []
    
    joven_no_vacunado = 0
    adulto_no_vacunado = 0
    anciano_no_vacunado = 0
    
    joven_vacunado = 0
    adulto_vacunado = 0
    anciano_vacunado = 0
    
    
    for i in range(len(pacientes)): 
        #se analiza la primera edad de la lista
        paciente = pacientes.first()
        #dependiendo de su franja de edad se enviara a una u otra
        
        
        if paciente < 50:
            #en el caso de que no queden vacunas de ese tipo se enviara a la persona a una lista de espera
            if dosis_c.is_empty():
                pacientes.enqueue(paciente)
                joven_no_vacunado += 1
            else:  
                joven_vacunado += 1
                dosis_c.dequeue()
                #en el caso de que queden dosis se elimina una 
            pacientes.dequeue()
            #se elimina a esa persona de la lista del dia y se comprueba la siguiente
        
        
        #repetimos lo mismo en los diferentes casos   
        elif paciente>=50 and paciente<=70:
            if dosis_b.is_empty():
                pacientes.enqueue(paciente)
                adulto_no_vacunado += 1
            else:  
                adulto_vacunado += 1
                dosis_b.dequeue()
            pacientes.dequeue()
        
        
        
        else:
            if dosis_a.is_empty():
                pacientes.enqueue(paciente)
                anciano_no_vacunado += 1
            else:  
                anciano_vacunado += 1
                dosis_a.dequeue()
            pacientes.dequeue()
    
    #RESUMEN DIARIO
    resumen.append(joven_vacunado)
    resumen.append(joven_no_vacunado)
    resumen.append(adulto_vacunado)
    resumen.append(adulto_no_vacunado)
    resumen.append(anciano_vacunado)
    resumen.append(anciano_no_vacunado)
    
    print("RESUMEN DIA {}:\n\n\tJOVENES VACUNADOS: {}\n\tJOVENES NO VACUNADOS: {}\n\t\
ADULTOS VACUNADOS: {}\n\tADULTOS NO VACUNADOS: {}\n\t\
ANCIANOS VACUNADOS: {}\n\tANCIANOS NO VACUNADOS: {}\n".format(day, resumen[0], resumen[1],
    resumen[2], resumen[3],resumen[4],resumen[5]))
    
    
    #RESUMEN FINAL
    if day == 1:
        resumen_final.append(joven_vacunado)
        resumen_final.append(joven_no_vacunado)
        resumen_final.append(adulto_vacunado)
        resumen_final.append(adulto_no_vacunado)
        resumen_final.append(anciano_vacunado)
        resumen_final.append(anciano_no_vacunado)
    else: 
        resumen_final[0] += resumen[0]
        resumen_final[2] += resumen[2]
        resumen_final[4] += resumen[4]
        
        resumen_final[1] = resumen[1]
        resumen_final[3] = resumen[3]
        resumen_final[5] = resumen[5]
        
    
    
    return resumen_final
            

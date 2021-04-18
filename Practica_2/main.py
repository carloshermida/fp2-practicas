#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Main
# Carlos Hermida / Clara Lado

"""
Código principal de la Práctica 2.
"""

import sys
from stockist import seleccionadorvacuna
from add import llegadadosis, selector_muestreo
from array_queue import ArrayQueue as Queue
from categories import Vacuna

def main():
    """ Función principal encargada de obtener los parámetros
    del usuario y ejecutar el código tantas veces como días de simulación """
    
    # Leemos los argumentos de entrada 
    personas_dia = int(sys.argv[1])
    days = int(sys.argv[2])
    choose = str(sys.argv[3])
    
    #-------------------------------------------------------------------------
    # Tipos de vacunas
    #-------------------------------------------------------------------------
    # vac_"nombre" = Vacuna("Nombre", limite_inferior, limite_superior, entrada diaria)
    vac_a = Vacuna("a", 71, 100, int(sys.argv[4]))
    vac_b = Vacuna("b", 50, 70, int(sys.argv[5]))
    vac_c = Vacuna("c", 0, 49, int(sys.argv[6]))
    
    #Vacuna "d" añadida para experimento:
    #vac_d = Vacuna("d", 85, 100, int(sys.argv[7]))
    #vac_a = Vacuna("a", 71, 84, int(sys.argv[4]))
    #-------------------------------------------------------------------------
    
    vac_lista = []
    dosis_lista = []
    cadena_var = ""
    
    # Añadimos a la lista de vacunas las vacunas que creamos y al la lista de 
    # dosis sus respectivas colas de dosis. De esta forma obtenemos una lista
    # con todas las variables vacuna, y otra lista con las variales dosis que
    # definiremos más tarde
   
    # (Vacuna.lista_vacunas devuelve una lista con los nombres de todos los objectos vacuna creados)
    for item in Vacuna.lista_vacunas:
        vac_lista.append("vac_" + item)
        dosis_lista.append("dosis_" + item)
        # Creamos un string con todas las variables separadas por coma para facilitar
        # la llamada de funciones posteriormente
        cadena_var += ("vac_" + item + ",dosis_" + item)
        # Añadimos la coma en despues de cada par, a excepción del último
        if Vacuna.lista_vacunas.index(item) != len(Vacuna.lista_vacunas)-1:
            cadena_var += (",")
    
    # Si hay más o menos argumentos de los requeridos según la cantidad de vacunas,
    # el programa se cerrará
    if len(sys.argv) != (len(vac_lista) + 4):
        print("Formato:\n<Personas nuevas / día>\n<Días>\n<Muestreo>\n<Cantidad Vacuna A / día>\n<Cantidad Vacuna B / día>\n<Cantidad Vacuna C / día> ...")
        sys.exit()
       
    # Comenzamos el bucle en el día 1, hasta el día especificado por el usuario    
    for day in range(1, days+1):
        
        if day == 1:
            # Si es el primer día, inicializamos las colas de dosis, cuyos nombres
            # están espcificados en la lista de dosis
            for item in dosis_lista:
                globals()[item] = Queue()
            # Inicializamos también la cola de pacientes
            pacientes = Queue()
        
        # Llamamos a la función llegadadosis a través de la función eval para
        # poder mandarle los parámetros de todas las vacunas y dosis.
        eval("llegadadosis" + "({})".format(cadena_var))
        # Generamos personas con edades aleatorias
        selector_muestreo(personas_dia, pacientes, choose)
        # Procedemos de la misma forma que con la función llegadadosis,
        # aunque en este caso añadimos 3 parametros fijos que se mandarán
        # a la función seleccionadorvacuna si importar el número de vacunas
        eval("seleccionadorvacuna" + "(pacientes, day, days, {})".format(cadena_var))

if __name__ == "__main__":
    
    main()
    
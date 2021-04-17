#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Main
# Carlos Hermida / Clara Lado

"""
Código principal de la Práctica 2.
"""

import sys
from stockist import seleccionadorvacuna
from add import llegadadosis, llegadapersonas
from array_queue import ArrayQueue as Queue
from categories import Vacuna

def main():
    #intento que lo solicite en el orden dosis A, B, C y Nº de pers
    if len(sys.argv) != 6:
        print("Formato:\n<Cantidad Vacuna A / día>\n<Cantidad Vacuna B / día>\n<Cantidad Vacuna C / día>\n<Personas nuevas / día>\n<Días>")
        sys.exit()
        #si no se aportan todos los argumentos que se cierre
    
    try:
        #identifico cada elemento introducido
        vac_a = Vacuna("a", 71, 101, int(sys.argv[1]), 0, 0, 0)
        vac_b = Vacuna("", 51, 70, int(sys.argv[2]), 0, 0, 0) 
        vac_c = Vacuna("c", 0, 50, int(sys.argv[3]), 0, 0, 0)
        personas_dia = int(sys.argv[4])
        days = int(sys.argv[5])
        #llamo a las funciones para crear las colas
        
        for day in range(1, days+1):
            if day == 1:
                dosis_a = Queue() #para mayores de 70
                dosis_b = Queue() #para entre 50 y 70
                dosis_c = Queue() #para menores de 50
                pacientes = Queue()
                
            llegadadosis(vac_a, vac_b, vac_c, dosis_a, dosis_b, dosis_c)
            llegadapersonas(personas_dia, pacientes)
            seleccionadorvacuna(dosis_a, dosis_b, dosis_c, pacientes, day, vac_a, vac_b, vac_c)

   
    finally:
        print("RESUMEN:\n\n\tA VACUNADOS: {}\n\tA NO VACUNADOS: {}\n\t\
B VACUNADOS: {}\n\tB NO VACUNADOS: {}\n\tC VACUNADOS: {}\n\t\
C NO VACUNADOS: {}\n\n\tTOTAL VACUNADOS: {}\n\tTOTAL NO VACUNADOS: {}\n\n\t\
VACUNAS SOBRANTES:\n\t\tA: {}\n\t\tB: {}\n\t\tC: {}".format(vac_a.getVacunados(),
vac_a.getNoVacunados(),vac_b.getVacunados(), vac_b.getNoVacunados(),vac_c.getVacunados(),vac_c.getNoVacunados(),
(vac_a.getVacunados()+vac_b.getVacunados()+vac_c.getVacunados()), (vac_a.getNoVacunados()+vac_b.getNoVacunados()+vac_c.getNoVacunados()),
len(dosis_a), len(dosis_b), len(dosis_c)))
         
if __name__ == "__main__":
   
    
   main()
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

def main():
    #intento que lo solicite en el orden dosis A, B, C y Nº de pers
    if len(sys.argv) != 6:
        sys.exit()
        #si no se aportan todos los argumentos que se cierre
    
    try:
        #identifico cada elemento introducido
        vac_a = int(sys.argv[1])
        vac_b = int(sys.argv[2])    
        vac_c = int(sys.argv[3])
        npers = int(sys.argv[4])
        days = int(sys.argv[5])
        #llamo a las funciones para crear las colas
        
        for day in range(1, days+1):
            if day == 1:
                dosis_a = Queue() #para mayores de 70
                dosis_b = Queue() #para entre 50 y 70
                dosis_c = Queue() #para menores de 50
                pacientes = Queue()
                resumen_final = []
                
            llegadadosis(vac_a, vac_b, vac_c, dosis_a, dosis_b, dosis_c)
            llegadapersonas(npers, pacientes)
            resumen_final = seleccionadorvacuna(dosis_a, dosis_b, dosis_c, pacientes, day, resumen_final)
    
    finally:
        print("RESUMEN FINAL:\n\n\tJOVENES VACUNADOS: {}\n\tJOVENES NO VACUNADOS: {}\n\t\
ADULTOS VACUNADOS: {}\n\tADULTOS NO VACUNADOS: {}\n\tANCIANOS VACUNADOS: {}\n\t\
ANCIANOS NO VACUNADOS: {}\n\n\tTOTAL VACUNADOS: {}\n\tTOTAL NO VACUNADOS: {}\n\n\t\
VACUNAS SOBRANTES:\n\t\tA: {}\n\t\tB: {}\n\t\tC: {}".format(resumen_final[0],
resumen_final[1],resumen_final[2], resumen_final[3],resumen_final[4],resumen_final[5],
(resumen_final[0]+resumen_final[2]+resumen_final[4]), (resumen_final[1]+resumen_final[3]+resumen_final[5]),
len(dosis_a), len(dosis_b), len(dosis_c)))
         

if __name__ == "__main__":
   
    
   main()
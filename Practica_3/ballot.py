#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Módulo Votaciones
# Carlos Hermida / Clara Lado

"""
Definición de las funciones encargadas
de llevar a cabo la votación
"""

import random
from array_positional_list import ArrayPositionalList as positionallist
#from linked_positional_list import LinkedPositionalList as positionallist


def print_list(opl):
    """Muestra la lista posicional por pantalla"""
    print("[", end=" ")
    for x in opl:
        print("{} [{}]".format(x.getNombre(), x.getPuntos()), end=" ")
    print("]")
    
    

def votacion(lista_concursantes, simulacion, demo):
    """Función que simulará todo el proceso de la votación"""
    
    # Creamos el ranking como una lista posicional
    ranking = positionallist()
    
    # Creamos un bucle que se repita para todos los concursantes
    for i in range(len(lista_concursantes)):
        
        # Si la simulación en proceso es la elegida aleatoriamente como demostración, 
        # se mostrará por pantalla el proceso (Número de simulación, votación, pais que vota)
        if simulacion == demo:
            print("\n","*"*50, "\n\nSIMULACIÓN Nº", simulacion, sep= "")
            print("VOTACIÓN: ", i+1)
            print("VOTA: ", lista_concursantes[i].getNombre(), "\nREPARTO:\n")
            
        # Creamos otra lista donde estarán los participantes, a excepción del que va a votar
        validos = []
        for pais in lista_concursantes:
            validos.append(pais)
        # Eliminamos al que vota
        validos.pop(i)
        
        # Creamos otra lista para los paises a los que les votaron de forma aleatoria
        lista_afortunados = []
        # Creamos un bucle para que se repita 10 veces (número de votos que tendrá que repartir cada país)
        for voto in range(10):
            # Selecciono a un pais aleatorio de la lista a los que se les puede dar el voto
            a = random.choice(validos)
            # Lo añadimos a la lista de afortunados
            lista_afortunados.append(a)
            # Lo elimino de la lista de válidos ya que no se podrá volver a votar otra vez en esta ronda
            validos.remove(a)
        
            
        # REPARTO DE PUNTOS
        
        cnt_points = 1
        x = 12
        # Aumentamos los puntos de los afortunados
        for afortunado in lista_afortunados:
            afortunado.setPuntos(afortunado.getPuntos()+x)
            
            # Si la simulación en proceso es la elegida aleatoriamente como demostración, 
            # se mostrará por pantalla el proceso (pais que ha sido votado, puntos concedidos)
            if simulacion == demo:    
                print("-"*30, sep="")
                print(afortunado.getNombre(), x)
            
            # Administramos los puntos según la posición
            if cnt_points < 3:
                x += -2
            else:
                x += -1
            cnt_points += 1 
        
        
        
            # ---------- (USO LISTA POSICIONAL) ----------
            # RANKING
            
            # Recolocamos cada pais que recibió puntos en la ronda de votación actual
            for country in lista_afortunados:
            
                puntos_pais_votado = country.getPuntos()
            
                # Si el ranking está vacío, añadimos el primer pais
                if ranking.is_empty():
                    ranking.add_first(country)
                
                # Si no está vacío, habrá que valorar y reordenar
                else:
                    cnt_tmp = 0
                    # Recorremos el ranking para asegurarnos que el pais que vamos a 
                    # añadir no está ya en el ranking
                    for pais_ranking in ranking:
                        # Si el pais ya estaba en el ranking, lo eliminamos
                        if pais_ranking == country:
                            ranking.delete(cnt_tmp)
                            break
                        cnt_tmp += 1
                
                
                    # ORDENAR
                    
                    cnt = 0
                    y = 0
                    # Recorremos el ranking
                    for pais in ranking:
                        # En el momento en el que los puntos del pais que queremos introducir
                        # son mayores que los puntos de un pais del ranking, añadimos el primer
                        # pais antes del que tiene menos puntos.
                        if puntos_pais_votado >= pais.getPuntos():
                            ranking.add_before(cnt, country)
                            y = 1
                            break
                        cnt += 1
                    # En el caso en el que no se encuentre en el ranking ningún pais
                    # con menos puntos que el pais que queremos introducir, lo añadiremos al
                    # final, pues significa que es el menor de todos
                    if y == 0:
                        ranking.add_last(country)
        
        
            # Si la simulación en proceso es la elegida aleatoriamente como demostración, 
            # se mostrará por pantalla el proceso (Ranking reordenado después de concederle puntos a un pais)
            if simulacion == demo:
                print_list(ranking)
            
     
    # Si la simulación en proceso es la elegida aleatoriamente como demostración, 
    # se mostrará por pantalla el proceso (Ranking final de la simulación)   
    if simulacion == demo:
        print("\n", "*"*50, sep="")
        print("\nRESULTADO FINAL:\n")  
        print_list(ranking)
    
    return ranking
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
from linked_positional_list import LinkedPositionalList



def votacion(lista_orden):
    """Función que simulará todo el proceso de la votación"""
    
    ranking = positionallist()
    
    #creo un bucle que se repita tantas veces como concursantes haya
    for i in range(len(lista_orden)): #15
        
        print("VOTACIÓN: ", i+1)
        print("VOTA: ", lista_orden[i].getNombre(), "\n")
        #creo otra lista donde estaran el resto de participantes menos al que le toca votar para que entre ellos repartan sus puntos
        validos = []
        for pais in lista_orden:
            validos.append(pais)
        
        #elimino al que vota
        validos.pop(i)
        #creo otra lista para los seleccionados a los que les tocaron los votos de forma aleatoria
        votos_seguros = []
        #creo un bucle para que se repita 10 veces, numero de votos que tendrá que repartir cada país
        
        for numero in range(10):
            #selecciono a un pais aleatorio de la lista a los que les puedo dar el voto
            a = random.choice(validos)
            #lo añado a la lista de afortunados
            votos_seguros.append(a)
            #lo elimino de la lista anterior ya que no podre volver a votarle otra vez
            validos.remove(a)
            
        cnt = 1
        x = 12
        for w in range(len(votos_seguros)):
            
            votos_seguros[0].setPuntos(votos_seguros[0].getPuntos()+x)
            
            if cnt < 3:
                x += -2
            else:
                x += -1
            
            print(votos_seguros[0].getNombre(), votos_seguros[0].getPuntos())
            votos_seguros.pop(0)
            cnt += 1 
        
        
        
        #RANKING
        
        
        
        
        
        # FIN BUCLE VOTACIONES
        print("*"*50)
     
        
    for i in range(len(lista_orden)):
        print(lista_orden[i].getNombre(), lista_orden[i].getPuntos())
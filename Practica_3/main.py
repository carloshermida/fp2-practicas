#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Main
# Carlos Hermida / Clara Lado

"""
Código principal de la Práctica 3.
"""
#importo los módulos necesarios para trabajar
from countries import country
import random 
from array_positional_list.py import ArrayPositionalList as positionallist
from linked_positional_list.py import LinkedPositionalList

#creo la lista posicional que hará de ranking del concurso
ranking = positionallist()
def inicio_participantes():
    """Función que creara una lista de participantes"""
    #creamos una lista vacia donde se iran añadiendo los participantes de eurovision
    lista_paises = []
    ascii_code = 65
    
    #creamos un bucle que para que añada los participantes necesarios, como se nombraran letras sucesivas desde la A
    #hacemos que automaticamente vaya nombrandolos por defecto la siguiente letra
    for i in range(15):
        name = chr(ascii_code)
        globals()[name] = country(name) #para que valia esto???????
        ascii_code += 1
        lista_paises.append(name)
    
    return lista_paises
        

#def puntos()

def votacion(lista_orden):
    """Función que simulará todo el proceso de la votación"""
    #creo un bucle que se repita tantas veces como concursantes haya
    for i in range(len(lista_orden)):
        #creo otra lista donde estaran el resto de participantes menos al que le toca votar para que entre ellos repartan sus puntos
        validos = lista_orden
        #elimino al que vota
        validos.remove(lista_orden[i])
        #creo otra lista para los seleccionados a los que les tocaron los votos de forma aleatoria
        votos_seguros = []
        #creo un bucle para que se repita 10 veces, numero de votos que tendrá que repartir cada país
        for i in range(10):
            #selecciono a un pais aleatorio de la lista a los que les puedo dar el voto
            a = random.choice(validos)
            #lo añado a la lista de afortunados
            votos_seguros.append(a)
            #lo elimino de la lista anterior ya que no podre volver a votarle otra vez
            validos.remove(a)
            
        #ahora que ya tengo una lista aleatoria con todos a los que les doy mis puntos, este país en concreto, empiezo a repartirlos entre ellos y añadirlos al ranking
        
        print(lista_orden[i], "votó a :")

if __name__ == "__main__":
    
    print("CONCURSANTES: ")
    lista = inicio_participantes()
    print(lista)
    random.shuffle(lista)
    print(lista)
    votacion(lista)
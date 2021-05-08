#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Main
# Carlos Hermida / Clara Lado

"""
Código principal de la Práctica 3.
"""

from ballot import votacion
from countries import country
import random 


def inicio_participantes_letras():
    """Función que creará una lista de participantes a partir del abecedario (NO SE USA)"""
    
    # Creamos una lista vacia donde se irán añadiendo los participantes
    lista_paises = []
    ascii_code = 65
    # Creamos un bucle que para que añada los participantes necesarios siguiendo el orden alfabético
    for i in range(random.randint(15, 25)):
        name = chr(ascii_code)
        # Generamos una variable donde guardamos el objeto pais para cada letra
        globals()[name] = country(name)
        ascii_code += 1
        # Añadimos todas las variables (participantes) a la lista de paises
        lista_paises.append(globals()[name])
    
    return lista_paises
  
      
def inicio_participantes_paises():
    """Función que creara una lista de participantes siguiendo el modelo real de eurovisión"""
    
    big_five = ["Alemania", "Italia", "España", "Francia", "Inglaterra"]
    candidatos = [ "Lituania", "Eslovenia", "Rusia", "Suecia", "Australia", "Macedonia",
                    "Irlanda", "Chipre", "Noruega", "Croacia", "Belgica", "Israel", "Rumania",
                    "Azerbaiyan", "Ucrania", "Malta", "Bielorrusia", "San_Marino", "Estonia",
                    "R_Checa", "Grecia", "Austria", "Polonia", "Moldavia", "Islandia",
                    "Serbia", "Georgia", "Albania", "Portugal", "Bulgaria", "Finlandia", "Letonia",
                    "Suiza", "Dinamarca", "Armenia", "Holanda"]

    # Añadimos por defecto a la final a los 5 paises fundadores
    lista_paises = big_five
    # Simulamos las semifinales aleatoriamente. Se clasifican entre 10 y 20 paises candidatos (en total 15-25)
    for i in range(random.randint(10, 20)):
        afortunado = random.choice(candidatos)
        lista_paises.append(afortunado)
        candidatos.remove(afortunado)
        
          
    # Reciclamos la lista "lista paises", donde para cada pais creamos su correspondiente objeto pais y lo 
    # guardamos en una variable que añadimos a la lista
    for i in range(len(lista_paises)):
        name = lista_paises[0]
        globals()[name] = country(name)
        lista_paises.append(globals()[name])
        lista_paises.pop(0)
    
    return lista_paises


def main(n):
    """Simula la final de Eurovisión n veces"""
    
    # Elegimos una simulación aleatoria para mostrar posteriormente por pantalla 
    # el funcionamiento del concurso, probando así la implementación de las listas posicionales
    demo = random.randint(1, n)
    # Creamos la lista stats_sim, que guardará sublistas con el nombre del pais y sus respectivas
    # posiciones a lo largo de las simulaciones
    stats_sim = []
    # Ejecutamos la simulación n veces
    for sim in range(n):  
        # Obtenemos la lista de participantes
        # lista = inicio_participantes_letras() # función para que los paises se identifiquen con una letra
        lista = inicio_participantes_paises()
        # Barajamos la lista para mayor aletoriedad
        random.shuffle(lista)
        # Simulamos la fase de votación y obbtenemos en resultado final. En una simulación
        # aleatoria, se mostrará por pantalla el proceso completo.
        ranking = votacion(lista, sim+1, demo)
        
        # Almacenamos los resultados de cada simulación en una lista para crear estadísticas posteriormente
        # Recorremos el ranking guardando el pais y su posición
        for i in range(len(ranking)):
            nombre = ranking.get_element(i).getNombre()
            posicion = i+1
            tmp = 0
            
            # Comprobamos si el pais ya se encuentra en la lista
            for stat in stats_sim:
                # Si ya existe, le añadimos la posición de la última simulación
                if stat[0] == nombre:
                    stat.append(posicion)
                    tmp = 1
                    
            # Si aún no está registrado, lo añadimos
            if tmp == 0:
                stats_sim.append([nombre, posicion])
                    
    return stats_sim


def final_stats(n, stats_sim):
    """Imprime por pantalla las estadísitcas finales despues de n simulaciones"""
    
    print("\n", "*"*50, "\n", sep="")
    print("-"*50, "\n\t\tESTADÍSTICAS (simulación {} veces)\n".format(n), "–"*50, sep="")
    print("\tPaís\t\t|\tParticipación\t|\tGanados\t\n", "-"*50, sep= "")
    # Para las estadísticas de cada pais, muestra el nombre, las veces que participó y las veces que ganó
    for stat in stats_sim:
        print(stat[0], " "*(21-len(stat[0])), len(stat)-1, " "*12, stat.count(1), "({0:.2f}%)".format(stat.count(1)/n*100))
        print("-"*50)
        
        
if __name__ == "__main__":
    
    n = int(input("Introduce el número de simulaciones: "))
    final_stats(n, main(n))     
    
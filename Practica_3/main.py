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
from ballot import votacion


def inicio_participantes():
    """Función que creara una lista de participantes"""
    #creamos una lista vacia donde se iran añadiendo los participantes de eurovision
    lista_paises = []
    ascii_code = 65
    #creamos un bucle que para que añada los participantes necesarios, como se nombraran letras sucesivas desde la A
    #hacemos que automaticamente vaya nombrandolos por defecto la siguiente letra
    for i in range(15):
        name = chr(ascii_code)
        globals()[name] = country(name)
        ascii_code += 1
        lista_paises.append(globals()[name])
    
    return lista_paises
        
def inicio_participantes_2():
    """Función que creara una lista de participantes"""
    
    big_five = ["Alemania", "Italia", "España", "Francia", "Inglaterra"]
    candidatos = [ "Lituania", "Eslovenia", "Rusia", "Suecia", "Australia", "Macedonia",
                    "Irlanda", "Chipre", "Noruega", "Croacia", "Belgica", "Israel", "Rumania",
                    "Azerbaiyan", "Ucrania", "Malta", "Bielorrusia", "San_Marino", "Estonia",
                    "R_Checa", "Grecia", "Austria", "Polonia", "Moldavia", "Islandia",
                    "Serbia", "Georgia", "Albania", "Portugal", "Bulgaria", "Finlandia", "Letonia",
                    "Suiza", "Dinamarca", "Armenia", "Holanda"]

    lista_paises = big_five
    for i in range(random.randint(10, 20)):
        afortunado = random.choice(candidatos)
        lista_paises.append(afortunado)
        candidatos.remove(afortunado)
        
          
        
    for i in range(len(lista_paises)):
        
        name = lista_paises[0]
        globals()[name] = country(name)
        lista_paises.append(globals()[name])
        lista_paises.pop(0)
    
    return lista_paises


def main(n):
    
    demo = random.randint(1, n)
    pos_sim = []
    for i in range(n):  
        lista = inicio_participantes_2()
        random.shuffle(lista)
        ranking = votacion(lista, i+1, demo)
        for i in range(len(ranking)):
            nombre = ranking.get_element(i).getNombre()
            posicion = i+1
            y = 0
            for q in pos_sim:
                if q[0] == nombre:
                    q.append(posicion)
                    y = 1
            
            if y == 0:
                pos_sim.append([nombre, posicion])
                    
    return pos_sim


def stats(n, pos_sim):
    
    print("\n", "*"*50, "\n", sep="")
    print("-"*50, "\n\t\tESTADÍSTICAS (simulación {} veces)\n".format(n), "–"*50, sep="")
    print("\tPaís\t\t|\tParticipación\t|\tGanados\t\n", "-"*50, sep= "")
    for w in pos_sim:
        print(w[0], " "*(21-len(w[0])), len(w)-1, " "*12, w.count(1), "({0:.2f}%)".format(w.count(1)/n*100))
        print("-"*50)
        
if __name__ == "__main__":
    
    n = int(input("Introduce el número de simulaciones: "))
    pos_sim = main(n)
    stats(n, pos_sim)     
    
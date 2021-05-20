#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Módulo Socios Aleatorios
# Carlos Hermida / Clara Lado

"""
Definición de las funciones encargadas de generar socios para los equipos
"""

import random

no_repeat = []

def random_dni():
    """Devuelve un dni válido generado aleatoriamente"""
    
    letter_code = {0:"T", 1:"R", 2:"W", 3:"A", 4:"G", 5:"M", 6:"Y", 7:"F", 8:"P", 9:"D", 10:"X", 11:"B",
              12:"N", 13:"J", 14:"Z", 15:"S", 16:"Q", 17:"V", 18:"H", 19:"L", 20:"C", 21:"K", 22:"E"}
    
    dni_number = 0
    for i in range(8):
        number = random.randint(0,9) * 10 ** i
        dni_number += number
    
    remainder = dni_number%23
    letter = letter_code[remainder]
    dni = str(str(dni_number) + "-" + letter)
    
    while len(dni) < 10:
        dni = "0" + dni
        
    if dni in no_repeat:
        dni = random_dni()
    no_repeat.append(dni)
    
    return dni



def random_name():
    """Devuleve dos apellidos y un nombre aleatorios"""
    
    masculine_names_list = ["Antonio", "Manuel", "Jose", "Francisco", "David", "Juan", 
                            "Javier", "Daniel", "Carlos", "Jesus", "Alejandro", "Miguel",
                            "Rafael", "Angel", "Pedro", "Pablo"]
    
    feminine_names_list = ["Maria", "Carmen", "Ana", "Josefa", "Isabel", "Pilar", "Dolores",
                           "Laura", "Teresa", "Cristina", "Marta", "Francisca", "Lucía",
                           "Clara", "Julia", "Berta"]
    
    surname_list = ["Garcia", "Rodriguez", "Gonzalez", "Fernandez", "Lopez", "Martinez", "Sanchez",
                    "Perez", "Gomez", "Jimenez", "Ruiz", "Hernandez", "Diaz", "Moreno", "Muñoz", "Alvarez",
                    "Romero", "Alonso", "Gutierrez"]

    gender = random.randint(0, 1)
    
    if gender == 0:
        name = random.choice(masculine_names_list)
    else:
        name = random.choice(feminine_names_list)
        
    surnames = random.choices(surname_list, k=2)
    first_surname, second_surname = surnames[0], surnames[1]
    
    identity = str(first_surname + " " + second_surname + ", " + name)
    
    return identity
    


def random_birth():
    """Devuelve una fecha de nacimiento aleatoria entre 1922y 2018"""
    
    # genera pesonas entre 3-99 años
    year = random.randint(1922, 2018)
    
    month = random.randint(1,12)
    
    if month in [1,3,5,7,8,10,12]:
        day = random.randint(1, 31)
    elif month == 2:
        if year%4 == 0:
            day = random.randint(1, 29)
        else:
            day = random.randint(1,28)
    else:
        day = random.randint(1, 30)
    
    date = "{}/{}/{}".format(day, month, year)
    no_repeat.append(date)
    
    return date



def random_location():
    """Devuleve una posición en el estadio aleatoria"""
    
    locations = ["tribuna", "preferencia", "fondoNorte", "fondoSur"]
    location = random.choice(locations)
    
    return location



def random_txt(team, people):
    """Genera un número determinado de socios (people) del equipo elegido (team)
    y guarda sus datos en un archivo de texto"""
    
    file = "equipo{}.txt".format(team)
    
    # eliminamos el contenido del fichero
    with open (file, "w") as r:
        r.write("")
    
    # escribimos los nuevos socios aleatorios
    with open (file, "a") as f:
        
        for w in range(people):
            
            personal_data = "{}, {}, {}, {}".format(random_dni(), random_name(), random_birth(), random_location())
            f.write(personal_data)
            if w < people - 1:
                f.write("\n")



#######################################
#               TEST
######################################

if __name__ == "__main__":

    random_txt("A", 10)
    random_txt("B", 20)
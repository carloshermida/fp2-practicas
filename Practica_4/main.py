#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Main
# Carlos Hermida / Clara Lado

"""
Código principal de la Práctica 4.
"""

from partner import socio
from avl_tree import AVL
from random_people import random_txt 
import sys
import random


def forest(team):
    """Crea árboles a partir de un fichero de texto"""   
   
    # Nombramos la variable file para llamar al archivo de texto donde se encuentran los datos de los socios de determinado club
    file = "equipo{}.txt".format(team)
    
    # Leemos el contenido de dicho archivo
    with open (file, "r") as f:
        contenido = f.read()
    
    # Lo dividimos en lineas
    lines = contenido.split("\n")
    
    # Creamos un árbol
    tree = AVL()
    print("\nARBOL: {}".format(team))
    
    # Guardamos los datos relacionados cada socio
    for linea in lines:
        abonado = False
        data = linea.split(", ")
        
        # Si la línea empieza por $ ($ocio), sabemos que se trata del dueño de un abono familiar
        if linea.startswith("$"):
            dni = data[0][1:]
        
        # Si la línea empieza por @ (@bonado), sabemos que se trata de un abonado a un abono familiar
        elif linea.startswith("@"):
            abonado = True
            dni_abonado = data[0][1:]
            # Buscamos la posicion del dueño del abono en el árbol y añadimos un abonado a su lista de abonados
            # Los abonados no forman parte del árbol
            posicion_socio = tree.find_position(dni_abonado)
            posicion_socio.value().setAbonado(socio(dni_abonado, str(data[1]+", "+data[2]), data[3], data[4]))
        
        # Si la línea no empieza por ningún código, se trata de un socio sin abono
        else: 
            dni = data[0]
        
        # Vamos añadiendo cada socio con sus determinados datos al árbol
        if not abonado:
            tree[dni] = socio(dni, str(data[1]+", "+data[2]), data[3], data[4])
         
    # Mostramos en árbol por pantalla   
    preorder_indent_BST(tree,tree.root(),0)
    return tree   
    

def grafting(arbol_1, arbol_2):
    """Unifica los integrantes de dos árboles en un único árbol"""
    
    # Copiamos en arbol 1 en el arbol final
    arbol_final = arbol_1
    
    # Accedemos a la primera posicion del arbol 2
    p = arbol_2.first()
    
    # Mientras la posición devuleva un valor, recorremos el árbol
    while p is not None:
        
        # Para cada posición sacamos la clave (DNI) y el valor (objeto socio)
        key = p.key()
        value = p.value()  
        
        # Si el socio que queremos añadir ya está en el árbol final, comprobamos que sus abonados no varían
        if check_key(arbol_final, key):
           
            # Obtenemos la lista de abonados del socio que queremos añadir
            abonados_2 = value.getListaAbonados()
            
            # Obtenemos la posicion en el arbol final del socio que queremos añadir y obtenemos su lista de abonados antigua
            position_final = arbol_final.find_position(key)
            abonados_final = position_final.value().getListaAbonados()
            
            # Creamos una lista con los nombres de los abonados antiguos para despues compararlos
            tmp = []
            for i in abonados_final:
                tmp.append(i.getNombre())
            
            # Comprobamos si hay algún abonado nuevo que debamos añadir
            for item in abonados_2:
                if item.getNombre() not in tmp:
                    abonados_final.append(item)
        
        # Si el socio que queremos añadir no está en el árbol final, lo añadimos
        else:
            arbol_final[key] = value
         
        # Nos movemos a la siguiente posición
        p = arbol_2.after(p)
   
    
    # Mostramos por pantalla en árbol final (unificado)
    print("\nARBOL FINAL:")
    preorder_indent_BST(arbol_final,arbol_final.root(),0)
    
    return arbol_final


def check_key(arbol, clave):
    """Comprueba si una clave está en un árbol"""
    
    # Buscamos la posicion de la clave en el árbol
    position = arbol.find_position(clave)
    # Si la posición es nula, no está en el árbol
    if position is None:
        return False
    # Si la clave en esa posición es igual a la clave que buscamos, confirmamos que se encuentra en ese árbol
    elif position.key() == clave:
        return True
    # En cualquier otro caso, devolvemos falso
    else:
        return False
   
    
def preorder_indent_BST(T, p, d):
    """Print preorder representation of a binary subtree of T rooted at p at depth d"""
    
    if p is not None:
        # use depth for indentation
        print(2*d*' ' + "(" + str(p.key()) + "," +  str(p.value().getNombre()) + str(p.value().getNombreAbonado()) + ")") 
        preorder_indent_BST(T, T.left(p), d+1) # left child depth is d+1
        preorder_indent_BST(T, T.right(p), d+1) # right child depth is d+1
             
        
def chop_down(arbol):
    """Crea un archivo de texto a partir de un árbol"""
    
    # Accedemos a la primera posición del árbol
    p = arbol.first()
    # Nombramos el fichero que tendrá la lista final de socios
    file = "equipoFINAL.txt"
    # Eliminamos el contenido del fichero
    with open (file, "w") as r:
        r.write("")
    # Mientras la posición devuleva un valor, recorremos el árbol   
    while p is not None:
        # Asignamos a la variable value valor de la posición p (objeto socio)
        value = p.value()
        
        # Añadimos al archivo de texto los datos correspondientes a cada socio
        with open (file, "a") as f:
            
            # Si es un socio sin abono, imprime solamente sus datos
            if len(value.getListaAbonados()) == 0:
                
                # Llamamos a la función prices para obtener la cuota del socio
                precio = prices(value.getUbicacion(), 0)
                personal_data = "{}, {}, {}, {}, {}€".format(value.getDni(), value.getNombre(), value.getFecha(), value.getUbicacion(), precio)
                f.write(personal_data)  
            
            # Si se trata de un socio con abono y abonados, imprime sus datos y los de sus abonados
            else:
                
                # LLamamos a la función prices para obtener el precio total del abono
                precio = prices(value.getUbicacion(), len(value.getListaAbonados()))
                # Identificamos al socio con el símbolo $ antes del DNI
                personal_data_s = "${}, {}, {}, {}, {}€".format(value.getDni(), value.getNombre(), value.getFecha(), value.getUbicacion(), precio)
                f.write(personal_data_s)
                f.write("\n")
                
                # Añadimos cada uno de los abonados y los identificamos con el símbolo @
                for abonado in value.getListaAbonados():
                    personal_data_a = "@{}, {}, {}, {}".format(abonado.getDni(), abonado.getNombre(), abonado.getFecha(), value.getUbicacion())
                    f.write(personal_data_a) 
                    # Escribimos un salto de línea a excepción de la última línea
                    if value.getListaAbonados().index(abonado) < len(value.getListaAbonados()) - 1:
                        f.write("\n")
            
            # Nos movemos a la siguiente posición        
            p = arbol.after(p)
            
            # Escribimos un salto de línea a excepción de la última línea, cuando ya se recorrió todo el árbol y la siguiente posición es nula
            if p is not None:
                f.write("\n")

        
def prices(ubicacion, abonados):
    """ Devulve el precio que se debe pagar según la ubicación 
    y el número de abonados en caso de abono familiar"""
    
    if ubicacion == "tribuna":
        cuota = 2024
    
    elif ubicacion == "preferencia":
        cuota = 1609
    
    elif ubicacion == "fondoNorte":
        cuota = 1101
        
    else:
        cuota = 660
    
    # El precio final será igual a la cuota de la ubicación más media cuota por cada abonado familiar
    precio = cuota + int(abonados)*cuota/2
    
    return precio


def start(n_equipos, minimo_socios, maximo_socios):
    """Genera los ficheros y los arboles correspondientes a cada equipo"""
    
    ascii_code = 65
    lista_arboles = []
    
    for i in range(n_equipos):
        # Nombramos a cada equipo con las letras del abecedario
        name = chr(ascii_code)
        # El número de socios de cada equipo será un número aleatorio entre el mínimo y el máximo especificado
        n_socios = random.randint(minimo_socios, maximo_socios)
        # Generamos los ficheros con los datos de los socios de los equipos
        random_txt(name, n_socios)
        # Creamos su correspondiente árbol y lo añadimos a una lista de árboles
        lista_arboles.append(forest(name))
        
        ascii_code += 1
   
    return lista_arboles
   
    
if __name__ == "__main__":
    

    if len(sys.argv) != 4:
        print("ERROR / Formato: <nº de equipos a fusionar> <mínimo de socios por equipo> <máximo de socios por equipo>")
        sys.exit()
    
    n_equipos = int(sys.argv[1])
    if n_equipos < 2:
        print("ERROR / nº de equipos a fusionar no válido")
        sys.exit()
    
    minimo_socios = int(sys.argv[2])
    maximo_socios = int(sys.argv[3])
    if maximo_socios < 1 or minimo_socios < 1:
        print("ERROR / nº de socios no válido")
        sys.exit()
    
    # Obtenemos una lista con todos los árboles
    lista_arboles = start(n_equipos, minimo_socios, maximo_socios)
    
    # Mientras exista más de un árbol, unificaremos los que haya
    while len(lista_arboles) > 1:
        
        # Obtenemos el primer y el segundo árbol y los borramos de la lista
        arbol1 = lista_arboles.pop(0)
        arbol2 = lista_arboles.pop(0)
        # Unificamos ambos árboles y añadimos el árbol resultante a la lista de árboles
        arbol_final = grafting(arbol1, arbol2)
        lista_arboles.append(arbol_final)
    
    # Creamos el archivo de texto correspondiente al último árbol
    chop_down(arbol_final)
    
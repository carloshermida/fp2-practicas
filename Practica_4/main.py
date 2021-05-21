#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Main
# Carlos Hermida / Clara Lado

"""
Código principal de la Práctica 4.
"""
#importamos los modulos necesarios
from partner import socio
from avl_tree import AVL
from random_people import random_txt 
from positional_binary_tree import PositionalTree
import sys
import random



def forest(team):
    """Función encargada de crear aarboles a partir de un fichero de texto"""   
   
    #nombremos la variable file para llamar a el archivo de texto donde se encuentran los datos de los socios de determinado club
    file = "equipo{}.txt".format(team)
    
    #leemos el contenido de dicho archivo
    with open (file, "r") as f:
        contenido = f.read()
    
    #lo dividimos en lineas al separarlo por los saltos de linea
    lines = contenido.split("\n")
    
    tree = AVL()
    print("\nARBOL: {}".format(team))
    
    #creamos un bucle que para cada linea guarde los datos relacionados con ese socio
    for linea in lines:
        
        abonado = False
        #separa por comas cada linea para poder almacenar los datos
        data = linea.split(", ")
        
        if linea.startswith("$"):
            dni = data[0][1:]
        
        elif linea.startswith("@"):
            abonado = True
            dni_abonado = data[0][1:]
            posicion_socio = tree.find_position(dni_abonado)
            posicion_socio.value().setAbonado(socio(dni_abonado, str(data[1]+", "+data[2]), data[3], data[4]))
            
        else: 
            dni = data[0]
        
        #vamos añadiendo cada socio con sus determinados datos al arbol
        if not abonado:
            
            tree[dni] = socio(dni, str(data[1]+", "+data[2]), data[3], data[4])
     
        
        
    preorder_indent_BST(tree,tree.root(),0)
    return tree   
    


def grafting(arbol_1, arbol_2):
    """Función encargada de unificar los integrantes de los arboles en un fichero de texto"""
    
    # Copiamos en arbol 1 en el arbol final
    arbol_final = arbol_1
    
    p = arbol_2.first()
    
    while p is not None:
        
        key = p.key()
        value = p.value()  
        
        if check_key(arbol_final, key):
           
            abonados_2 = value.getListaAbonados()
            
            position_final = arbol_final.find_position(key)
            abonados_final = position_final.value().getListaAbonados()
            
            tmp = []
            
            for i in abonados_final:
                tmp.append(i.getNombre())
            
            for item in abonados_2:
                if item.getNombre() not in tmp:
                    abonados_final.append(item)
            
        else:
            arbol_final[key] = value
         
        
        p = arbol_2.after(p)
   
    
    print("\nARBOL FINAL:")
    preorder_indent_BST(arbol_final,arbol_final.root(),0)
    
    return arbol_final



def check_key(arbol, clave):
    
    position = arbol.find_position(clave)
    
    if position is None:
        return False
    
    elif position.key() == clave:
        return True
    
    else:
        return False
  
    
    
def preorder_indent_BST(T, p, d):
    """Print preorder representation of a binary subtree of T rooted at p at depth d.
    To print aTree completely call preorder_indent_BST(aTree, aTree.root(), 0)"""
    if p is not None:
        # use depth for indentation
        print(2*d*' ' + "(" + str(p.key()) + "," +  str(p.value().getNombre()) + str(p.value().getNombreAbonado()) + ")") 
        
        
        preorder_indent_BST(T, T.left(p), d+1) # left child depth is d+1
        preorder_indent_BST(T, T.right(p), d+1) # right child depth is d+1
        
        
        
def chop_down(arbol):
    
    p = arbol.first()
    
    file = "equipoFINAL.txt"
    
    # eliminamos el contenido del fichero
    with open (file, "w") as r:
        r.write("")
         
    while p is not None:
        
        value = p.value()

        with open (file, "a") as f:
            
            if len(value.getListaAbonados()) == 0:
                
                precio = prices(value.getUbicacion(), 0)
                personal_data = "{}, {}, {}, {}, {}€".format(value.getDni(), value.getNombre(), value.getFecha(), value.getUbicacion(), precio)
                f.write(personal_data)  
            
            else:
                precio = prices(value.getUbicacion(), len(value.getListaAbonados()))
                personal_data_s = "${}, {}, {}, {}, {}€".format(value.getDni(), value.getNombre(), value.getFecha(), value.getUbicacion(), precio)
                f.write(personal_data_s)
                f.write("\n")
                
                for abonado in value.getListaAbonados():
                    personal_data_a = "@{}, {}, {}, {}".format(abonado.getDni(), abonado.getNombre(), abonado.getFecha(), value.getUbicacion())
                    f.write(personal_data_a) 
                    if value.getListaAbonados().index(abonado) < len(value.getListaAbonados()) - 1:
                        f.write("\n")
                    
            p = arbol.after(p)
            
            if p is not None:
                f.write("\n")
        
def prices(ubicacion, abonados):
    
    if ubicacion == "tribuna":
        cuota = 2024
    
    elif ubicacion == "preferencia":
        cuota = 1609
    
    elif ubicacion == "fondoNorte":
        cuota = 1101
        
    else:
        cuota = 660
        
    precio = cuota + int(abonados)*cuota/2
    
    return precio

    
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
    
    ascii_code = 65
    
    lista_arboles = []
    
    for i in range(n_equipos):
        name = chr(ascii_code)
        n_socios = random.randint(minimo_socios, maximo_socios)
        random_txt(name, n_socios)
        lista_arboles.append(forest(name))
        
        ascii_code += 1
    
    
    while len(lista_arboles) > 1:
        
        arbol1 = lista_arboles.pop(0)
        arbol2 = lista_arboles.pop(0)
        arbol_final = grafting(arbol1, arbol2)
        lista_arboles.append(arbol_final)
    

    chop_down(arbol_final)
    

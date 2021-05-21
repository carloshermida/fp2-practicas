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



def start_teams():
    random_txt("A", 3)
    random_txt("B", 5)



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
    print("ARBOL: {}".format(team))
    
    #creamos un bucle que para cada linea guarde los datos relacionados con ese socio
    for linea in lines:
        #separa por comas cada linea para poder almacenar los datos
        data = linea.split(", ")
        #vamos añadiendo cada socio con sus determinados datos al arbol
        tree[data[0]] = socio(data[0], str(data[1]+", "+data[2]), data[3], data[4])
        #preorder_indent_BST(tree,tree.root(),0)
        #print("\n")
        
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
        
        if not check_key(arbol_final, key):
            
            arbol_final[key] = value
            #if arbol_final.find_position(key).value() != value:
                
        p = arbol_2.after(p)
    print("ARBOL FINAL: \n")
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
        print(2*d*' ' + "(" + str(p.key()) + "," +  str(p.value()) + ")") 
        preorder_indent_BST(T, T.left(p), d+1) # left child depth is d+1
        preorder_indent_BST(T, T.right(p), d+1) # right child depth is d+1
        
        
        
def chop_down(arbol):
    
    p = arbol.first()
    
    file = "equipo{}.txt".format("C")
    
    # eliminamos el contenido del fichero
    with open (file, "w") as r:
        r.write("")
         
    while p is not None:
        
        value = p.value()

        with open (file, "a") as f:
            personal_data = "{}, {}, {}, {}".format(value.getDni(), value.getNombre(), value.getFecha(), value.getUbicacion())
            f.write(personal_data)
            
            p = arbol.after(p)
            if p is not None:
                f.write("\n")
        
            
    
    
    
if __name__ == "__main__":
    
    #start_teams()
    
    arbol_A = forest("A")
    arbol_B = forest("B")
    
    arbol_final = grafting(arbol_A, arbol_B)

    chop_down(arbol_final)
    
    


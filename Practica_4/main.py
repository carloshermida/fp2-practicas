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
#from random_people import random_txt 

#creamos la funcion forest que será le encargada de crear los arboles
def forest(team):
    """Función encargada de crear aarboles a partir de un fichero de texto"""   
    #nombremos la variable file para llamar a el archivo de texto donde se encuentran los datos de los socios de determinado club
    file = "equipo{}.txt".format(team)
    
    #leemos el contenido de dicho archivo
    with open (file, "r") as f:
        contenido = f.read()
    
    #lo dividimos en lineas al separarlo por los saltos de linea
    lines = contenido.split("\n")
    
    #print("Insertamos las claves en orden")
    tree = AVL()
    #print("Árbol vacío"); preorder_indent_BST(tree,tree.root(),0)
    print("ARBOL: {}".format(team))
    
    #creamos un bucle que para cada linea guarde los datos relacionados con ese socio
    for linea in lines:
        #separa por comas cada linea para poder almacenar los datos
        data = linea.split(", ")
        #definimos la varibale dni que nos hara de clave 
        dni = int(data[0][0:-2])
        
        #print("Insertamos", dni)
        #vamos añadiendo cada socio con sus determinados datos al arbol
        tree[dni] = socio(data[0], str(data[1]+", "+data[2]), data[3], data[4])
        #preorder_indent_BST(tree,tree.root(),0)
        #print("\n")    
    preorder_indent_BST(tree,tree.root(),0)
    return tree   
    
def talar(arbol1, arbol2):
    """Función encargada de unificar los integrantes de los arboles en un fichero de texto"""
    # get item me devuelve el valor
    for i in range(__len__(arbol1)):
        __getitem__()
def preorder_indent_BST(T, p, d):
    """Print preorder representation of a binary subtree of T rooted at p at depth d.
    To print aTree completely call preorder_indent_BST(aTree, aTree.root(), 0)"""
    if p is not None:
        # use depth for indentation
        print(2*d*' ' + "(" + str(p.key()) + "," +  str(p.value()) + ")") 
        preorder_indent_BST(T, T.left(p), d+1) # left child depth is d+1
        preorder_indent_BST(T, T.right(p), d+1) # right child depth is d+1
    
if __name__ == "__main__":
    
    forest("A")
    forest("B")
    talar(forest)
    


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Main
# Carlos Hermida / Clara Lado

"""
Código principal de la Práctica 4.
"""

from partner import socio
from avl_tree import AVL

def garden(team):
    
    file = "equipo{}.txt".format(team)
    
    with open (file, "r") as f:
        contenido = f.read()
        
    lines = contenido.split("\n")
    
    print("Insertamos las claves en orden")
    tree = AVL()
    print("Árbol vacío"); preorder_indent_BST(tree,tree.root(),0)
    
    for linea in lines:
        data = linea.split(", ")
        dni = int(data[0][0:-2])
        
        print("Insertamos", dni)
        tree[dni] = socio(data[0], str(data[1]+", "+data[2]), data[3], data[4])
        preorder_indent_BST(tree,tree.root(),0)
        print("\n")
        
  
        
def preorder_indent_BST(T, p, d):
    """Print preorder representation of a binary subtree of T rooted at p at depth d.
    To print aTree completely call preorder_indent_BST(aTree, aTree.root(), 0)"""
    if p is not None:
        # use depth for indentation
        print(2*d*' ' + "(" + str(p.key()) + "," +  str(p.value()) + ")") 
        preorder_indent_BST(T, T.left(p), d+1) # left child depth is d+1
        preorder_indent_BST(T, T.right(p), d+1) # right child depth is d+1
    
if __name__ == "__main__":
    
    garden("A")
    


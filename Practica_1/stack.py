#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Definicion de las funciones
de la clase pila.
"""

class Empty(Exception):
  """Error intentando acceder a un elemento de un contenedor vacio."""
  pass

class ArrayStack:
  """Implementación de LIFO Stack usando una lista de Python como almacenamiento subyacente."""

  def __init__(self):
    """Crear una pila vacia.""" 
    self._data = []                       # instancia de lista no pública

  def __len__(self):
    """Devuelve el numero de elementos de una pila."""
    return len(self._data)

  def is_empty(self):
    """Devuelve verdadero si la pila esta vacia."""
    return len(self._data) == 0

  def push(self, e):
    """Añade un elemento e en la parte superior de la pila."""
    self._data.append(e)                  # nuevo elemento almacenado al final de la lista

  def peek(self):
    """Devuelve (pero no elimina) el elemento de la parte superior de la pila.

    Raise Empty exception si la pila esta vacia.
    """
    if self.is_empty():
      raise Empty('Pila vacia')
    return self._data[-1]                 # el ultimo elemento de la lista

  def pop(self):
    """Elimina y devuelve el elemento de la parte superior de la pila (i.e., LIFO).

    Raise Empty exception si la pila esta vacia.
    """
    if self.is_empty():
      raise Empty('Pila vacia')
    return self._data.pop()               # elimina el ultimo elemento de la lista

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Módulo Clase Paises
# Carlos Hermida / Clara Lado

"""
Definición de las funciones
de la clase pais
"""
 
class country:
    """"Definición de las funciones de la clase pais"""
    
    def __init__(self, nombre):
        """Crea un nuevo pais"""
        self.nombre = nombre
        self.puntos = 0
    
    def getNombre(self):
        """Devuelve el nombre"""
        return self.nombre
    
    def setPuntos(self, puntos):
        """Establece los puntos del pais"""
        self.puntos = puntos
        
    def getPuntos(self):
        """Devuelve los puntos"""
        return self.puntos
 
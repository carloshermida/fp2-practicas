#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Módulo Vacunas
# Carlos Hermida / Clara Lado

"""
Definición de las funciones
de la clase vacuna, persona.
"""
 
class Vacuna:
    """"Definición de las funciones de la clase Vacuna"""
   
    # Creamos una lista con todos los nombres de la vacunas cradas a partir de esta clase
    lista_vacunas = []
    
    def __init__(self, nombre, lim_inf, lim_sup, entrada_diaria, stock, vacunados, no_vacunados):
        """Crea una nueva vacuna"""
        self.nombre = nombre
        self.lim_inf = lim_inf
        self.lim_sup = lim_sup
        self.stock = stock
        self.vacunados = vacunados
        self.no_vacunados = no_vacunados
        self.entrada_diaria = entrada_diaria
        # Cada vez que se inicializa, añade a la lista el nombre de la vacuna
        Vacuna.lista_vacunas.append(self.nombre)
        
    def getNombre(self):
        """Devuelve el nombre"""
        return self.nombre
    
    def getLim_inf(self):
        """Devuelve el límite inferior"""
        return self.lim_inf
    
    def getLim_sup(self):
        """Devuelve el límite superior"""
        return self.lim_sup

    def getStock(self):
        """Devuelve el Stock de la vacuna"""
        return self.stock
    
    def getVacunados(self):
        """Devuelve el número de vacunados"""
        return self.vacunados
    
    def getEntrada(self):
        """Devuelve la entrada diaria de vacunas"""
        return self.entrada_diaria
    
    def setStock(self, stock):
        """Establece el Stock de la vacuna"""
        self.stock = stock
    
    def setVacunados(self, vacunados):
        """Establece el número de vacunados"""
        self.vacunados = vacunados
        
    def setNoVacunados(self, no_vacunados):
        """Establece el número de no vacunados"""
        self.no_vacunados = no_vacunados
    
    def getNoVacunados(self):
        """Devuelve el número de no vacunados"""
        return self.no_vacunados
    
    


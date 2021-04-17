#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Módulo Vacunas
# Carlos Hermida / Clara Lado

"""
Definición de las funciones
de la clase vacuna, persona.
"""
    
class Vacuna:
    
    def __init__(self, nombre, lim_inf, lim_sup, entrada_diaria, stock, vacunados, no_vacunados):
        self.nombre = nombre
        self.lim_inf = lim_inf
        self.lim_sup = lim_sup
        self.stock = stock
        self.vacunados = vacunados
        self.no_vacunados = no_vacunados
        self.entrada_diaria = entrada_diaria
        
    def getNombre(self):
        return self.nombre
    
    def getLim_inf(self):
        return self.lim_inf
    
    def getLim_sup(self):
        return self.lim_sup

    def getStock(self):
        return self.stock
    
    def getVacunados(self):
        return self.vacunados
    
    def getEntrada(self):
        return self.entrada_diaria
    
    def setStock(self, stock):
        self.stock = stock
    
    def setVacunados(self, vacunados):
        self.vacunados = vacunados
        
    def setNoVacunados(self, no_vacunados):
        self.no_vacunados = no_vacunados
    
    def getNoVacunados(self):
        return self.no_vacunados
    



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
    
    def __init__(self, nombre, lim_inf, lim_sup, entrada_diaria):
        """Crea una nueva vacuna"""
        self.nombre = nombre
        self.lim_inf = lim_inf
        self.lim_sup = lim_sup
        self.stock = 0
        self.vacunados = 0
        self.no_vacunados = 0
        self.entrada_diaria = entrada_diaria
        self.vacunados_total = 0
        # Cada vez que se inicializa, añade a la lista el nombre de la vacuna
        Vacuna.lista_vacunas.append(self.nombre)
        self.lista_diaria_vac = []
        self.lista_diaria_no_vac = []
        
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
        """Devuelve el número de vacunados diario"""
        return self.vacunados
    
    def getEntrada(self):
        """Devuelve la entrada diaria de vacunas"""
        return self.entrada_diaria
    
    def setStock(self, stock):
        """Establece el Stock de la vacuna"""
        self.stock = stock
    
    def setVacunados(self, vacunados):
        """Establece el número de vacunados diario"""
        self.vacunados = vacunados
        
    def setNoVacunados(self, no_vacunados):
        """Establece el número de no vacunados diario"""
        self.no_vacunados = no_vacunados
    
    def getNoVacunados(self):
        """Devuelve el número de no vacunados diario"""
        return self.no_vacunados
    
    def getVacunados_total(self):
        """Devuelve el número de vacunados total"""
        return self.vacunados_total
    
    def setVacunados_total(self, vacunados_total):
        """Establece el número de vacunados total"""
        self.vacunados_total = vacunados_total
    
    def set_lista_vac(self, x):
        """Guarda en una lista los vacunados de cada día"""
        self.lista_diaria_vac.append(x)
    
    def set_lista_no_vac(self, x):
        """Guarda en una lista los no vacunados de cada día"""
        self.lista_diaria_no_vac.append(x)
        
    def get_lista_vac(self):
        """Devuelve una lista los vacunados de cada día"""
        return self.lista_diaria_vac
    
    def get_lista_no_vac(self):
        """Devuelve en una lista los no vacunados de cada día"""
        return self.lista_diaria_no_vac
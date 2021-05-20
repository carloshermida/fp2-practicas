#!/usr/bin/env python3
# -- coding: utf-8 --

# Socios
# Carlos Hermida / Clara Lado

"""
Definición de las funciones
de la clase socio
"""
 
from datetime import date, datetime

def calcular_edad(fecha_nacimiento):
    """ calcula la edad en años de una persona que ha nacido 
        en la fecha indicada en el parametro de tipo date fecha_nacimiento """
    # obtenemos la fecha actual
    hoy = date.today()
    # restamos los años
    resultado = (hoy.year - fecha_nacimiento.year)
    # ajustamos por mes y día
    resultado -= ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return resultado
    

class socio:
    """"Definición de las funciones de la clase socio"""
    
    def __init__(self, dni, nombre, fecha_de_nacimiento, ubicacion):
        """Crea un nuevo socio"""
        
        self.dni = dni
        self.nombre = nombre
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.ubicacion = ubicacion
        
    def getNombre(self):
        """Devuelve el nombre"""
        return self.nombre
    
    def getDni(self):
        """Devuelve el nombre"""
        return self.dni
    
    def getFecha(self):
        """Devuelve el nombre"""
        return self.fecha_de_nacimiento
    
    def getEdad(self):
        """Devuelve la edad del socio"""
        fecha = datetime.strptime(self.fecha_de_nacimiento, "%d/%m/%Y")
        return calcular_edad(fecha)
    
    def getUbicacion(self):
        """Devuelve el nombre"""
        return self.ubicacion
    
    

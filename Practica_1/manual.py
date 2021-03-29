#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Módulo Manual
# Carlos Hermida / Clara Lado

"""
Contiene el manual de usuario que 
permite el correcto uso del programa.
"""

def mostrar_manual():
    """Imprime por pantalla el manual de usuario."""
    
    print("="*35, "\n", "\t\tManual de usuario", "\n", "="*35, "\n", sep="")
    print("\
La correcta interpretación de este manual permitirá que\n\
el usuario obtenga los resultados esperados.\n\n\
\
- Requerimientos al usuario:\n\n\
    Es imprescindible que escriba la operacion deseada sin\n\
    espacios. Una vez escrito el cálculo que se quiere realizar,\n\
    pulsar la tecla enter.\n\n\
\
    Las operaciones básicas son: suma (+), resta (-), multiplicación (*),\n\
    división (/) y elevado a (**).\n\n\
\
    Hemos implementado una serie de códigos que identifican distintas\n\
    operaciones más complejas. Para procesarlas correctamente, escriba\n\
    por ejemplo: s(34). En este caso, el programa calculará el seno de 34.\n\n\
\
        - s() -> seno\n\
        - c() -> coseno\n\
        - t() -> tangente\n\
        - x() -> arcseno\n\
        - k() -> arccoseno\n\
        - a() -> arctangente\n\
        - r() -> raíz caudrada\n\n\
\
    En el caso de números negativos, debe introducirlos siempre\n\
    entre paréntesis. Por ejemplo: (-3)\n\n\
\
- Funcionamiento del programa:\n\n\
    Al introducir una expresión infija, el programa evaluará su correcta\n\
    escritura y devolverá un error si un requerimiento del usuario no se cumple.\n\
    Si todo está correcto, transformará la expresión infija introducida en una \n\
    expresión infija espaciada. En el caso de números negativos, los cambiará por \n\
    una resta de 0 - x, siendo x el valor absoluto del número negativo introducido.\n\
    Acto seguido, pasará la expresión a postfijo, tranformando los números decimales\n\
    en fracciones con el denominador múltiplo de 10 correspondiente. Finalmente, \n\
    realiza las operaciones en el orden especificado por el usuario.")
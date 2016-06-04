#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Este es solo un codigo para mostrar a los usuarios como se usan los operadores de comparación, no doy por hecho que es la mejor forma de usar las condicionales.
"""
semaforo = input("¿En que color esta el semaforo? ")

if semaforo == 'verde':

    print ("puedes seguir")

elif semaforo == 'amarillo':

    print ("frenar")

elif semaforo == 'rojo':

    print ("Detener el auto")

if 'pez' != 'perro':

    print ("Es Correcto")

else:

    print ("incorrecto")

if 10 < 23:	
    
    print ("Es menor")

else: 
  
    print ("Es mayor")    

if 10 >= 3:
    print ("Si es mayor")

else: 

    print ("Lo siento, es menor")

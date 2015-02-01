#!/usr/bin/python
# -*- coding: utf-8 -*-

fichero = open("/etc/passwd", "r")
#Guardamos en una lista cada linea del fichero.

numeroLineas = fichero.readlines()
print ""

#Creamos un diccionario.

diccionario = {}

for lineas in numeroLineas:
	frase = lineas.split(":")
	nombreUsuario = frase[0]
	nombreShell = frase[-1][:-1]
	diccionario[nombreUsuario] = nombreShell 
	
	Idroot = diccionario["root"]
	print "Tamaño diccionario" + len(diccionario)

	#Identificador de usuario, y shell que utiliza ese identificador de usuario.

	print "Identificador de usuario: " + frase[0] + " =>Shell: " + frase[-1][:-1]

#Número de usuarios para esta máquina.

print "\n" + "Número de usuarios de la máquina " + str(len(numeroLineas))

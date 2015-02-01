#!/usr/bin/python
# -*- coding: utf-8 -*-

fichero = open("/etc/passwd", "r")

#Guardamos en una lista cada linea del fichero.
numeroLineas = fichero.readlines()
print ""

#Creamos un diccionario.
diccionario = {}

contador = 0
for lineas in numeroLineas:
	frase = lineas.split(":")
	if contador == 0:
		idRoot = frase[0]
	contador = contador + 1
	nombreUsuario = frase[0]
	nombreShell = frase[-1][:-1]
	diccionario[nombreUsuario] = nombreShell 
	
shellRoot = diccionario["root"]
longitudDic = str(len(diccionario))
	
#Identificador de usuario, y shell que utiliza ese identificador de usuario.
print "Identificador de usuario: " + idRoot + " => Shell: " + shellRoot

#Número de usuarios para esta máquina.
print "\n" + "Número de usuarios de la máquina = " + longitudDic

#Control de excepcion.
try: 
	print diccionario["imaginario"]
except KeyError:
	print ""
	print "El identificador de usuario 'imaginario' no existe"


#!/usr/bin/python
# -*- coding: utf-8 -*-

fichero = open("/etc/passwd", "r")
#Guardamos en una lista cada linea del fichero.

numeroLineas = fichero.readlines()
print ""

for lineas in numeroLineas:
	frase = lineas.split(":")
	#Identificador de usuario, y shell que utiliza ese identificador de usuario.

	print "Identificador de usuario: " + frase[0] + " =>Shell: " + frase[-1][:-1]
#Número de usuarios para esta máquina.

print "\n" + "Número de usuarios de la máquina " + str(len(numeroLineas))




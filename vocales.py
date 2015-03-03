import sys as sys
import unicodedata

n = int(sys.argv[1])
lineas = []


file = open("Sainte-Beuve.txt", "r")

for i in range(n):
	lineas.append(file.readline())

for i in range(len(lineas)):
	linea = lineas[i]
	#Eliminar mayuscula
	linea = linea.lower()
	#Remocion de tildes
	linea = unicode(linea, "utf-8")
	unicodedata.normalize('NFKD', linea).encode('ascii','ignore')
	def elimina_tildes(s):
		return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
	linea = elimina_tildes(linea)

	


	if (linea[0] != "\n"):

		count = 0
		for j in range(len(linea)):
			letra = linea[j]
			if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
				count += 1
				
		print "El numero de vocales en la linea", (i+1), "es", count

	else:
		print "La linea", (i+1),"es vacia"



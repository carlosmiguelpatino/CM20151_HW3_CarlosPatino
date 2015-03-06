infile = open("Notas.csv", 'r')
outfile = open("Notas.dat", 'w')
linea =  infile.readline()

import os

linea = linea.replace(',T' , '+T')
#En esta version se escoge que el formato del encabezado sea Taller1 y no Taller 1. Sin embargo se presenta la linea de codigo necesaria para hacer lo contrario
linea = linea.replace('r,',  'r')
#linea =  linea.replace('r,' , 'r ')
outfile.write(linea)

for i in range(31):
	linea = infile.readline()
	linea = linea.replace(',', '+')
	outfile.write(linea)

infile.close()
outfile.close()

#No se si en la segunda parte del punto tocaba hacer esto
os.system('sed \'s/,T/!T/g\' Notas.csv > Notasterminaltmp1.dat')
os.system('sed \'s/r,/r/g\' Notasterminaltmp1.dat > Notasterminaltmp2.dat')
os.system('sed \'s/,/!/g\' Notasterminaltmp2.dat > Notasterminal.dat')
os.system('rm Notasterminaltmp1.dat')
os.system('rm Notasterminaltmp2.dat')





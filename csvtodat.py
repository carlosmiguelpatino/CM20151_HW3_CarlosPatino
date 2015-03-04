infile = open("Notas.csv", 'r')
outfile = open("Notas.dat", 'w')
linea =  infile.readline()

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


"""La solucion al problema es crear una serie de fibonacci porque
para saber las posibilidades hasta un escalon n se deben tener en cuenta
las posibilidades de llegar al anterior escalon y sumarlas. Tomando
este principio desde el escalon uno se obtiene una serie de fibonacci
ya que las posibilidades que hay para llegar un escalon n depende de
las posibilidades de llegar a los dos escalones anteriores. Se toman los
dos escalones anteriores ya que solo se pueden subir uno o dos
escalones a la vez."""

def posibilidades_escalera(n):

	if n == 0:
		posibilidades = 1
		print "No hay escalones para subir"
	elif n == 1:
		posibilidades = 1
	elif n == 2:
		posibilidades = 2
	else:
		posibilidades = posibilidades_escalera(n-1) + posibilidades_escalera(n-2)

	return posibilidades

#Para 13 escalones

posibilidades = posibilidades_escalera(13)
print "Hay",posibilidades, "maneras de subir una escalera de 13 escalones"

#Para 15 escalones

posibilidades = posibilidades_escalera(15)
print "Hay",posibilidades, "maneras de subir una escalera de 15 escalones"

def escaleras(A, B):
	resultados = []
	for i in range(len(A)):
		a = A[i]
		b = B[i]
		n = a % (2*b)
		resultado = posibilidades_escalera(n)
		resultados.append(resultado)
		

	return resultados

A = [4, 4, 5, 5, 1]
B = [3, 2, 4, 3, 1]

print escaleras(A, B)

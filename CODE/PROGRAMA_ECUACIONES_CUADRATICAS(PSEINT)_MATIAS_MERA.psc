Algoritmo Ecuacion_cuadratica
	Escribir 'Sea la formula: a*x^2+b*x+c=0'
	Escribir 'Ingrese los coeficientes'
	Leer a, b, c
	Si b^2-4*a*c>=0 Entonces
		x1 <- (-b+RC(b^2-4*a*c))/2*a
		x2 <- (-b-RC(b^2-4*a*c))/2*a
		Escribir 'Las raices serian:', x1, ' y ', x2
	SiNo
		Escribir 'Las raices complejas son:'
		Escribir -b/(2*a), '+', (RC(abs(b^2-4*a*c)))/2*a, 'i'
		Escribir -b/(2*a), '-', (RC(abs(b^2-4*a*c)))/2*a, 'i'
	FinSi
FinAlgoritmo

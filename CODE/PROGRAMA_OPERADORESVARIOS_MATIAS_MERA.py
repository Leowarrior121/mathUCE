"""Operadores en Python"""

"""1.-Operadores aritméticos"""
a = 3
b = 4
suma = a + b #esto es una suma/adicion
print('La suma de: ', a,'más', b,'es: ', suma)
resta = a - b #esto es una resta/sustraccion
print('La resta de: ', a,'menos', b,'es: ', resta)
multiplicacion = a * b #esto es una multiplicacion/producto
print('la multiplicacion de: ', a,'multiplicado por', b,'es: ', multiplicacion)
division = a / b #esto es una division/cociente
print('la division de: ', a,'divido para', b,'es: ', division)
division_entera = a // b #esto es una division entera
print('la division entera de: ', a,'divido para', b,'es: ', division_entera)
potenciacion = a ** b #esto es una potenciacion
print('la potenciacion de: ', a,' elevado a', b,'es: ', potenciacion)

#1.2-Operadores Relacionales
a = 5
b = 6
c = 2 
d = 1
print(a, 'es menor que', b, a < b)

#1.3-Operadores Lógicos
p= 5 > 2
q= 6 < 1
p or q
p and q
not p or q
not p and q
print('la proposición p o q es: ', p or q)
print('la proposicón p y q es: ',p and q)
print('la proposición not p o q es: ', not p or q)
print('la proposicón not p y q es: ',not p and q)

"""2.-Tipos de divisiones"""
#2.2-Entera:
27//14
#2.3-Decimal
27/14
#2.4-Módulo/porcentaje
27%14
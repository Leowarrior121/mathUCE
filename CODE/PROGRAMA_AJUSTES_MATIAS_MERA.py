print('Bienvenido al programa de ajustes')
print('Solo se admitiran valores para x, w, z en el rango (0,1)')
print('Tomando en cuenta que la fórmula es R=((8%*x/0.4%*w)+150%*z)^(0.2)')
x = float(input('Ingrese el valor de x:'))
w = float(input('Ingrese el valor de w:'))
z = float(input('Ingrese el valor de z:'))
R = ((0.08*x/(0.004*w))+(1.5*z))**0.2
print('El resultado es:')
print (R)

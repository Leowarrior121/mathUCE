print("Ingrese el largo en metros")
largo = float(input())
print("Ingrese el ancho en metros")
ancho = float(input())
area = largo * ancho
numero_baldosas = area / 0.003
costo_total=numero_baldosas * 3.5
print("El área es:",area, "metros cuadrados")
print("El número de baldosas para utilizarse es:", numero_baldosas)
print("El costo total es:", costo_total, "USD")
print("Gracias por usar nuestro programa, esperamos que los reultados hayan sido los adecuados")

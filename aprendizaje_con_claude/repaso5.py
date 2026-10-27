gastos = [12, 5, 8, 20, 15]
total = 0 
for gasto in gastos:
    total = total + gasto 

promedio = total / len(gastos)
print("El total de la compra fue de: " ,total)
print("El promedio de la compra fue de: " ,promedio)
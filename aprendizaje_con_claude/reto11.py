total = 0
with open("gastos.txt", "r") as archivo:
    for linea in archivo: 
        partes = linea.split()
        precio = int(partes[1])
        total = total + precio
    print("El total gastado es de: " ,total)
with open("gastos.txt", "r") as archivo:
    for linea in archivo:
        partes = linea.split()
        print(partes)
opcion = input(" 1.añadir gasto 2.Ver total 3.Salir: ")

while opcion != "3":
    if opcion == "1":
        gastos = input("Que compraste y su valor (3 para salir): ")
        with open("gastos.txt", "a") as archivo:
            archivo.write(gastos + "\n")
    elif opcion == "2":
        with open("gastos.txt", "r") as archivo:
            total = 0
            for linea in archivo:
                partes = linea.split()
                precio = int(partes[1])
                total = total + precio
            print("El total gastado es de: ", total)
    else:
        print("Opcion no valida")
    opcion = input(" 1. añadir gasto 2.Ver total 3.Salir: ")
print("Adios")
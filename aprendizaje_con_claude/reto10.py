archivo = open("gastos.txt", "a")
gastos = input("¿Qué compraste y cuánto costó? (n para salir): ")

while gastos  != "n":
    archivo.write(gastos + "\n")
    gastos = input("¿Qué compraste y cuánto costó? (n para salir): ")

archivo.close()
print("Listo, guardado")

archivo = open("gastos.txt", "r")
contenido = archivo.read()
archivo.close()
print(contenido)
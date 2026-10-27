archivo = open("notas.txt", "r")
contenido = archivo.read()
archivo.close()
print(contenido)
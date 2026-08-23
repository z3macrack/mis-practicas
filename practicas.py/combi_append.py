participanes = []
nombre = input("Nombre (o escribe 'salir' para terminar): ")
while nombre != "salir":
    participanes.append(nombre)
    nombre = input("Nombre (o escribe 'salir' para terminar):")
print(participanes)
print(len(participanes))

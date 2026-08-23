rifa = []

def calcular_total(cantidad_numero):
    return cantidad_numero * 6000

nombre = input("Nombre (o escribe 'salir' para terminar): ")
while nombre != "salir":
    cantidad = int(input("¿Cuantos numeros compró? "))
    total = calcular_total(cantidad)
    persona = {"nombre": nombre, "total": total}
    rifa.append(persona)
    nombre = input("Nombre (o escribe 'salir' para terminar): ")

for persona in rifa:
    print(f"{persona['nombre']} pagó ${persona['total']}")

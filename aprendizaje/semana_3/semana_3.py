contactos = []
nombre = input("Nombre (o escribe 'salir' para terminar):")

while nombre != "salir":
    telefono = int(input("Telofono (o escibre 'salir' para terminar):"))
    contacto = {"nombre": nombre, "telefono": telefono}
    contactos.append(contacto)
    nombre = input("Nombre (o escibre 'salir' para terminar):")

for contacto in contactos: 
    print(f"{contacto['nombre']} - {contacto['telefono']}")
print(len(contactos))
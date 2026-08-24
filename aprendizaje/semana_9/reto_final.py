class Persona:
    def __init__ (self, nombre, monto, pago):
        self .nombre = nombre
        self .monto = monto
        self .pago = pago

class Rifa:
    def __init__(self):
        self .participantes = []
    def agregar(self, persona):
        self .participantes.append(persona)
    def total_recaudado(self):
        suma = 0 
        for persona in self.participantes:
            if persona .pago == True:
                suma = suma + persona.monto
            return suma

mi_rifa = Rifa()
nombre = input("Nombre (o escribre 'salir' para terminar):")
while nombre != "salir":
    numeros = int(input("¿Cuantos numeros compro?"))
    monto = numeros * 6000
    respuesta = input("¿Ya pago? (si/no):")
    pago = respuesta == "si"
    nueva_persona = Persona(nombre, monto, pago)
    mi_rifa.agregar(nueva_persona)
    nombre = input("Nombre (o escribe 'salir' para terminar):")

print(f"Total_recaudado: ${mi_rifa.total_recaudado()}")
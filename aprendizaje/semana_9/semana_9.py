class Persona:
    def __init__(self, nombre, monto, pago):
        self .nombre = nombre
        self .monto = monto
        self .pago = pago

class Rifa:
    def __init__(self):
        self .participantes =[]
    def agregar(self, persona):
        self .participantes.append(persona)
    def total_recaudado(self):
        suma = 0
        for persona in self.participantes:
            if persona .pago == True:
                suma = suma + persona.monto
            return suma

mi_rifa = Rifa()

persona1 = Persona("Marshall", 6000, True)
persona2 = Persona("Emanuel", 3000, False)

mi_rifa.agregar(persona1)
mi_rifa.agregar(persona2)

print(mi_rifa.total_recaudado())
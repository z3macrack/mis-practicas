class Persona: 
    def __init__(self, nombre, monto, pago):
        self .nombre = nombre
        self .monto = monto
        self .pago = pago 
    def ya_pago(self):
        return self .pago
marshall = Persona ("Marshall", 6000, True)
print(marshall.nombre)
print(marshall.monto)
print(marshall.ya_pago())
rifa = [
    {"nombre": "Marshall", "monto": 6000, "pago": True}, 
    {"nombre": "Camila", "monto": 3000, "pago": False},
    {"nombre": "Janisa", "monto": 5000, "pago": False}
]
def verificar_pago (persona):
    if persona ["pago"] == True:
        print(persona["nombre"], "ya pago")
    else: 
        print(persona["nombre"], "debe")
for persona in rifa:
    verificar_pago(persona)
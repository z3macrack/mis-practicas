rifa = [
    {"nombre": "Emanuel", "monto": 6000, "pago": True},
    {"nombre": "Janisa", "monto": 3000, "pago": False},
    {"nombre": "Fernando", "monto": 6000, "pago": True},
    {"nombre": "Sara", "monto": 3000, "pago": False}
]

def total_recaudado():
    suma = 0
    for persona in rifa:
        if persona ["pago"] == True:
            suma = suma + persona["monto"]
    return suma 
total = total_recaudado()
print(f"El total recaudado es $ {total}")
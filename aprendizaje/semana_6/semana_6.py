import json 
rifa = [
    {"nombre": "Emanuel", "monto": 6000, "pago": True},
    {"nombre": "Maria Belen", "monto": 3000, "pago": False},
    {"nombre": "Janisa", "monto": 6000, "pago": False},
    {"nombre": "Alexa", "monto": 3000, "pago": True}
]
archivo = open("rifa.json", "w")
json.dump(rifa, archivo, indent=4)
archivo.close()
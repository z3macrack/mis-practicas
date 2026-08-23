import json
archivo = open("rifa.json", "r")
rifa = json.load(archivo)
archivo.close
for persona in rifa:
    print(f"{persona['nombre']} - ${persona['monto']}")
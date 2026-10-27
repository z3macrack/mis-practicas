precios = {"pan": 2000, "leche": 4500, "huevos": 12000}
total = 0
for clave in precios:
    total = total + precios[clave]
    print(clave, precios[clave])

print("La suma total es de:",total)
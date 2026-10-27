def promedio(lista):
    total = 0
    for numero in lista:
        total = total + numero
    return  total / len(lista)

print(promedio([12, 5, 8, 20, 15]))
print(promedio([7, 9, 5, 10, 8]))
nombre = input("Como te llamas? ")
nacimiento = int(input("introduce el año de tu nacimiento "))
edad = 2026 - nacimiento
if edad >= 18:
    print(nombre, "eres mayor de edad")
else:
    print(nombre,"menor de edad")
    mayoria =  18 - edad
    print("te faltan" , mayoria, " años para ser mayor de edad")

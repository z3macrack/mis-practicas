numero_valido = False

while numero_valido == False:
    try: 
        edad = int(input("¿Cuantos años tienes? "))
        numero_valido = True
        print("El proximo año tendras" , edad + 1)
    except ValueError:
        print("Eso no es un numero")
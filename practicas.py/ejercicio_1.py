def verificar_pago (nombre, monto):
    if monto >= 6000: 
        print(nombre, "ya pago completo")
    else:
        print(nombre, "pago incompleto")
verificar_pago("Marshall", 6000)
verificar_pago("Camila", 3000)

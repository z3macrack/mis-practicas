tareas = [
    {"nombre": "lavar la ropa", "hecha": True},
    {"nombre": "doblar la ropa", "hecha": False},
    {"nombre": "hacer el aseo", "hecha": True}
]
def verificar_tarea(tarea):
    if tarea ["hecha"] == True:
        print("La tarea esta realizada")
    else:
        print("tarea no esta realizada")
for tarea in tareas:
    verificar_tarea(tarea)
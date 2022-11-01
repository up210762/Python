def Urnas(urnas):
    cantidad = []
    for i in range(urnas):
        x = str(input(f"Escribe el nombre de la urna {i}: "))
        cantidad.append(x)
    return cantidad

def Muestras(Muestras):
    muestras = []
    for i in range(Muestras):
        x = str(input(f"Escribe el numbre del objeto {i}: "))
        muestras.append(x)
    return muestras

def Elementos(Elementos):
    elementos = []
    for i in range(Elementos):
        x = str(input(f"Escribe el nombre del elemento {i}: "))
        elementos.append(x)

urnas = int(input("Cuantas urnas tienes: "))
elemetos = str(input("¿Qué elementos hay? "))
catMuetras = int(input("¿Cuántas muestras tienes? "))


"""
anchura = int(input("Anchura del triángulo: "))
for i in range(1,anchura + 1):
    for j in range(i):
        print("* ", end = "")
    print()

for i in range(1, anchura):
    for j in range(anchura - i):
        print("* ", end = "")
    print()

anchura = int(input("Anchura del triángulo: "))
for i in range(1, anchura + 1):
    for j in range(i):
        print("* ", end = "")

for i in range(1, anchura):
    for j in range(anchura - 1):
        print("* ", end = "")

for i in range(1, anchura - 1):

#Ejercicio 1
def centrar(cad):
    print(" " * int(40 - (len(cad)/2)), cad)
    print(" " * int(40 - (len(cad)/2)),"=" * len(cad))

mensaje1 = "Un mensaje centrado"
centrar(mensaje1)
mensaje2 = "Otro anime"
centrar(mensaje2)

#Ejercicio 2
def Multiplo(Num1, Num2):
    if Num1%Num2 == 0:
        print(f"El número {Num1} es multiplo de {Num2}")
    else:
        print(f"El número {Num1} no es multiplo de {Num2}")

Num1 = int(input("Escribe el primer número: "))
Num2 = int(input("Escribe el segundo número: "))

Multiplo(Num1, Num2)
"""

operacion = []
operacion.append("+")

print(operacion)
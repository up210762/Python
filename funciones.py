def area_circulo(r):
    area = 3.1415*r**2
    return area

diametro = 10
area = area_circulo(diametro/2)
print(f"Área del círculo de diámetro {diametro} es {area}")

def area_cilindro(r,h):
    pi = 3.14159
    area = 2*pi*r**2 + 2*pi*r*h
    return area

radio = 1
altura = 4.5
area_c = area_cilindro(radio, altura)
print(f"El área del cilindro de radio {radio} y altura {altura} es {area_c}.")

def min_max(lista):
    mn = mx = lista[0]
    for elem in lista[1:]:
        if mn > elem:
            mn = elem
        elif mx < elem:
            mx = elem
    return mn, mx
lista_prueba = [1, 10, 2, -3, 6, 8]
mn, mx = min_max(lista_prueba)
print(f"Los valores extremos de la lista {lista_prueba} son:\nMin: {mn} Max: {mx}")

def Mayuscula(x):
    mayuscula = cadena1.upper()
    print(mayuscula)

def Minuscula(x):
    minuscula = cadena2.lower()
    print(minuscula)

def Invertir(x):
    invertido = cadena3.swapcase()
    print(invertido)

for i in range(0,3):
    if i == 0:
        cadena1 = str(input("Escribe una palabra: "))
        Mayuscula(cadena1)
    elif i == 1:
        cadena2 = str(input("Introduce otra palabra: "))
        Minuscula(cadena2)
    elif i == 2:
        cadena3 = str(input("Introduce la ultima palabra: "))
        Invertir(cadena3)

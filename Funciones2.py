def Fun_Ecuacion(x):
    y = (x**2)-(8*x)+15
    return y

#entrada = float(input('Escribe el valor de "x" para la ecuación: '))
#y = Fun_Ecuacion(entrada)
#print(f'El resultado de la ecuación donde "x" vale {entrada} es {y}')

x1 = 4
x2 = 7
i = 0
Es = 0.0001
Er = abs(x2-x1)

while Er > Es:
    xm = (x1 + x2)/2
    y1 = Fun_Ecuacion(x1)
    y2 = Fun_Ecuacion(xm)
    if y1*y2 < 0:
        x2 = xm
    else:
        x1 = xm
    Er = abs(x2-x1)
    i = i + 1
    print(f'{i} | {x1} | {x2} | {Er} | {xm} | {Fun_Ecuacion(x1)} | {Fun_Ecuacion(x2)}')
print(f'i = {i}, raiz = {xm}\nHecho . . .')

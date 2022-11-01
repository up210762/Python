import random
moneda = [1,2]
dado = [1, 2, 3, 4, 5, 6]
resultado = []
calidad = random.randint(0, 6)
for i in range(len(dado)):
    if calidad % 2 == 0:
        print(f"El valor del dado es: {calidad}")
        for j in range(2):
            Val = random.randint(moneda[i])
            resultado.append(Val)
    if calidad % 2 != 0:
        print(f"El valor del dado es: {calidad}")
        Val = random.randint(moneda[i], 1)
        resultado.append[Val]
print(f"Los resultados son: {resultado}")
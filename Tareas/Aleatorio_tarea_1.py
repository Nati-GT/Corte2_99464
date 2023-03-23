import random 

def Aleatorio():
    num = random.randint(100, 120)
    while num in [110, 115, 119]:
        num = random.randint(100, 120)
    return num

numeros = []
for i in range(10):
    numeros.append(Aleatorio())

contador = 0
for i in range(10):
    if contador % 2 == 1:
        print(numeros[i])
    contador += 1

contador = 0
for i in range(10):
    if contador % 2 == 0:
        print(numeros[i])
    contador += 1
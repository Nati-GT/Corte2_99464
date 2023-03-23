n=input('ingrese un numero: ')
dimension=len(n)
contador=0

#if dimension <2 and dimension >8
if 2<dimension<8:
    for i in n:
        if int(i) ==5:
            print("salto")
            contador+=1
        else:
            print(i)
    print(f'Numeros iguales a 5: {contador}')
    print(f'Numeros diferentes a 5: {dimension-contador}')
    print(f'total de digitos: {dimension}')
else:
    print('error fuera de rango')



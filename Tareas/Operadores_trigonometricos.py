

def coseno(valor_grados):
   
    valor_radianes = valor_grados * (3.14159 / 180)
    resultado = 0
    termino = 1
    signo = 1
    for n in range(1, 10):
        resultado += termino * signo
        termino *= -1 * valor_radianes**2 / ((2*n-1)*(2*n))
        signo *= -1
    return resultado

def tangente(valor_grados):
   
    valor_radianes = valor_grados * (3.14159 / 180)
    return seno(valor_radianes) / coseno(valor_radianes)

def exponencial(valor):
   
    resultado = 1
    termino = 1
    for n in range(1, 10):
        termino *= valor / n
        resultado += termino
    return resultado

def logaritmo_natural(valor):
    
    resultado = 0
    termino = (valor - 1) / valor
    for n in range(1, 10):
        resultado += termino / n
        termino *= (valor - 1) / valor
    return resultado

valor_grados = float(input("Ingrese el valor en grados: "))
funcion = input("Ingrese la función a aplicar (seno, coseno, tangente, exponencial o logaritmo): ")
print('escoja una de las siguietes opciones: \n')
print('1. for in range(final)')
print('2. for in range(inicio,final)')
print('3. for in range(inicio, final,paso) ')

opc=input('Escoja una opcion')
if opc =='1':
   
elif opc=='2':
    for i in range(5,10):
        print(i+1)
    print('fin del proceso')
elif opc=='3':
    for i in range(30,10,-2):
        print(i)
    print('fin del proceso')
    pass

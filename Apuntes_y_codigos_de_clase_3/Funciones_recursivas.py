def imprimir(x):
    if x>0:
        imprimir(x-1)
        print(x)
    else:
        print(f'finalizo {x}')

def cuenta_atras(num):
    num-=1
    if num >0:
        print(num)
        cuenta_atras(num)
    else: 
        print("Boooooo!")
    print("Fin de la funcion", num)
cuenta_atras(5) 
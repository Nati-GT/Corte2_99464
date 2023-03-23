import random as rand 

def matrices(filas,columnas):
    matriz=[]
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            #num=int(input(f'ingrese el numero de las posiciones [{i},{j}]: ')) 
            num=rand.randint(1,10) #para generar la matriz aleatoria
            matriz[i].append(num)
    return matriz 

def escalar(matriz,n):
    for i in matriz:
        for j in range(len(i)):
            i[j]=n*i[j]
    print(matriz)

def app():
        filas=int(input('ingrese el numero de filas: '))
        columnas=int(input('ingrese el valor de columnas: '))
        matriz= matrices(filas,columnas)
        print(matriz)
        n=int(input('ingrese un numero para escalar la matriz'))
        escalar(matriz,n) 



if __name__=="__main__":
    app()  

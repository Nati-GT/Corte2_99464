def main():
    dicc={}
    f=open("matrizAsignacion.txt",'rt')
    matriz= f.readlines()
    f.seek(0)
    suma=0
    #print(len(matriz))
    for i in range(len(matriz)):
        #print(f.readline().rstrip('\n').split(','))
        valor=f.readline().rstrip('\n').split(',')
        for j in range(len(valor)):
            pos=str(f'{i}{j}')
            dicc[pos]= valor[j]
        

        #print(valor)
        # suma +=int(valor[0]) #suma los valores de cada fila posicion 0
        # print(suma)
    #print(suma)
    print(dicc)
    #print(f'la posicion 4,3 es {dicc["43"]}')
    print('43' in dicc)
    f.close()
   
        

    
    #matriz= f.read() #lee el archivo completo
    #matriz= f.readline() #Lee e imprime una sola linea
    #matriz= f.readlines() #lee e imprime en forma de lista
    # print(matriz)


        

if __name__=="__main__":
    main()
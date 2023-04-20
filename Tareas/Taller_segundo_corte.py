def lectura():
    f= open('organization_data.csv','rt')
    data = [] 
    linea = f.readline()
    while linea !='':
        data.append(linea.rstrip('\n').split(','))
        linea= f.readline()
    f.close()
    return data 

def Orden_Paises(data): 
    paises=[]
    for i in data:
        country =i[4]
        if country not in paises:
            paises.append(country)
    paises.sort()
    print(len(paises))

def busqueda(data,paises):
    search= int(input('ingrese el indice de un pais'))
    compañias= []
    for i in data:
        if i[4] == paises[search]:
            compañias.append(i)
    print(compañias)
    print(paises.append)



def main():
    data=lectura()
    paises=Orden_Paises(data)
    busqueda(data,paises)


if __name__=="__main__":
    main()
    
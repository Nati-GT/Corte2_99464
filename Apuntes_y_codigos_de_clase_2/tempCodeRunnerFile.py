milista=[3,5,7,5]
opc=''
while opc!='salir':
    opc= input('¿que metodo desea utilizar? ')
    if opc=='borrar':
        dato=int(input('¿cual dato quiere borrar? '))
        milista.remove(dato)
        print(milista)
    elif opc=='agregar':
        dato= int(input('¿cual es el dato que quiere agregar? '))
        milista.append(dato)
        print(milista)
    elif opc=='buscar':
        dato=int(input('¿cual dato quiere buscar? '))
        pos=milista.index(dato)
        print(f'el indice es {pos}')
    elif opc=='limpiar':
        milista.clear()
        print(milista)
    elif opc=='insertar':
        dato=int(input('¿cual dato quiere inserta? '))
        idx=int(input('ingrese un indice: '))
        milista.insert(idx,dato)
        print(milista)
    elif opc=='sacar':
        idx=int(input('indice del numero a sacar: '))
        milista.pop(idx)
        print(milista)
    elif opc=='comparar':
        print(f' el valor maximo de la lista es: {max(milista)}')
        print(f' el valor minimo de la lista es: {min(milista)}')
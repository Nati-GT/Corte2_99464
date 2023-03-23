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
    elif opc=='contar':
        dato=int(input('¿que numero desea revisar? '))
        con= milista.count(dato)
        print(f'el numero {dato} esta {con} veces en la lista')
    elif opc=='sumar':
        print(f'los elementos de la lista suman {sum(milista)}')
    elif opc=='comprobar':
        dato=int(input('¿que numero desea comprobar? '))
        valor= dato in milista
        print(valor)
    elif opc=='extender':
        otralista= [1,2,3,4,5,6]
        milista.extend(otralista)
        print(milista)
    elif opc=='ascender':
        milista.sort()
        print(milista)
    elif opc=='desender':
        milista.reverse()
        print(milista)


         
        


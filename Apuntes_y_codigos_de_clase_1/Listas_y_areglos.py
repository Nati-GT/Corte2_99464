#las listas emiezan desde 0 y un arreglo desde 1
cadena= "Hola mundo"
print(cadena[6]) 
print(len(cadena))
texto=""
for i in cadena:
    print(i) #imprime en vertical

for i in cadena:
    texto+=str(f'{i},') #imprime de manera piramidal la cadena de caracteres
    print(texto)

#Ahora con while
contador=0
texto2=''
while contador<len(cadena):
    texto2+=str(f'{cadena[contador]},') 
    contador+=1
    print(texto2)
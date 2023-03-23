import random as r
numero1=r.randint(10,20)
print(numero1)

#Para que imprima mas de un valor se usa un for 
import random as r
for i in range(5): #el numero que usemos en el rango es el numero de valores que obtendremos 
    numero2=r.randint(10,20)
    print(numero2)
#para numeros flotantes (decimales) utilizamos la funcion "uniform"
import random as r
numero=r.uniform(10,20)
print(numero)
#para imprimir caracteres aleateorios (letras y numeros)
import random as r
caracter=r.choice("natalia")#se pone en el range en el parentesis los terminos que queremos tenerpara sacar en aleatorio
print(caracter) 
#tambien se puede usar con numeros
import random as r
caractern=r.choice("1234")
print(caractern)
#

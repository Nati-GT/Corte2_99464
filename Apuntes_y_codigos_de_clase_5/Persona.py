#PEP.org

class Persona:
    def __init__(self):   #self es el objeto
        self.nombre=None
        self.apellido=None
        self.edad=None
        self.frase=None

    def hablar(self): #metodo
        return self.frase

def main():
    estudiante= Persona()
    estudiante.nombre= 'Natalia'
    estudiante.apellido= 'Garcia'
    estudiante.edad= 20
    estudiante.frase= 'oh debo estudiar'

    futbolista= Persona()
    futbolista.nombre= 'Radamel'
    futbolista.apellido= 'Falcao'
    futbolista.edad= 36 
    futbolista.frase= 'Goooolll'  

    # print(id(estudiante), estudiante.nombre)
    # print(id(futbolista), futbolista.nombre)
    #futbolista = estudiante #cuando igualamos los objetos lo que hacemos es volver anonimo su id

    print(f'El estudiante dice: {estudiante.hablar()}')  #uso del metodo
    print(f'El futbolista dice: {futbolista.hablar()}')

if __name__=="__main__":
    main()


#variables: uso en minuscula,es opcional usar <_>.
    #Ej: variable1
#Clases: la primera letra de cada palabra en mayusculas o en 
# casi de ser mas de una palabra se denota con la convencion CameClass
    #Ej: ClasePrincipal

class Personas:
    def __init__(self):   #self es el objeto
        self.nombre=None   #atributos
        self.altura=None
        self.peso=None

    def Indice(self): #metodo
        IMC=self.peso/((self.altura/100)**2)
        if IMC <=18.5:
            return str('Por debajo')
        elif IMC <=24.9:
            return str('Saludable')
        elif IMC <=29.9:
            return str('Sobrepeso')
        elif IMC <=34.9:
            return str('Obesidad I')
        elif IMC <=39.9:
            return str('Obesidad II')
        else:
            return str('Obesidad III')
        


def main(): #instancia
    estudiante1 = Personas()
    estudiante1.nombre= 'Pedro Caseres'
    estudiante1.altura= 188
    estudiante1.peso= 97

    estudiante2 = Personas()
    estudiante2.nombre= 'Maria Perez'
    estudiante2.altura= 160
    estudiante2.peso= 47

    estudiante3 = Personas()
    estudiante3.nombre= 'Julian Dominguez'
    estudiante3.altura= 158
    estudiante3.peso= 58

    estudiante4 = Personas()
    estudiante4.nombre= 'Jessica Fuentes'
    estudiante4.altura= 170
    estudiante4.peso= 73

    estudiante5 = Personas()
    estudiante5.nombre= 'Natalia Garcia'
    estudiante5.altura= 160
    estudiante5.peso= 70

    print(f'Estudiante: {estudiante1.nombre} resultado: {estudiante1.Indice()}')
    print(f'Estudiante: {estudiante2.nombre} resultado: {estudiante2.Indice()}')
    print(f'Estudiante: {estudiante3.nombre} resultado: {estudiante3.Indice()}')
    print(f'Estudiante: {estudiante4.nombre} resultado: {estudiante4.Indice()}')
    print(f'Estudiante: {estudiante5.nombre} resultado: {estudiante5.Indice()}')

if __name__=="__main__":
    main()
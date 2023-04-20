#--------------Clase Padre--------------
class Ciudadano:
    def __init__(self,nombre:str, apellido:str, genero: str,documento:int,edad:int):
        self.__nombre= nombre
        self.__apellido= apellido
        self.__genero= genero
        self.__documento= documento
        self.__edad= edad
    #-----------Getters--------------
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getGenero(self):
        return self.__genero
    def getDocumento(self):
        return self.__documento
    def getEdad(self):
        return self.__edad
    #-----------Setters----------
    def setNombre(self,nombre:str):
        self.__nombre=nombre
    def setApellido(self,apellido:str):
        self.__apellido=apellido 
    def setGenero(self,genero:str):
        self.__genero=genero
    def setDocumento(self,documento:int):
        self.__documento=documento
    def setEdad(self,edad:int):
        self.__edad=edad
    #----------Sobrecarga Metodo--------------
    def reconocimientos(self):
        return 'No ha recibido ningun reconocimiento'
    
#-------------Clase Hijo Actor------------------
class Actor(Ciudadano):
    def __init__(self, nombre: str, apellido: str, genero: str, documento: int, edad: int,\
        añosDeProfesion:int, obrasInterpretadas:int, papelesActuados:int ):
            super().__init__(nombre, apellido, genero, documento, edad)
            self.__añosDeProfesion=añosDeProfesion
            self.__obrasInterpretadas=obrasInterpretadas
            self.__papelesActuados=papelesActuados
    #-----------Getters hijo----------
    def getAñosDeProfesion(self):
        return self.__añosDeProfesion
    def getObrasInterpretadas(self):
        return self.__obrasInterpretadas
    def getPapelesActuados(self):
        return self.__papelesActuados
    #-----------Setter hijo--------
    def setAñosDeProfesion(self,añosDeProfesion:int):
        self.__añosDeProfesion=añosDeProfesion 
    def setObrasInterpretadas(self,obrasInterpretadas:int):
        self.__obrasInterpretadas=obrasInterpretadas
    def setPapelesActuados(self,papelesActuados:int):
        self.__papelesActuados=papelesActuados
    #----------Sobrecarga Metodo--------------
    def reconocimientos(self):
        return 'Ha sido convocado a obras importantes y ganado 3 premios'
    
#-------------Clase Hijo Escritor-----------------
class Escritor(Ciudadano):
    def __init__(self, nombre: str, apellido: str, genero: str, documento: int, edad: int,\
        añosDeEscritura:int, librosPublicados:int, generoDeEscritura:str, ):
            super().__init__(nombre, apellido, genero, documento, edad)
            self.__añosDeEscritura=añosDeEscritura
            self.__librosPublicados=librosPublicados
            self.__generoDeEscritura=generoDeEscritura
    #-----------Getters hijo----------
    def getAñosDeEscritura(self):
        return self.__añosDeEscritura
    def getLibrosPublicados(self):
        return self.__librosPublicados
    def getGeneroDeEscritura(self):
        return self.__generoDeEscritura
    #-----------Setter hijo--------
    def setAñosDeEscritura(self,añosDeEscritura:int):
        self.__añosDeEscritura=añosDeEscritura 
    def setLibrosPublicados(self,librosPublicados:int):
        self.__librosPublicados=librosPublicados
    def setGeneroDeEscritura(self,generoDeEscritura:str):
        self.__generoDeEscritura=generoDeEscritura
    #----------Sobrecarga Metodo--------------
    def reconocimientos(self):
        return 'Ha sido invitado a multiples eventos y a obtenido 5 premios'
    
#-------------Clase Hijo Cantante-----------------
class Cantante(Ciudadano):
    def __init__(self, nombre: str, apellido: str, genero: str, documento: int, edad: int,\
        añosDeCarrera: int, cancionesCompuestas: int, generoMusical: str):
         super().__init__(nombre, apellido, genero, documento, edad)
         self.__añosDeCarrera=añosDeCarrera
         self.__cancionesCompuestas=cancionesCompuestas
         self.__generoMusical=generoMusical
    #-----------Getters Hijo----------
    def getAñosDeCarrera(self):
        return self.__añosDeCarrera
    def getCancionesCompuestas(self):
        return self.__cancionesCompuestas
    def getGeneroMusical(self):
        return self.__generoMusical
    #-----------Setter hijo-----------
    def setAñosDeCarrera(self, añosDeCarrera: int):
        self.__añosDeCarrera=añosDeCarrera
    def setCancionesCompuestas(self, cancionesCompuestas: int):
        self.__cancionesCompuestas=cancionesCompuestas
    def setGeneroMusical(self, generoMusical: str):
        self.__generoMusical=generoMusical
    def reconocimientos(self):
        return 'Es conocida a nivel mundial y ha obtenido 4 premios'

def main():
        Ciudadano1 = Ciudadano('Javier Roberto','Orozco Lopez','Masculino',258963,36)
        print(f'Nombre: {Ciudadano1.getNombre()}\n'\
              f'Apellido: {Ciudadano1.getApellido()}\n'\
              f'Genero: {Ciudadano1.getGenero()}\n'\
              f'Documento:{Ciudadano1.getDocumento()}\n'\
              f'Edad:{Ciudadano1.getEdad()}\n'+\
              f'reconocimientos: {Ciudadano1.reconocimientos()}')
        
        Ciudadano2= Actor('Luz Angela','Sotelo Monterrosa','Femenino',78963314,26,5,15,20)
        print(f'Nombre: {Ciudadano2.getNombre()}\n'\
              f'Apellido: {Ciudadano2.getApellido()}\n'\
              f'Genero: {Ciudadano2.getGenero()}\n'\
              f'Documento:{Ciudadano2.getDocumento()}\n'\
              f'Edad:{Ciudadano2.getEdad()}\n'\
              f'Años De Profesion:{Ciudadano2.getAñosDeProfesion()}\n'\
              f'Obras Interpretadas:{Ciudadano2.getObrasInterpretadas()}\n'\
              f'Papeles Actuados:{Ciudadano2.getPapelesActuados()}\n'\
              f'reconocimientos: {Ciudadano2.reconocimientos()}')
        
        Ciudadano3= Escritor('Christopher Alexander','Miller Contreras','Masculino',1596321,35,10,8,'Misterio y Suspenso')
        print(f'Nombre: {Ciudadano3.getNombre()}\n'\
              f'Apellido: {Ciudadano3.getApellido()}\n'\
              f'Genero: {Ciudadano3.getGenero()}\n'\
              f'Documento:{Ciudadano3.getDocumento()}\n'\
              f'Edad:{Ciudadano3.getEdad()}\n'\
              f'Años De Escritura:{Ciudadano3.getAñosDeEscritura()}\n'\
              f'Libros Publicados:{Ciudadano3.getLibrosPublicados()}\n'\
              f'Genero De Escritura:{Ciudadano3.getGeneroDeEscritura()}\n'\
              f'reconocimientos: {Ciudadano3.reconocimientos()}')
        
        Ciudadano4= Cantante('Luna Sofia','Thompsom Guess','Femenino',75369842,22,6,30,'Pop')
        print(f'Nombre: {Ciudadano4.getNombre()}\n'\
              f'Apellido: {Ciudadano4.getApellido()}\n'\
              f'Genero: {Ciudadano4.getGenero()}\n'\
              f'Documento:{Ciudadano4.getDocumento()}\n'\
              f'Edad:{Ciudadano4.getEdad()}\n'\
              f'Años De Carrera:{Ciudadano4.getAñosDeCarrera()}\n'\
              f'Canciones Compuestas:{Ciudadano4.getCancionesCompuestas()}\n'\
              f'Genero Musical:{Ciudadano4.getGeneroMusical()}\n'\
              f'reconocimientos: {Ciudadano4.reconocimientos()}')

if __name__=="__main__":
        main()
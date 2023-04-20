#--------------Clase Padre--------------
class Deportista:
    def __init__(self,nombre:str,documento:int,edad:int):
        self.__nombre= nombre
        self.__documento= documento
        self.__edad= edad
    #-----------Getters--------------
    def getNombre(self):
        return self.__nombre
    def getDocumento(self):
        return self.__documento
    def getEdad(self):
        return self.__edad
    #-----------Setters----------
    def setNombre(self,nombre:str):
        self.__nombre=nombre
    def setDocumento(self,documento:int):
        self.__documento=documento
    def setEdad(self,edad:int):
        self.__edad=edad
    #----------Sobrecarga Metodo--------------
    def palmares(self):
        return 'Ha ganado una Medalla'
#-------------Clase Hijo Futbol------------------
class DeportistaFutbol(Deportista):
    def __init__(self, nombre: str, documento: int, edad: int,golesAnotados:int, nombreEquipo:str):
            super().__init__(nombre, documento, edad)
            self.__golesAnotados=golesAnotados
            self.__nombreEquipo=nombreEquipo
    #-----------Getters hijo----------
    def getGolesAnotados(self):
        return self.__golesAnotados
    def getNombreEquipo(self):
        return self.__nombreEquipo
    #-----------Setter hijo--------
    def setGolesAnotados(self,golesAnotados:int):
        self.__golesAnotados=golesAnotados 
    def setNombreEquipo(self,nombreEquipo:str):
        self.__nombreEquipo=nombreEquipo
    #----------Sobrecarga Metodo--------------
    def palmares(self):
        return 'Ganado una la copa europa'
#-------------Clase Hijo Basket-----------------
#Crea clase de basket y tennis 
        


def main():
        Futbolista = DeportistaFutbol('Falcao',258963,36,10, 'seleccion Colombia')
        print(f'Deportista: {Futbolista.getNombre()}\n'\
              f'Documento:{Futbolista.getDocumento()}\n'\
              f'Edad:{Futbolista.getEdad()}\n'\
              f'Cantidad de goles:{Futbolista.getGolesAnotados()}\n'\
              f'Equipo:{Futbolista.getNombreEquipo()}'+\
                f'Palmares: {Futbolista.palmares()}')
        
        Futbolista2= Deportista('Mario Yepes',78963314,48)
        print(f'Deportista: {Futbolista2.getNombre()}\n'\
              f'Documento:{Futbolista2.getDocumento()}\n'\
              f'Edad:{Futbolista2.getEdad()}\n'\
                f'Palmares: {Futbolista2.palmares()}')
        pass

if __name__=="__main__":
        main()
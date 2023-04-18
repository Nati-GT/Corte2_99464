class Ciudadano():
    def __init__(self):
        self.__nombre=None
        self.__idioma=None

    #-------Getters------
    def getNombre(self):
        return self.__nombre
    def getIdioma(self):
        return self.__idioma
    #-------Setters-------
    def setNombre(self, nombre:str):
        return self.__nombre
    def setIdioma(self,idioma:str):
        return self.__idioma
    #-------Sobrecarga------
    def saludo(self):
        return "Quoi de beau!"

class Colombia(Ciudadano):
        def __init__(self):
            super().__init__()
            self.__cc=None
        
        def getCC(self):
            return self.__cc

        def setCC(self,cc:int):
            self.__cc=cc

        def saludo(self):
            return "Qiubo parce"

class Inglaterra(Ciudadano):
        def __init__(self):
            super().__init__()
            self.__id=None
        
        def getID(self):
            return self.__id

        def setID(self,id):
            self.__id=id

        def saludo(self):
            return "Hi brother"
        
class Chino(Ciudadano):
        def __init__(self):
            super().__init__()
            self.__Shengfenzheng=None
        
        def getShengfenzheng(self):
            return self.__Shengfenzheng

        def setShengfenzheng(self,Shengfenzheng:int ):
            self.__Shengfenzheng=Shengfenzheng

        def saludo(self):
            return "Ni Gan Ma Ya"
        
#-----Poliformismo------
def darSaludo(obj):
    return obj.saludo()


def main():
    colombiano=Colombia()
    colombiano.setNombre("Kevin")
    colombiano.setIdioma("Español")
    colombiano.setCC(123654789)

    ingles=Inglaterra()
    ingles.setNombre("Richard")
    ingles.setIdioma("English")
    ingles.setID(8567469)

    chino=Chino()
    chino.setNombre("Jim Lee")
    chino.setIdioma("Mandarin")
    chino.setShengfenzheng(123654789)

    #--------Aplicantes--------
    print(f'Aplicante: {colombiano.getNombre()}\n'+\
        f'Idioma: {colombiano.getIdioma()}\n'+\
        f'CC: {colombiano.getCC()}\n'+
        darSaludo(colombiano)+'\n')

    print(f'Aplicante: {ingles.getNombre()}\n'+\
        f'Idioma: {ingles.getIdioma()}\n'+\
        f'Id: {ingles.getID()}\n'+
        darSaludo(ingles)+'\n')

    print(f'Aplicante: {chino.getNombre()}\n'+\
        f'Idioma: {chino.getIdioma()}\n'+\
        f'Shengfenzheng: {chino.getShengfenzheng()}\n'+
        darSaludo(chino)+'\n')
    pass


if __name__=="__main__":
    main()
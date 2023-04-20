from PySide6.QtWidgets import * #QApplication,QMainWindow,QComboBox 
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        desplegable=QComboBox()
        self.setCentralWidget(desplegable)

        desplegable.addItems(["","opcion 1","opcion 2","opcion 3"])

        desplegable.currentIndexChanged.connect(self.indice_cambiado)
        desplegable.currentTextChanged.connect(self.texto_camiado)

        print("Indice actual ->", desplegable.currentIndex())
        print("Texto actual ->", desplegable.currentText())

    def indice_cambiado(self, indice):
        print("Nuevo indice ->", indice)
    
    def texto_camiado(self,texto):
        print("Nuevo texto ->",texto)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    window= MainWindow()
    window.show()
    sys.exit(app.exec_())


#app= QApplication(sys.argv)

#window=QMainWindow()

#window.setWindowTitle("Hola mundo")

#button=QPushButton("soy un boton")

#window.setCentralWidget(button)

#window.show()

#sys.exit(app.exec_())
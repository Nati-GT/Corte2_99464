from PySide6.QtWidgets import *
import sys

app= QApplication(sys.argv)

window=QMainWindow()

window.setWindowTitle("Hola mundo")

button=QPushButton("soy un boton")

window.setCentralWidget(button)

window.show()

sys.exit(app.exec_())
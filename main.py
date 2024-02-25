from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from automata import Parser

class MiVentana(QMainWindow):
    def __init__(self):
        super(MiVentana, self).__init__()
        loadUi('vista.ui', self)
        self.parser = None
        self.pushButton.clicked.connect(self.verificar)

    def verificar(self):
        texto = self.textEdit.toPlainText()
        self.parser = Parser(texto)
        self.mostrar_recorrido(self.parser.parse())

    def mostrar_recorrido(self, exito):
        recorrido = self.parser.recorrido
        if exito:
            self.textBrowser.clear()
            self.textBrowser.append("Resultado de la pila:")
            for i, paso in enumerate(recorrido):
                self.textBrowser.append(f"Paso {i + 1}: {' '.join(paso)}")
                
            self.textBrowser.append("Pila vacia: $")
            self.textBrowser.append("La cadena es valida según la gramática")

        else:
            self.textBrowser.clear()
            for i, paso in enumerate(recorrido):
                self.textBrowser.append(f"Paso {i + 1}: {' '.join(paso)}")
            self.textBrowser.append("\nLa cadena no es valida según la gramática")

if __name__ == '__main__':
    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    app.exec_()
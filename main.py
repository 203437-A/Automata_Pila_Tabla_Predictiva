from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from automata import Parser

class MiVentana(QMainWindow):
    def __init__(self):
        super(MiVentana, self).__init__()
        loadUi('vista.ui', self)
        self.pushButton.clicked.connect(self.verificar)

    def verificar(self):
        texto = self.textEdit.toPlainText()
        parser = Parser(texto)
        resultado = parser.parse()
        recorrido_pila = parser.recorrido

        self.textBrowser.clear()
        self.textBrowser.append("Recorrido de la Pila:")
        self.textBrowser.append("Pila inicial: ['$', 'S']")
        
        for paso in range(len(recorrido_pila) - 1):
            estado_anterior = recorrido_pila[paso]
            estado_actual = recorrido_pila[paso + 1]

            cambio = [simbolo for simbolo in estado_actual if simbolo not in estado_anterior]
            proceso = ' '.join(cambio)

            pila_mantener = [simbolo for simbolo in estado_actual if simbolo in estado_anterior]
            pila_final = pila_mantener + cambio
            if cambio:
                self.textBrowser.append(f"Pila después de procesar '{proceso}': {pila_final}")
        
        if resultado:
            self.textBrowser.append("Pila final: ['$']")
            self.textBrowser.append('\nLa cadena es válida según la gramática.')
        else:
            self.textBrowser.append('\nLa cadena no es válida según la gramática.')

if __name__ == '__main__':
    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    app.exec_()

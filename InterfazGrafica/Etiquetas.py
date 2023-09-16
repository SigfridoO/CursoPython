from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import sys
from pathlib import Path

def absPath(archivo):
    return str(Path(__file__).parent.absolute() / archivo)

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)

        print (absPath('atardecer.jpg'))

        imagen = QPixmap(absPath('atardecer.jpg'))

        # creando una etiqueta
        etiqueta = QLabel('Soy una etiqueta')
        etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        etiqueta.setPixmap(imagen)


        self.setCentralWidget(etiqueta)

if __name__ == '__main__':
    app =QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
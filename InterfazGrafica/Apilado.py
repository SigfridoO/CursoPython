from PySide6.QtWidgets import QApplication, QMainWindow, \
    QStackedWidget, QWidget
from PySide6.QtCore import Qt
import sys
from Caja import Caja

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 400)

        layout = QStackedWidget()
        layout.addWidget(Caja('orange'))
        layout.addWidget(Caja('green'))
        layout.addWidget(Caja('blue'))
        layout.addWidget(Caja('pink'))

        self.layout = layout
        self.setCentralWidget(layout)




    def keyPressEvent(self, event) -> None:
        print('Tecla presionada', event.key())

        indice = self.layout.currentIndex()
        indiceMaximo = self.layout.count()-1

        if event.key() == Qt.Key_Right:
            print('Se presiono la tecla derecha')
            indice += 1

        if event.key() == Qt.Key_Left:
            print('Se presiono la tecla izquierda')
            indice -= 1

        if indice > indiceMaximo:
            indice = 0
        if indice < 0:
            indice = indiceMaximo

        self.layout.setCurrentIndex(indice)
        # event.accept()
#https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

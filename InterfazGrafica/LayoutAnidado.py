from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, \
    QVBoxLayout, QHBoxLayout, QWidget
import sys

class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f'background-color: {color}')

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)

        layoutVertical1 = QVBoxLayout()

        miCaja1 = Caja("green")
        miCaja2 = Caja("blue")

        layoutVertical1.addWidget(miCaja1)
        layoutVertical1.addWidget(miCaja2)



        layoutAux = QHBoxLayout()
        miCaja3 = Caja("yellow")
        layoutAux.addWidget(miCaja3)


        layoutHorizontal1 = QHBoxLayout()
        layoutHorizontal1.addLayout(layoutVertical1)
        layoutHorizontal1.addLayout(layoutAux)


        # layout.setContentsMargins(0,0,0,0)
        # layout.setSpacing(0)

        widget = QWidget()
        widget.setLayout(layoutHorizontal1)

        self.setCentralWidget(widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
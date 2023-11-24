from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, \
    QGridLayout, QWidget
import sys

class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f'background-color: {color}')

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)

        layout = QGridLayout()
        miCaja = Caja('green')
        # miCaja.setFixedWidth(50)
        miCaja.setFixedSize(50,80)
        layout.addWidget(miCaja,0, 0)
        layout.addWidget(Caja('cyan'),1, 2)
        layout.addWidget(Caja('red'),2, 1, 2, 2)
        layout.addWidget(Caja('orange'),1, 0, 3, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
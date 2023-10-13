from PySide6.QtWidgets import QApplication, QMainWindow, QDockWidget, QLabel
from PySide6.QtCore import Qt
import sys

class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f'background-color: {color}')


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)

        dock1 = QDockWidget()
        dock1.setWindowTitle('DOCK')
        dock1.setWidget(Caja('blue'))
        dock1.setFeatures(QDockWidget.NoDockWidgetFeatures |QDockWidget.DockWidgetMovable)

        self.addDockWidget(Qt.LeftDockWidgetArea, dock1)

        self.setCentralWidget(Caja('green'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

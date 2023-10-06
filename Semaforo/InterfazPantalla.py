import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout

from Caja import Caja

from PyQt5.QtCore import QThread, QObject, QRunnable, QThreadPool, \
    pyqtSignal as Signal, pyqtSlot as Slot


class WorkerSignals(QObject):
    luzRoja = Signal(bool)
    luzAmarilla = Signal(bool)
    luzVerde = Signal(bool)

    entrada = Signal(bool)


class Worker(QRunnable):

    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()

    def activarLuzRoja(self, estado: bool = False):
        try:
            self.signals.luzRoja.emit(estado)
        except Exception as error:
            print(error)

    def activarLuzAmarilla(self, estado: bool = False):
        try:
            self.signals.luzAmarilla.emit(estado)
        except Exception as error:
            print(error)

    def activarLuzVerde(self, estado: bool = False):
        try:
            self.signals.luzVerde.emit(estado)
        except Exception as error:
            print(error)

    def leerEntrada(self, estado: bool = False):
        try:
            self.signals.entrada.emit(estado)
        except Exception as error:
            print(error)

class InterfazPantalla(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.resize(420, 420)

        layout = QGridLayout()
        self.cajaAzul = Caja('cyan')
        # self.cajaAzul.setFixedWidth(50)
        # self.cajaAzul.setFixedSize(50,80)

        self.cajaLuzRoja = Caja('red')
        self.cajaLuzAmarilla = Caja('yellow')
        self.cajaLuzVerde = Caja('green')

        layout.addWidget(self.cajaAzul, 0, 0, 3, 2)
        layout.addWidget(self.cajaLuzRoja, 0, 2)
        layout.addWidget(self.cajaLuzAmarilla, 1, 2)
        layout.addWidget(self.cajaLuzVerde, 2, 2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.threadpool = QThreadPool()

        self.worker = Worker()
        self.worker.signals.luzRoja.connect(self.activarLuzRoja)
        self.worker.signals.luzAmarilla.connect(self.activarLuzAmarilla)
        self.worker.signals.luzVerde.connect(self.activarLuzVerde)
        self.worker.signals.entrada.connect(self.leerEntrada)

        # Iniciamos el trabajador en la pool de hilos
        self.threadpool.start(self.worker)

    def activarLuzRoja(self, opcion: bool = False) -> None:
        self.cajaLuzRoja.setHidden(not opcion)

    def activarLuzAmarilla(self, opcion: bool = False) -> None:
        self.cajaLuzAmarilla.setHidden(not opcion)

    def activarLuzVerde(self, opcion: bool = False) -> None:
        self.cajaLuzVerde.setHidden(not opcion)

    def activarCajaAzul(self, opcion: bool = False) -> None:
        self.cajaAzul.setHidden(not opcion)

    def obtenerWorker(self):
        return self.worker


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InterfazPantalla()
    window.show()
    sys.exit(app.exec())

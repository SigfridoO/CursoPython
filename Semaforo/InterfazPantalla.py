__author__ = "Sigfrido Soria"
__date__ = "14-mar-2023 21:10:00"

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel

from Caja import Caja

from PyQt5.QtCore import QThread, QObject, QRunnable, QThreadPool, \
    pyqtSignal as Signal, pyqtSlot as Slot


class WorkerSignals(QObject):
    luzRoja = Signal(bool)
    luzAmarilla = Signal(bool)
    luzVerde = Signal(bool)

    variableDigital = Signal(bool)
    variableAnalogica = Signal(str)


class Worker(QRunnable):

    def __init__(self):
        super().__init__()
        self.signals: WorkerSignals = WorkerSignals()

    def senal_luz_roja(self, estado: bool = False):
        try:
            self.signals.luzRoja.emit(estado)
        except Exception as error:
            print(error)

    def senal_luz_amarilla(self, estado: bool = False):
        try:
            self.signals.luzAmarilla.emit(estado)
        except Exception as error:
            print(error)

    def senal_luz_verde(self, estado: bool = False):
        try:
            self.signals.luzVerde.emit(estado)
        except Exception as error:
            print(error)

    def actualizar_variable_digital(self, estado: bool = False):
        try:
            self.signals.variableDigital.emit(estado)
        except Exception as error:
            print(error)

    def actualizar_variable_analogica(self, valor: str = ''):
        try:
            self.signals.variableAnalogica.emit(valor)
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

        self.etiquetaPrueba = QLabel('')
        self.etiquetaPrueba.setFixedWidth(150)

        layout.addWidget(self.cajaAzul, 0, 0, 2, 2)
        layout.addWidget(self.etiquetaPrueba, 2, 0, 1, 1)

        layout.addWidget(self.cajaLuzRoja, 0, 2)
        layout.addWidget(self.cajaLuzAmarilla, 1, 2)
        layout.addWidget(self.cajaLuzVerde, 2, 2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.threadpool = QThreadPool()

        self.worker = Worker()
        self.worker.signals.luzRoja.connect(self.actualizar_luz_roja)
        self.worker.signals.luzAmarilla.connect(self.actualizar_luz_amarilla)
        self.worker.signals.luzVerde.connect(self.actualizar_luz_verde)
        self.worker.signals.variableDigital.connect(self.actualizar_variable_digital)
        self.worker.signals.variableAnalogica.connect(self.actualizar_variable_analogica)

        # Iniciamos el trabajador en la pool de hilos
        self.threadpool.start(self.worker)

    def actualizar_luz_roja(self, opcion: bool = False) -> None:
        self.cajaLuzRoja.setHidden(not opcion)

    def actualizar_luz_amarilla(self, opcion: bool = False) -> None:
        self.cajaLuzAmarilla.setHidden(not opcion)

    def actualizar_luz_verde(self, opcion: bool = False) -> None:
        self.cajaLuzVerde.setHidden(not opcion)

    def actualizar_variable_digital(self, opcion: bool = False) -> None:
        self.cajaAzul.setHidden(not opcion)

    def actualizar_variable_analogica(self, valor: str = ''):
        self.etiquetaPrueba.setText(valor)

    def obtener_worker(self):
        return self.worker


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InterfazPantalla()
    window.show()
    sys.exit(app.exec())

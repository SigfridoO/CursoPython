import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

# from PyQt5.QtCore import (QThread, QObject, QRunnable, QThreadPool
#                           pyqtSignal as Signal), pyqtSlot as Slot

# class WorkerSignals(QObject):
#     llamadaEntrante = Signal(bool)
#
# class Worker(QRunnable):
#
#     def __init__(self):
#         super().__init__()
#         self.signals = WorkerSignals()
#
#         self.banderaMostrarLlamadaEntrante: bool = False
#
#         # Para el control del programa
#         self.TON_00: Temporizador = Temporizador("TON_00", 1, "Control del programa")
#         self.TON_01: Temporizador = Temporizador("TON_01", 0.2)
#
#
#         self.M: list = []
#         for i in range(80):
#             self.M.append(0)
#
#         self.RC: list = []
#         for i in range(80):
#             self.RC.append(0)
#
#
#     @Slot()
#     def run(self):
#         self.banderaControlDelPrograma = True
#         contador = 0
#
#         while self.banderaControlDelPrograma:
#             self.TON_00.entrada = not self.TON_00.salida
#             self.TON_00.actualizar()
#
#             if self.TON_00.salida:
#                 # print('Funcionando' , contador)
#                 contador += 1
#
#             self.TON_01.entrada = not self.TON_01.salida
#             self.TON_01.actualizar()
#
#             if self.TON_01.salida:
#
#                 try:
#                     self.signals.llamadaEntrante.emit(parpadeo)
#                 except Exception as error:
#                     print(error)
#
#     def mostrarLlamadaEntrante(self, opcion: bool = False) -> None:
#         self.banderaMostrarLlamadaEntrante = opcion
#


class InterfazPantalla(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.resize(240, 120)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InterfazPantalla()
    window.show()
    sys.exit(app.exec())

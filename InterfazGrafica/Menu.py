from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui  import QIcon, QAction

import sys
from pathlib import Path
def absPath(archivo):
    return str(Path(__file__).parent.absolute() / archivo)

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 300)
        icono = QIcon(absPath('arbol.ico'))
        self.setWindowIcon(icono)
        self.setWindowTitle("MI PROGRAMA")

        self.construir_menu()

    def construir_menu(self):
        menu = self.menuBar()
        menuArchivo = menu.addMenu("&Archivo")
        menuArchivo.addAction("&Guardar")
        menuArchivo.addSeparator()

        menuArchivo.addAction( QIcon(absPath('arbol.ico')),"&Salir", self.cerrar, 'Ctrl+Q' )
        
        actionCopiar = QAction("copiar", self)
        menuEditar = menu.addMenu("&Editar")
        menuEditar.addAction(actionCopiar)

        menuAyuda = menu.addMenu("A&yuda")

    def cerrar(self):
        print('cerrando la aplicacion')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

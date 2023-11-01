from PySide6.QtWidgets import QApplication, QMainWindow, \
    QWidget, QLabel, QPushButton, QLineEdit, QFormLayout, QDial, QDateEdit, QDateTimeEdit, QSpinBox, \
    QDoubleSpinBox, QComboBox, QFontComboBox, QProgressBar, QLCDNumber, QSlider, QCheckBox, QRadioButton
from PySide6.QtCore import Qt
import sys
from qt_material import apply_stylesheet

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QFormLayout()
        layout.addRow("QLabel", QLabel("QLabel"))
        layout.addRow("QPushButton", QPushButton("QPushButton"))
        layout.addRow("QCheckBox", QCheckBox())
        layout.addRow("QRadioButton", QRadioButton())

        layout.addRow("QLineEdit", QLineEdit("QLineEdit"))
        layout.addRow("QDateEdit", QDateEdit())
        layout.addRow("QDateTimeEdit", QDateTimeEdit())
        layout.addRow("QSpinBox", QSpinBox())
        layout.addRow("QDoubleSpinBox", QDoubleSpinBox())
        layout.addRow("QComboBox", QComboBox())
        layout.addRow("QFontComboBox", QFontComboBox())
        layout.addRow("QProgressBar", QProgressBar())
        layout.addRow("QLCDNumber", QLCDNumber())
        layout.addRow("QSlider", QSlider(Qt.Horizontal))
        layout.addRow("QDial", QDial())

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_amber.xml')
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

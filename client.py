import sys

from PyQt6.QtWidgets import QApplication

from controller import Controller

if __name__ == '__main__':
    qt = QApplication([])
    c = Controller()
    sys.exit(qt.exec())

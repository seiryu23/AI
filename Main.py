import sys
from PyQt5 import QtWidgets
import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(
        sys.argv
    )
    win = MainWindow.MainWindow()
    win.show()
    ret = app.exec_()
    sys.exit(ret)
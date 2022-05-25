##メイン処理##
import sys
from PyQt5 import QtWidgets
import MainWindow

##処理##
if __name__ == "__main__":
    app = QtWidgets.QApplication(
        sys.argv
    )
    
    win = MainWindow.MainWindow()
    #画面起動
    win.show()
    ret = app.exec_()
    sys.exit(ret)
##画面起動後の処理##
from PyQt5 import QtWidgets
import CCsMsc
import datetime
import qt_mscDialogUI

##クラス##
#起動した画面の操作に応じて各操作に紐づく関数を呼び出す
class MainWindow(QtWidgets.QMainWindow):
    ##関数##
    #-----------------------------------------------------
    # 画面起動時
    #-----------------------------------------------------
    def __init__(self):
        super().__init__()
        #システム名をセット
        self.msc_operator = CCsMsc.CCsMsc('msc_operator')
        self.action = True
        self.ui = qt_mscDialogUI.Ui_MainWindow()
        self.log = []
        #画面起動
        self.ui.setupUi(self)

    #-----------------------------------------------------
    # メッセージ送信時にリストに送信したメッセージを表示する
    #-----------------------------------------------------
    # str  : 送信した文字列
    #-----------------------------------------------------
    # 戻値 ：なし
    #-----------------------------------------------------
    def putlog(self, str):
        self.ui.listWidget.addItem(str)
        self.log.append(str + '\n')
    
    #-----------------------------------------------------
    # 送信者名を表示
    #-----------------------------------------------------
    # 戻値 ：文字列
    #-----------------------------------------------------
    def prompt(self):
        p = self.msc_operator.get_name()
        if self.action == True:
            p += '：' + self.msc_operator.get_responder_name()
        return p + '> '
    
    #-----------------------------------------------------
    # ログ出力
    #-----------------------------------------------------
    # 戻値 ：なし
    #-----------------------------------------------------
    def writeLog(self):
        now = 'System Dialogue Log: '\
            + datetime.datetime.now().strftime('%Y-%m-%d %H:%M::%S')\
            + '\n'
        self.log.insert(0, now)
        with open('LOG/log.txt', 'a', encoding = 'utf_8') as f:
            f.writelines(self.log)

    #-----------------------------------------------------
    # システム応答処理
    #-----------------------------------------------------
    # 戻値 ：なし
    #-----------------------------------------------------
    def buttonTalkSlot(self):
        value = self.ui.lineEdit.text()
        #送信した文字列が空の時
        if not value:
            self.ui.labelResponse.setText('いかがしましたか？')
        #送信した文字列が空以外の時
        else:
            #送信内容によって、応答する文字列を取得する
            response = self.msc_operator.dialogue(value)
            #応答内容をラベルに表示
            self.ui.labelResponse.setText(response)
            #トークログに表示
            self.putlog('> ' + value)
            self.putlog(self.prompt() + response)
            #送信欄をクリア
            self.ui.lineEdit.clear()

    #-----------------------------------------------------
    # 画面終了処理
    #-----------------------------------------------------
    # 戻値 ：なし
    #-----------------------------------------------------
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(
            self,
            '確認',
            "プログラムを終了しますか？",
            buttons = QtWidgets.QMessageBox.Yes |
                        QtWidgets.QMessageBox.No
        )
        #画面終了時
        if reply == QtWidgets.QMessageBox.Yes:
            self.msc_operator.save()
            self.writeLog()
            event.accept()
        #画面終了しない時
        else:
            event.ignore()
    
    #-----------------------------------------------------
    # Responder表示ボタンをクリック
    #-----------------------------------------------------
    # 戻値 ：なし
    #-----------------------------------------------------
    def showResponderName(self):
        self.action = True

    #-----------------------------------------------------
    # Responder非表示ボタンをクリック
    #-----------------------------------------------------
    # 戻値 ：なし
    #-----------------------------------------------------
    def hiddenResponderName(self):
        self.action = False

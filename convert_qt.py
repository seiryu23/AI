from PyQt5 import uic

#読み込みモードでQTPyで作成したuiファイルを展開
fin = open('qt_mscDialog.ui', 'r', encoding='utf-8')

#書き込みモードでコンバートファイルを展開
fout = open('qt_mscDialogUI.py', 'w', encoding='utf-8')

#コンバート処理開始
uic.compileUi(fin, fout)

#各展開したファイルを閉じる
fin.close()
fout.close()
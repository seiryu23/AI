from PyQt5 import uic

fin = open('qt_mscDialog.ui', 'r', encoding='utf-8')

fout = open('qt_mscDialogUI.py', 'w', encoding='utf-8')

uic.compileUi(fin, fout)

fin.close()
fout.close()
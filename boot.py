import sys
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QMainWindow, QFileDialog

from ui_main import Ui_MainWindow


# 添加事件信号槽,不要去生成的uixx.py里添加事件，这样做的目的界面与业务分离
class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent = None):
        super(MyMainWindow,self).__init__()
        self.setupUi(self)
        self.btnOpenFile.clicked.connect(self.openFile)
    def openFile(self):
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', '')
        self.lblFileName.setText(openfile_name[0])


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = MyMainWindow()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
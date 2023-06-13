from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from UI.Ui_My_widget import Ui_Form


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        # 导入工具文件
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.init_ui()

    def get_text(self):
        print(self.ui.lineEdit.text())

    def init_ui(self):
        self.ui.pushButton.clicked.connect(self.get_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())

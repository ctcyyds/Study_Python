from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("自定义窗口标题")
        self.resize(640, 480)
        self.init_ui()

    def btn1_clicked(self):
        print("按钮1被点击")

    def btn2_clicked(self):
        print("按钮2被点击")

    def init_ui(self):
        """
        Init UI
        :return:
        """
        # 添加两个按钮，给按钮绑定事件
        layout = QHBoxLayout()
        # 初始化界面内容
        btn1 = QPushButton("按钮1")
        btn2 = QPushButton("按钮2")
        # 添加按钮事件
        btn1.clicked.connect(self.btn1_clicked)
        btn2.clicked.connect(self.btn2_clicked)
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())

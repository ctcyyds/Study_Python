from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtGui import QPixmap
import sys

# 创建PyQt Application
app = QApplication(sys.argv)

# =======================================
# 创建第一个窗口
w = QWidget()

# 设置标题
w.setWindowTitle("Game Start!")
# 设置图标
w.setWindowIcon(QIcon("img/qq.png"))
# 设置窗口大小
w.resize(1800, 900)


# =======================================
# 设置文本(需要用到QLanel)
# label = QLabel()
# label.setText("这是一个标签")
# # 设置图片(需要用到GUI的Qpixmap)
# q_pixmap = QPixmap("img/img.png")
# label.setPixmap(q_pixmap)
# label.setParent(w)
# # 根据图片修改窗口大小
# w.resize(q_pixmap.width(), q_pixmap.height())

# =======================================
# 单行输入文本框
# layout = QVBoxLayout()
# username_edit = QLineEdit()
# username_edit.setText("张三丰")
# username_edit.setPlaceholderText("请输入姓名")
# # 设置输入的文本长度
# username_edit.setMaxLength(5)
# layout.addWidget(username_edit)
#
# pwd_edit = QLineEdit()
# pwd_edit.setPlaceholderText("请输入密码")
# # 设置密码隐藏
# pwd_edit.setEchoMode(QLineEdit.Password)
# layout.addWidget(pwd_edit)
# w.setLayout(layout)

# =======================================
# 多行文本输入框
# layout = QVBoxLayout()
# edit = QTextEdit()
# edit.setPlaceholderText("请输入个人简介")
# edit.setPlainText("默认内容")
# # 获取输入的内容
# edit.toPlainText()
# # 清空内容
# edit.clear()
# layout.addWidget(edit)
# w.setLayout(layout)

# =======================================
# 按钮

def btn_click_func(x):
    """
    按钮事件
    :return:
    """
    print("火箭发射了")


btn = QPushButton(w)
# 设置按钮文本w
btn.setText("发射")
# 给按钮添加事件监听
# btn.clicked.connect(btn_click_func)
# 将按钮添加到窗口中==btn = QPushButton(w)
# btn.setParent(w)
# 按钮信号和槽函数（其中x为函数里面的参数）
# btn.clicked.connect(lambda x: print("按钮按下啦，要起飞了！"))
# 这里要注意quit后面不要加括号
btn.clicked.connect(QApplication.quit)
# =======================================
# 显示窗口
w.show()
# 阻塞主线程的while Ture
app.exit(app.exec())

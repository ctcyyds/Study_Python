from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QTextEdit, QPushButton, QHBoxLayout, \
    QFormLayout, QMessageBox, QInputDialog, QRadioButton, QButtonGroup, QCheckBox
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
# w.resize(1800, 900)

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

# def btn_click_func(x):
#     """
#     按钮事件
#     :return:
#     """
#     print("火箭发射了")
#
#
# btn = QPushButton(w)
# # 设置按钮文本w
# btn.setText("发射")
# # 给按钮添加事件监听
# # btn.clicked.connect(btn_click_func)
# # 将按钮添加到窗口中==btn = QPushButton(w)
# # btn.setParent(w)
# # 按钮信号和槽函数（其中x为函数里面的参数）
# # btn.clicked.connect(lambda x: print("按钮按下啦，要起飞了！"))
# # 这里要注意quit后面不要加括号
# btn.clicked.connect(QApplication.quit)

# 水平布局(QHBoxLayout) 竖直布局（QVBoxLayout）
# layout = QHBoxLayout()
# layout.addWidget(QPushButton("1"))
# layout.addWidget(QPushButton("2"))
# layout.addWidget(QPushButton("3"))
# layout.addWidget(QPushButton("4"))
# layout.addWidget(QPushButton("5"))
# w.setLayout(layout)

# =======================================
# 表单布局
# def on_submit():
#     print("Username:", edit_username.text())
#     print("Password:", edit_password.text())
#     print("Phone:", edit_phone.text())
#
#
# layout = QFormLayout()
# edit_username = QLineEdit()
# edit_password = QLineEdit()
# edit_password.setEchoMode(QLineEdit.Password)
# edit_phone = QLineEdit()
# layout.addRow("username", edit_username)
# layout.addRow("password", edit_password)
# layout.addRow("Tel", edit_phone)
# w.setLayout(layout)
# # 添加一个提交按钮
# btn = QPushButton("提交")
# btn.clicked.connect(on_submit)
# layout.addWidget(btn)

# =======================================
# 嵌套布局
# h_layout = QHBoxLayout()
# v_layout_1 = QVBoxLayout()
# v_layout_1.addWidget(QPushButton("1"))
# h_layout.addLayout(v_layout_1)
#
# v_layout_2 = QVBoxLayout()
# v_layout_2.addWidget(QPushButton("2"))
# v_layout_2.addWidget(QPushButton("3"))
# h_layout.addLayout(v_layout_2)
#
# v_layoout_3 = QVBoxLayout()
# v_layoout_3.addWidget(QPushButton("4"))
# v_layoout_3.addWidget(QPushButton("5"))
# v_layoout_3.addWidget(QPushButton("6"))
# h_layout.addLayout(v_layoout_3)
#
# v_layout_4 = QVBoxLayout()
# v_layout_4.addWidget(QPushButton("7"))
# v_layout_4.addWidget(QPushButton("8"))
# v_layout_4.addWidget(QPushButton("9"))
# v_layout_4.addWidget(QPushButton("0"))
# h_layout.addLayout(v_layout_4)
# w.setLayout(h_layout)

# =======================================
# 消息对话框
# def show_message():
#     # question的图标是问号，information的图标是感叹号
#     result = QMessageBox.question(w, "删除提示", "确认要删除吗？", buttons=QMessageBox.Ok | QMessageBox.Cancel,
#                                   defaultButton=QMessageBox.Cancel)
#     if result == QMessageBox.Ok:
#         print("删除成功")
#     else:
#         print("取消删除")
#
#
# btn = QPushButton("显示对话框")
# btn.clicked.connect(show_message)
# btn.setParent(w)

# =======================================
# 输入对话框
# def add_role():
#     text, confirm = QInputDialog.getText(w, "提示", "请输入角色名称")
#     if confirm:
#         # 更改内容
#         q_label.setText(text)
#
#
# layout = QHBoxLayout()
# q_label = QLabel()
# q_label.setText("匿名")
# layout.addWidget(q_label)
#
# btn = QPushButton("创建角色")
# # 添加按钮事件
# btn.clicked.connect(add_role)
# layout.addWidget(btn)
# w.setLayout(layout)

# =======================================
# 单选框
# def on_group_toggled(btn: QRadioButton):
#     print(btn.text()), btn.isChecked()
#
#
# btn1 = QRadioButton("男")
# btn2 = QRadioButton("女")
# # 默认选中
# btn2.setChecked(True)
# group = QButtonGroup(w)
# group.addButton(btn1)
# group.addButton(btn2)
# # 添加事件
# group.buttonToggled.connect(on_group_toggled)
# # 将两个按钮添加到布局里面
# layout = QHBoxLayout()
# layout.addWidget(btn1)
# layout.addWidget(btn2)
# w.setLayout(layout)

# =======================================
# 多选框
def on_box_state_changed(index, arg):
    print("按钮", index)
    if arg == Qt.Checked:  # 2==Qt.Checked
        print("被选中")
    else:
        print("取消选中")


box1 = QCheckBox("抽烟")
box2 = QCheckBox("喝酒")
box3 = QCheckBox("烫头")
# 添加事件(使用lambad函数)
box1.stateChanged.connect(lambda arg: on_box_state_changed(1, arg))
box2.stateChanged.connect(lambda arg: on_box_state_changed(2, arg))
box3.stateChanged.connect(lambda arg: on_box_state_changed(3, arg))

# 创建布局
layout = QHBoxLayout()
layout.addWidget(box1)
layout.addWidget(box2)
layout.addWidget(box3)
w.setLayout(layout)

# =======================================
# 显示窗口
w.show()
# 阻塞主线程的while Ture
app.exit(app.exec())

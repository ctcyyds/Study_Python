from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from ui.Ui_main_window import Ui_MainWindow
from drivers.tcp_client import TcpClient


class NetMainWindow(QMainWindow):
    def __init__(self, parent=None):
        # 如果集成了别人的类，一定要调用父类构造方法
        super().__init__(parent)
        # 创建对象
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 创建TCP客户端
        self.tcp_client = None

        # 初始化UI工具
        self.init_ui()

    def on_connect_clicked(self):
        print("-----content")
        ip = self.ui.edit_target_ip.text()
        port = int(self.ui.edit_target_port.text())
        connect_log = "连接{}：{}".format(ip, port)
        print(connect_log)
        # 状态栏显示
        self.statusBar().showMessage(connect_log)

        # 获取本机IP和端口
        local_ip = self.ui.cb_local_ip.currentText()
        local_port = int(self.ui.edit_local_port.text())

        # 执行连接
        self.tcp_client = TcpClient(local_ip, local_port)
        connect_rst = self.tcp_client.connect(ip, port)
        if connect_rst:
            self.statusBar().showMessage("连接成功")
        else:
            self.statusBar().showMessage("连接失败,请重试")

    def on_send_clicked(self):
        print("-----send")
        send_text = self.ui.edit_send.toPlainText()
        print(send_text)
        # 状态栏显示
        self.statusBar().showMessage("发送消息！")

    def init_ui(self):
        # 给按钮添加绑定事件
        self.ui.btn_connect.clicked.connect(self.on_connect_clicked)
        self.ui.btn_send.clicked.connect(self.on_send_clicked)

        self.ui.cb_local_ip.addItem("")
        self.ui.cb_local_ip.addItem("127.0.0.1")

        # 添加工具栏
        tool_bar = QToolBar()
        self.addToolBar(tool_bar)

        # 创建工具栏上的保存按钮
        action_save = QAction("保存", self)
        action_save.setIcon(QIcon("img/txt_save.png"))
        # 创建事件
        action_save.triggered.connect(lambda: print("保存"))
        tool_bar.addAction(action_save)

        # 创建工具栏上的打开文件按钮
        action_open = QAction("打开", self)
        action_open.setIcon(QIcon("img/txt_open.png"))
        # 创建事件
        action_open.triggered.connect(lambda: print("打开"))
        tool_bar.addAction(action_open)

        # 创建工具栏上的撤销按钮
        action_undo = QAction("撤销", self)
        action_undo.setIcon(QIcon("img/txt_return.png"))
        # 创建事件
        action_undo.triggered.connect(lambda: print("撤销"))
        tool_bar.addAction(action_undo)

        # 创建菜单栏
        self.ui.action_save.triggered.connect(lambda: print("保存"))
        self.ui.action_exit.triggered.connect(QApplication.quit)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NetMainWindow()
    window.show()

    sys.exit(app.exec_())

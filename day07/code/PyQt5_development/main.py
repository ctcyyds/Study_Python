from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

import tools.utils
from ui.Ui_main_window import Ui_net_window
from drivers.tcp_client import TcpClient
from tools.utils import *


class net_window(QMainWindow):
    def __init__(self, parent=None):
        # 如果集成了别人的类，一定要调用父类构造方法
        super().__init__(parent)
        # 创建对象
        self.ui = Ui_net_window()
        self.ui.setupUi(self)

        # 创建TCP客户端
        self.tcp_client: TcpClient = None

        self.ui.edit_recv.appendPlainText("Hello world!")

        # 初始化UI工具
        self.init_ui()

        # 将本地IP加载到本地
        self.init_data()

    @pyqtSlot(str)
    def on_msg_recv(self, msg):
        self.ui.edit_recv.appendPlainText(msg)

    def on_connect_clicked(self):
        if self.tcp_client is not None:
            # 已经连接了，需要断开连接
            self.tcp_client.relase()
            self.tcp_client = None
            self.updat_current_state()
            return

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

        # 绑定信号槽
        self.tcp_client.msg_signal.connect(self.on_msg_recv)

        # 连接服务器
        success, socket_name = self.tcp_client.connect(ip, port)
        if success:
            self.statusBar().showMessage("连接成功")
            ip, port = socket_name
            current_ip_index = self.ui.cb_local_ip.findText(ip)
            self.ui.cb_local_ip.setCurrentIndex(current_ip_index)
            self.ui.edit_local_port.setText(str(port))
        else:
            self.statusBar().showMessage("连接失败,请重试")
            self.tcp_client.relase()
            self.tcp_client = None
        self.updat_current_state()

    def updat_current_state(self):
        """
        设置连接按钮状态
        :return:
        """
        if self.tcp_client is None:
            self.ui.btn_connect.setText("连接网络")
        else:
            self.ui.btn_connect.setText("断开网络")

    def on_send_clicked(self):
        print("-----send")
        send_text = self.ui.edit_send.toPlainText()
        print(send_text)
        # 状态栏显示
        self.statusBar().showMessage("发送消息！")

        self.tcp_client.send(send_text + "\n")

    def init_ui(self):
        # 给按钮添加绑定事件
        self.ui.btn_connect.clicked.connect(self.on_connect_clicked)
        self.ui.btn_send.clicked.connect(self.on_send_clicked)

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

    def init_data(self):
        """
        将本地所有IP加载到图形化工具中的下拉框中
        :return:
        """
        local_ips = tools.utils.get_local_ip()
        self.ui.cb_local_ip.addItems(local_ips)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = net_window()
    window.show()

    sys.exit(app.exec_())

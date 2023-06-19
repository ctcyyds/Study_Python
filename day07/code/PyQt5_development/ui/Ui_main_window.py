# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_net_window(object):
    def setupUi(self, net_window):
        net_window.setObjectName("net_window")
        net_window.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon_logo"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        net_window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(net_window)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(260, 0))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.edit_target_port = QtWidgets.QLineEdit(self.groupBox)
        self.edit_target_port.setObjectName("edit_target_port")
        self.gridLayout.addWidget(self.edit_target_port, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.btn_connect = QtWidgets.QPushButton(self.groupBox)
        self.btn_connect.setObjectName("btn_connect")
        self.gridLayout.addWidget(self.btn_connect, 3, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.edit_target_ip = QtWidgets.QLineEdit(self.groupBox)
        self.edit_target_ip.setObjectName("edit_target_ip")
        self.gridLayout.addWidget(self.edit_target_ip, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.edit_recv = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.edit_recv.setReadOnly(True)
        self.edit_recv.setObjectName("edit_recv")
        self.verticalLayout.addWidget(self.edit_recv)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.cb_local_ip = QtWidgets.QComboBox(self.centralwidget)
        self.cb_local_ip.setObjectName("cb_local_ip")
        self.horizontalLayout_2.addWidget(self.cb_local_ip)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.edit_local_port = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_local_port.sizePolicy().hasHeightForWidth())
        self.edit_local_port.setSizePolicy(sizePolicy)
        self.edit_local_port.setMinimumSize(QtCore.QSize(60, 0))
        self.edit_local_port.setMaximumSize(QtCore.QSize(60, 16777215))
        self.edit_local_port.setObjectName("edit_local_port")
        self.horizontalLayout_2.addWidget(self.edit_local_port)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.edit_send = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.edit_send.setMinimumSize(QtCore.QSize(0, 200))
        self.edit_send.setMaximumSize(QtCore.QSize(16777215, 300))
        self.edit_send.setObjectName("edit_send")
        self.horizontalLayout_3.addWidget(self.edit_send)
        self.btn_send = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_send.sizePolicy().hasHeightForWidth())
        self.btn_send.setSizePolicy(sizePolicy)
        self.btn_send.setObjectName("btn_send")
        self.horizontalLayout_3.addWidget(self.btn_send)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(0, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_4.setStretch(1, 1)
        net_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(net_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        net_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(net_window)
        self.statusbar.setObjectName("statusbar")
        net_window.setStatusBar(self.statusbar)
        self.action_save = QtWidgets.QAction(net_window)
        self.action_save.setObjectName("action_save")
        self.actionLoading = QtWidgets.QAction(net_window)
        self.actionLoading.setObjectName("actionLoading")
        self.action_exit = QtWidgets.QAction(net_window)
        self.action_exit.setObjectName("action_exit")
        self.actionAbout = QtWidgets.QAction(net_window)
        self.actionAbout.setObjectName("actionAbout")
        self.menu.addSeparator()
        self.menu.addAction(self.action_save)
        self.menu.addAction(self.actionLoading)
        self.menu.addAction(self.action_exit)
        self.menu_2.addAction(self.actionAbout)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(net_window)
        QtCore.QMetaObject.connectSlotsByName(net_window)

    def retranslateUi(self, net_window):
        _translate = QtCore.QCoreApplication.translate
        net_window.setWindowTitle(_translate("net_window", "网络工具"))
        self.groupBox.setTitle(_translate("net_window", "网络设置"))
        self.edit_target_port.setText(_translate("net_window", "8888"))
        self.label_2.setText(_translate("net_window", "服务器IP："))
        self.btn_connect.setText(_translate("net_window", "连接网络"))
        self.comboBox.setItemText(0, _translate("net_window", "TCP服务端"))
        self.comboBox.setItemText(1, _translate("net_window", "TCP客户端"))
        self.comboBox.setItemText(2, _translate("net_window", "UDP"))
        self.label.setText(_translate("net_window", "设置模式："))
        self.edit_target_ip.setInputMask(_translate("net_window", "000.000.000.000"))
        self.edit_target_ip.setText(_translate("net_window", "..."))
        self.label_3.setText(_translate("net_window", "服务器端口："))
        self.label_4.setText(_translate("net_window", "本地IP:"))
        self.label_5.setText(_translate("net_window", "本地端口："))
        self.edit_local_port.setInputMask(_translate("net_window", "99999"))
        self.edit_local_port.setText(_translate("net_window", "0"))
        self.btn_send.setText(_translate("net_window", "发送"))
        self.menu.setTitle(_translate("net_window", "文件"))
        self.menu_2.setTitle(_translate("net_window", "帮助"))
        self.action_save.setText(_translate("net_window", "Save"))
        self.actionLoading.setText(_translate("net_window", "Loading"))
        self.action_exit.setText(_translate("net_window", "Exit"))
        self.actionAbout.setText(_translate("net_window", "About"))
from ui import resource_rc

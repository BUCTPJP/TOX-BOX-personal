# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\办公学习\学习\理\编程设计\python\Python项目\工具盒\v2.0\UI\common.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1066, 626)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/common.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1066, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(1066, 600))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 1066, 600))
        self.frame_4.setMinimumSize(QtCore.QSize(1066, 600))
        self.frame_4.setMaximumSize(QtCore.QSize(1066, 600))
        self.frame_4.setStyleSheet("QFrame{\n"
"    \n"
"    background-image: url(:/img/common_bg.jpg);\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_4)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setStyleSheet("QFrame{\n"
"    background:rgba(255, 255, 255, 100)\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setContentsMargins(72, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("站酷小薇LOGO体")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 219, 241);\n"
"    border-radius:10px;\n"
"    border-width: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"    font: 16pt \"站酷小薇LOGO体\";\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("站酷小薇LOGO体")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(230, 225, 255);\n"
"    border-radius:10px;\n"
"    border-width: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"    font: 16pt \"站酷小薇LOGO体\";\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("站酷小薇LOGO体")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background-color: rgb(241, 255, 234);\n"
"    border-radius:10px;\n"
"    border-width: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"    font: 16pt \"站酷小薇LOGO体\";\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("站酷小薇LOGO体")
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(255, 248, 210);\n"
"    border-radius:10px;\n"
"    border-width: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"    font: 16pt \"站酷小薇LOGO体\";\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("站酷小薇LOGO体")
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(216, 255, 228);\n"
"    border-radius:10px;\n"
"    border-width: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"    font: 16pt \"站酷小薇LOGO体\";\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_6.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("站酷小薇LOGO体")
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(255, 216, 201);\n"
"    border-radius:10px;\n"
"    border-width: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"    font: 16pt \"站酷小薇LOGO体\";\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame = QtWidgets.QFrame(self.frame_4)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setStyleSheet("QFrame{\n"
"    background:rgba(255, 255, 255, 100)\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(72, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("站酷小薇LOGO体")
        font.setPointSize(14)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(255, 188, 198);\n"
"    border-radius:10px;\n"
"    border-width: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"    font: 16pt \"站酷小薇LOGO体\";\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("站酷小薇LOGO体")
        font.setPointSize(14)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(218, 203, 255);\n"
"    border-radius:10px;\n"
"    border-width: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"    font: 16pt \"站酷小薇LOGO体\";\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_2.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    border-width: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"    font: 16pt \"站酷小薇LOGO体\";\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_2.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    border-width: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"    font: 16pt \"站酷小薇LOGO体\";\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_2.addWidget(self.pushButton_11)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    border-width: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"    font: 16pt \"站酷小薇LOGO体\";\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    border-width: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"    font: 16pt \"站酷小薇LOGO体\";\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_2.addWidget(self.pushButton_12)
        self.horizontalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setStyleSheet("QFrame{\n"
"    background:rgba(255, 255, 255, 100)\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(72, -1, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_18.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton_18.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    border-width: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"    font: 16pt \"站酷小薇LOGO体\";\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_18.setObjectName("pushButton_18")
        self.verticalLayout_3.addWidget(self.pushButton_18)
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_13.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    border-width: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"    font: 16pt \"站酷小薇LOGO体\";\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_3.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_14.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton_14.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    border-width: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"    font: 16pt \"站酷小薇LOGO体\";\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_3.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_15.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton_15.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    border-width: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"    font: 16pt \"站酷小薇LOGO体\";\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout_3.addWidget(self.pushButton_15)
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_16.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton_16.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    border-width: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"    font: 16pt \"站酷小薇LOGO体\";\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_16.setObjectName("pushButton_16")
        self.verticalLayout_3.addWidget(self.pushButton_16)
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_17.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton_17.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    border-width: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"    font: 16pt \"站酷小薇LOGO体\";\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_17.setObjectName("pushButton_17")
        self.verticalLayout_3.addWidget(self.pushButton_17)
        self.horizontalLayout_2.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1066, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "BMI指数计算"))
        self.pushButton_2.setText(_translate("MainWindow", "温度转换"))
        self.pushButton_3.setText(_translate("MainWindow", "疫情查询"))
        self.pushButton_4.setText(_translate("MainWindow", "二维码生成"))
        self.pushButton_5.setText(_translate("MainWindow", "解析二维码"))
        self.pushButton_6.setText(_translate("MainWindow", "图种制作"))
        self.pushButton_8.setText(_translate("MainWindow", "词频统计(en)"))
        self.pushButton_9.setText(_translate("MainWindow", "B站视频下载"))
        self.pushButton_10.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_11.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_12.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_18.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_13.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_14.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_15.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_16.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_17.setText(_translate("MainWindow", "PushButton"))
import img_rc

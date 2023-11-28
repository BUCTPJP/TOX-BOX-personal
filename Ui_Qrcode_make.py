# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\办公学习\学习\理\编程设计\python\Python项目\工具盒\v2.0\UI\Qrcode_make.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        MainWindow.setMinimumSize(QtCore.QSize(960, 540))
        MainWindow.setMaximumSize(QtCore.QSize(960, 540))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/QRcode_make.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.frame.setMinimumSize(QtCore.QSize(960, 540))
        self.frame.setMaximumSize(QtCore.QSize(960, 540))
        self.frame.setStyleSheet("QFrame{\n"
"    \n"
"    background-image:url(:/img/qr_make_bg.jpg);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 11)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(213, 255, 241);\n"
"    border-color: rgb(0, 0, 0);\n"
"    border-radius:20px\n"
"}\n"
"QPushButton::hover{\n"
"    \n"
"    background-color: rgb(234, 234, 234);\n"
"    font: 15pt \"隶书\";\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(206, 226, 255);\n"
"    border-color: rgb(0, 0, 0);\n"
"    border-radius:20px\n"
"}\n"
"QPushButton::hover{\n"
"    \n"
"    background-color: rgb(234, 234, 234);\n"
"    font:10pt\"隶书\";\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(252, 216, 255);\n"
"    border-color: rgb(0, 0, 0);\n"
"    border-radius:20px\n"
"}\n"
"QPushButton::hover{\n"
"    \n"
"    background-color: rgb(234, 234, 234);\n"
"    font:10pt\"隶书\";\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(255, 252, 179);\n"
"    border-color: rgb(0, 0, 0);\n"
"    border-radius:20px\n"
"}\n"
"QPushButton::hover{\n"
"    \n"
"    background-color: rgb(234, 234, 234);\n"
"    font:10pt\"隶书\";\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(560, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label.setStyleSheet("QLabel{\n"
"    background:rgba(213, 215, 255, 0);\n"
"}")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 300))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"    background:rgba(255, 255, 255, 100);\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_2.setStyleSheet("QLabel{\n"
"    background:rgba(213, 215, 255, 0);\n"
"}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_3.setStyleSheet("QLabel{\n"
"    background:rgba(213, 215, 255, 0);\n"
"}")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setMaximumSize(QtCore.QSize(300, 80))
        self.label_4.setStyleSheet("QLabel{\n"
"    background:rgba(255, 255, 255, 100);\n"
"}")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_4)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 250))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.horizontalLayout.addWidget(self.frame_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "直接生成"))
        self.pushButton_2.setText(_translate("MainWindow", "选择Logo并生成"))
        self.pushButton_3.setText(_translate("MainWindow", "选择背景并生成"))
        self.pushButton_4.setText(_translate("MainWindow", "使用帮助"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">请输入二维码要显示的内容:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">请输入二维码要保存的文件名:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">请输入二维码想要保存的颜色:</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">颜色需要输入代码 </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">可参照如下网址 </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">https://blog.csdn.net/ </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">TheLittlePython/article/ </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">details/79063779 </span></p></body></html>"))
import img_rc

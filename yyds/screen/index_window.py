# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(482, 308)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setStyleSheet("")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(300, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.checkButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.checkButton.setFont(font)
        self.checkButton.setObjectName("checkButton")
        self.verticalLayout.addWidget(self.checkButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cleanPortButton = QtWidgets.QPushButton(Form)
        self.cleanPortButton.setObjectName("cleanPortButton")
        self.verticalLayout_2.addWidget(self.cleanPortButton)
        self.downButton = QtWidgets.QPushButton(Form)
        self.downButton.setObjectName("downButton")
        self.verticalLayout_2.addWidget(self.downButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.yes_checkBox = QtWidgets.QCheckBox(Form)
        self.yes_checkBox.setMinimumSize(QtCore.QSize(20, 0))
        self.yes_checkBox.setMaximumSize(QtCore.QSize(20, 16777215))
        self.yes_checkBox.setText("")
        self.yes_checkBox.setChecked(True)
        self.yes_checkBox.setObjectName("yes_checkBox")
        self.horizontalLayout_3.addWidget(self.yes_checkBox)
        self.note_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.note_label.setFont(font)
        self.note_label.setObjectName("note_label")
        self.horizontalLayout_3.addWidget(self.note_label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.login_pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_pushButton.setFont(font)
        self.login_pushButton.setObjectName("login_pushButton")
        self.verticalLayout.addWidget(self.login_pushButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "授权使用"))
        self.label.setText(_translate("Form", "欢迎使用办公小助手！"))
        self.checkButton.setText(_translate("Form", "1、环境检测"))
        self.textEdit.setPlaceholderText(_translate("Form",
                                                    "使用说明：所依赖的微信版本必须匹配3.9.2.23 ; 安装微信后到设置页选择通用设置关闭（有更新时自动升级微信）"))
        self.cleanPortButton.setText(_translate("Form", "1.1清理占用端口"))
        self.downButton.setText(_translate("Form", "1.2下载对应微信"))
        self.note_label.setText(_translate("Form", "我已阅读同意<服务和隐私协议>，同时授权系统使用登录微信做权限管理"))
        self.login_pushButton.setText(_translate("Form", "2、进入使用"))
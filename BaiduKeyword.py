# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 440)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.findpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.findpushButton.setGeometry(QtCore.QRect(230, 20, 75, 27))
        self.findpushButton.setObjectName("findpushButton")
        self.exportpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.exportpushButton.setGeometry(QtCore.QRect(310, 20, 75, 27))
        self.exportpushButton.setObjectName("exportpushButton")
        self.keywordtextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.keywordtextEdit.setGeometry(QtCore.QRect(20, 90, 371, 321))
        self.keywordtextEdit.setObjectName("keywordtextEdit")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 193, 32))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.keywordlabel = QtWidgets.QLabel(self.widget)
        self.keywordlabel.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.keywordlabel.setFont(font)
        self.keywordlabel.setObjectName("keywordlabel")
        self.horizontalLayout.addWidget(self.keywordlabel)
        self.keywordlineEdit = QtWidgets.QLineEdit(self.widget)
        self.keywordlineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.keywordlineEdit.setObjectName("keywordlineEdit")
        self.horizontalLayout.addWidget(self.keywordlineEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.findpushButton.clicked.connect(MainWindow.run)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "百度关键词采集 by 南瓜"))
        self.findpushButton.setText(_translate("MainWindow", "查询"))
        self.exportpushButton.setText(_translate("MainWindow", "导出"))
        self.keywordlabel.setText(_translate("MainWindow", "关键词："))


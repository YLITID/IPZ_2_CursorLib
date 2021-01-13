# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUIOrder.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_Order(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint | Qt.WindowMinimizeButtonHint)
        self.textBrowser_description = QTextBrowser(Dialog)
        self.textBrowser_description.setObjectName(u"textBrowser_description")
        self.textBrowser_description.setGeometry(QRect(10, 140, 256, 141))
        self.textBrowser_Details = QTextBrowser(Dialog)
        self.textBrowser_Details.setObjectName(u"textBrowser_Details")
        self.textBrowser_Details.setGeometry(QRect(10, 60, 256, 41))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 121, 16))
        palette = QPalette()
        brush = QBrush(QColor(0, 85, 127, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.label.setPalette(palette)
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.RichText)
        self.label.setScaledContents(False)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 121, 16))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.label_2.setPalette(palette1)
        self.label_2.setFont(font)
        self.textBrowser_Details.setFont(font)
        self.label_2.setTextFormat(Qt.RichText)
        self.label_2.setScaledContents(False)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 120, 47, 13))
        self.pushButton_order = QPushButton(Dialog)
        self.pushButton_order.setObjectName(u"pushButton_order")
        self.pushButton_order.setGeometry(QRect(280, 60, 91, 31))
        self.pushButton_Download = QPushButton(Dialog)
        self.pushButton_Download.setObjectName(u"pushButton_Download")
        self.pushButton_Download.setGeometry(QRect(280, 250, 91, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"ChangeName", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Cursor Library", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441:", None))
        self.pushButton_order.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043c\u043e\u0432\u0438\u0442\u0438", None))
        self.pushButton_Download.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0432\u0430\u043d\u0442\u0430\u0436\u0438\u0442\u0438 ", None))
    # retranslateUi


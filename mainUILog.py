# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUILog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_start_Login(object):
    def setupUi(self, Dialog_start):
        if not Dialog_start.objectName():
            Dialog_start.setObjectName(u"Dialog_start")
        Dialog_start.setEnabled(True)
        Dialog_start.resize(228, 171)
        Dialog_start.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint | Qt.WindowMinimizeButtonHint)
        self.pushButton_Login = QPushButton(Dialog_start)
        self.pushButton_Login.setObjectName(u"pushButton_Login")
        self.pushButton_Login.setGeometry(QRect(70, 120, 75, 23))
        self.lineEdit_user_id = QLineEdit(Dialog_start)
        self.lineEdit_user_id.setObjectName(u"lineEdit_user_id")
        self.lineEdit_user_id.setGeometry(QRect(70, 45, 113, 20))
        self.lineEdit_password = QLineEdit(Dialog_start)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setGeometry(QRect(70, 80, 113, 20))
        self.lineEdit_password.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.label_User_id = QLabel(Dialog_start)
        self.label_User_id.setObjectName(u"label_User_id")
        self.label_User_id.setGeometry(QRect(10, 40, 51, 31))
        self.label_Password = QLabel(Dialog_start)
        self.label_Password.setObjectName(u"label_Password")
        self.label_Password.setGeometry(QRect(10, 75, 51, 31))
        self.line = QFrame(Dialog_start)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-30, 260, 531, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_success = QLabel(Dialog_start)
        self.label_success.setObjectName(u"label_success")
        self.label_success.setGeometry(QRect(70, 27, 67, 13))
        self.label_TimeR_St = QLabel(Dialog_start)
        self.label_TimeR_St.setObjectName(u"label_TimeR_St")
        self.label_TimeR_St.setGeometry(QRect(110, 150, 151, 31))
        self.label_TimeR_St.hide()
        self.labelCURS = QLabel(Dialog_start)
        self.labelCURS.setObjectName(u"label")
        self.labelCURS.setGeometry(QRect(10, 10, 121, 16))
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
        self.labelCURS.setPalette(palette)
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelCURS.setFont(font)
        self.labelCURS.setTextFormat(Qt.RichText)
        self.labelCURS.setScaledContents(False)

        self.retranslateUi(Dialog_start)

        QMetaObject.connectSlotsByName(Dialog_start)
    # setupUi
    #def showTime(self):
    #    time = QTime.currentTime()
    #    text = time.toString('hh:mm:ss')
    #    text = "Current time: "+text
    #   self.label_TimeR_St.setText(text)




    def retranslateUi(self, Dialog_start):
     #   timer = QTimer(Dialog_start)
     #   timer.connect(timer, SIGNAL('timeout()'), self.showTime)
     #   timer.start(10)

     #   time_now = self.showTime()


        Dialog_start.setWindowTitle(QCoreApplication.translate("Dialog_start", u"Dialog", None))
        self.pushButton_Login.setText(QCoreApplication.translate("Dialog_start", u"\u0412\u0445\u0456\u0434", None))
        self.label_User_id.setText(QCoreApplication.translate("Dialog_start", u"User_id", None))
        self.label_Password.setText(QCoreApplication.translate("Dialog_start", u"Password", None))
        self.label_success.setText("")

        self.labelCURS.setText(QCoreApplication.translate("Dialog_start", u"Cursor Library", None))
    # retranslateUi



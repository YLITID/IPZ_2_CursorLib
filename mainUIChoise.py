# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUIChoise.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_Choise(object):
    def setupUi(self, Dialog_Choise):
        if not Dialog_Choise.objectName():
            Dialog_Choise.setObjectName(u"Dialog_Choise")
        Dialog_Choise.setEnabled(True)
        Dialog_Choise.resize(702, 288)
        Dialog_Choise.setFocusPolicy(Qt.NoFocus)
        Dialog_Choise.setAutoFillBackground(False)
        Dialog_Choise.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint | Qt.WindowMinimizeButtonHint)
        self.pushButton_Search = QPushButton(Dialog_Choise)
        self.pushButton_Search.setObjectName(u"pushButton_Search")
        self.pushButton_Search.setGeometry(QRect(140, 240, 75, 23))
        self.lineEdit_find = QLineEdit(Dialog_Choise)
        self.lineEdit_find.setObjectName(u"lineEdit_find")
        self.lineEdit_find.setGeometry(QRect(10, 240, 113, 20))
        self.line = QFrame(Dialog_Choise)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-30, 260, 931, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_success = QLabel(Dialog_Choise)
        self.label_success.setObjectName(u"label_success")
        self.label_success.setGeometry(QRect(200, 280, 47, 13))
        self.label_TimeR_St = QLabel(Dialog_Choise)
        self.label_TimeR_St.setObjectName(u"label_TimeR_St")
        self.label_TimeR_St.setGeometry(QRect(430, 50, 51, 31))
        self.label = QLabel(Dialog_Choise)
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
        self.tableView = QTableView(Dialog_Choise)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 30, 460, 160))
        self.comboBox_Genre = QComboBox(Dialog_Choise)
        self.comboBox_Genre.setObjectName(u"comboBox_Genre")
        self.comboBox_Genre.setGeometry(QRect(480, 50, 69, 22))
        self.label_Genres = QLabel(Dialog_Choise)
        self.label_Genres.setObjectName(u"label_Genres")
        self.label_Genres.setGeometry(QRect(480, 30, 47, 13))
        self.comboBox_year = QComboBox(Dialog_Choise)
        self.comboBox_year.setObjectName(u"comboBox_year")
        self.comboBox_year.setGeometry(QRect(580, 50, 69, 22))
        self.label_year = QLabel(Dialog_Choise)
        self.label_year.setObjectName(u"label_year")
        self.label_year.setGeometry(QRect(580, 30, 91, 16))
        self.comboBox_vidav = QComboBox(Dialog_Choise)
        self.comboBox_vidav.setObjectName(u"comboBox_vidav")
        self.comboBox_vidav.setGeometry(QRect(480, 100, 69, 22))
        self.label_vidav = QLabel(Dialog_Choise)
        self.label_vidav.setObjectName(u"label_vidav")
        self.label_vidav.setGeometry(QRect(480, 80, 71, 16))
        self.comboBox_labg = QComboBox(Dialog_Choise)
        self.comboBox_labg.setObjectName(u"comboBox_labg")
        self.comboBox_labg.setGeometry(QRect(580, 100, 69, 22))
        self.label_lang = QLabel(Dialog_Choise)
        self.label_lang.setObjectName(u"label_lang")
        self.label_lang.setGeometry(QRect(580, 80, 47, 13))
        self.pushButton_Choise = QPushButton(Dialog_Choise)
        self.pushButton_Choise.setObjectName(u"pushButton_Choise")
        self.pushButton_Choise.setGeometry(QRect(480, 150, 71, 23))
        self.label_Find = QLabel(Dialog_Choise)
        self.label_Find.setObjectName(u"label_Find")
        self.label_Find.setGeometry(QRect(10, 220, 47, 13))
        self.pushButton_toBook = QPushButton(Dialog_Choise)
        self.pushButton_toBook.setObjectName(u"pushButton_toBook")
        self.pushButton_toBook.setGeometry(QRect(480, 200, 71, 23))
        self.retranslateUi(Dialog_Choise)

        QMetaObject.connectSlotsByName(Dialog_Choise)
    # setupUi

    def retranslateUi(self, Dialog_Choise):
        Dialog_Choise.setWindowTitle(QCoreApplication.translate("Dialog_Choise", u"CursorLib", None))
        self.pushButton_Search.setText(QCoreApplication.translate("Dialog_Choise", u"\u0417\u043d\u0430\u0439\u0442\u0438", None))
        self.label_success.setText("")
        self.label_TimeR_St.setText("")
        self.pushButton_toBook.setText("Забронювати")
        self.label.setText(QCoreApplication.translate("Dialog_Choise", u"Cursor Library", None))
        self.label_Genres.setText(QCoreApplication.translate("Dialog_Choise", u"\u0416\u0430\u043d\u0440", None))
        self.label_year.setText(QCoreApplication.translate("Dialog_Choise", u"\u0420\u0456\u043a \u0432\u0438\u043f\u0443\u0441\u043a\u0443", None))
        self.label_vidav.setText(QCoreApplication.translate("Dialog_Choise", u"\u0412\u0438\u0434\u0430\u0432\u043d\u0438\u0446\u0442\u0432\u043e", None))
        self.label_lang.setText(QCoreApplication.translate("Dialog_Choise", u"\u041c\u043e\u0432\u0430", None))
        self.pushButton_Choise.setText(QCoreApplication.translate("Dialog_Choise", u"\u0412\u0438\u0431\u0440\u0430\u0442\u0438", None))
        self.label_Find.setText(QCoreApplication.translate("Dialog_Choise", u"\u041f\u043e\u0448\u0443\u043a", None))
    # retranslateUi


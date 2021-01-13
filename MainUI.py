from mainUILog import *
from mainUIChoise import *
from mainUIOrder import *
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_show_error():
    def setupUi(self, Dialog_start):
        if not Dialog_start.objectName():
            Dialog_start.setObjectName(u"Dialog_start")
        Dialog_start.setEnabled(True)
        Dialog_start.resize(160, 80)
        Dialog_start.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.pushButton_OK = QPushButton(Dialog_start)
        self.pushButton_OK.setObjectName(u"pushButton_OK")
        self.pushButton_OK.setGeometry(QRect(40, 40, 75, 23))
        self.label_Err = QLabel(Dialog_start)
        self.label_Err.setObjectName(u"label_User_id")
        self.label_Err.setGeometry(QRect(40, 7, 251, 31))

        self.retranslateUi(Dialog_start)

    def retranslateUi(self, Dialog_start):
        Dialog_start.setWindowTitle('Error')
        self.label_Err.setText('Connection Error')
        self.pushButton_OK.setText("Reconnect")
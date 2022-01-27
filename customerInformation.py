from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Ui_customerInformation(object):
    def setupUi(self, customerInformation):
        customerInformation.setObjectName("customerInformation")
        customerInformation.resize(700, 571)
        customerInformation.setStyleSheet("background-color: rgb(204, 13, 48);")
        self.frame = QtWidgets.QFrame(customerInformation)
        self.frame.setGeometry(QtCore.QRect(80, 20, 551, 80))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.waiterLabel = QtWidgets.QLabel(self.frame)
        self.waiterLabel.setGeometry(QtCore.QRect(110, 20, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Times")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.waiterLabel.setFont(font)
        self.waiterLabel.setObjectName("waiterLabel")
        self.line = QtWidgets.QFrame(customerInformation)
        self.line.setGeometry(QtCore.QRect(40, 110, 621, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.informationLabel = QtWidgets.QLabel(customerInformation)
        self.informationLabel.setGeometry(QtCore.QRect(40, 140, 371, 16))
        font = QtGui.QFont()
        font.setFamily("Times")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.informationLabel.setFont(font)
        self.informationLabel.setObjectName("informationLabel")
        self.line_2 = QtWidgets.QFrame(customerInformation)
        self.line_2.setGeometry(QtCore.QRect(50, 180, 271, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.addressTextEdit = QtWidgets.QTextEdit(customerInformation)
        self.addressTextEdit.setGeometry(QtCore.QRect(40, 420, 541, 141))
        self.addressTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.addressTextEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.addressTextEdit.setObjectName("addressTextEdit")
        self.dateLineEdit = QtWidgets.QLineEdit(customerInformation)
        self.dateLineEdit.setGeometry(QtCore.QRect(260, 210, 181, 23))
        self.dateLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateLineEdit.setText("")
        self.dateLineEdit.setObjectName("dateLineEdit")
        self.codeLineEdit = QtWidgets.QLineEdit(customerInformation)
        self.codeLineEdit.setGeometry(QtCore.QRect(40, 370, 281, 23))
        self.codeLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.codeLineEdit.setObjectName("codeLineEdit")
        self.timeLineEdit = QtWidgets.QLineEdit(customerInformation)
        self.timeLineEdit.setGeometry(QtCore.QRect(460, 210, 161, 23))
        self.timeLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.timeLineEdit.setObjectName("timeLineEdit")
        self.contactTextEdit = QtWidgets.QTextEdit(customerInformation)
        self.contactTextEdit.setGeometry(QtCore.QRect(40, 280, 531, 71))
        self.contactTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.contactTextEdit.setObjectName("contactTextEdit")

        self.retranslateUi(customerInformation)
        QtCore.QMetaObject.connectSlotsByName(customerInformation)

    def retranslateUi(self, customerInformation):
        _translate = QtCore.QCoreApplication.translate
        customerInformation.setWindowTitle(_translate("customerInformation", "Dialog"))
        self.waiterLabel.setText(_translate("customerInformation", "WAITER ON WHEELS"))
        self.informationLabel.setText(_translate("customerInformation", "CUSTOMER INFORMATION"))
        self.addressTextEdit.setPlaceholderText(_translate("customerInformation", "Customer Address:"))
        self.dateLineEdit.setPlaceholderText(_translate("customerInformation", "Date"))
        self.codeLineEdit.setPlaceholderText(_translate("customerInformation", "Customer Code:"))
        self.timeLineEdit.setPlaceholderText(_translate("customerInformation", "Time"))
        self.contactTextEdit.setHtml(_translate("customerInformation", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Customer Name:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Customer Phone:</span></p></body></html>"))
        self.contactTextEdit.setPlaceholderText(_translate("customerInformation", "Customer Name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    customerInformation = QtWidgets.QDialog()
    ui = Ui_customerInformation()
    ui.setupUi(customerInformation)
    customerInformation.show()
    sys.exit(app.exec_())


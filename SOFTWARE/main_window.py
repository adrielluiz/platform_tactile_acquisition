# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(711, 594)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        self.comboBoxSerialPort = QtWidgets.QComboBox(Dialog)
        self.comboBoxSerialPort.setGeometry(QtCore.QRect(260, 40, 73, 22))
        self.comboBoxSerialPort.setObjectName("comboBoxSerialPort")
        self.label_porta_serial = QtWidgets.QLabel(Dialog)
        self.label_porta_serial.setGeometry(QtCore.QRect(50, 40, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_porta_serial.setFont(font)
        self.label_porta_serial.setObjectName("label_porta_serial")
        self.pbConectarSerial = QtWidgets.QPushButton(Dialog)
        self.pbConectarSerial.setGeometry(QtCore.QRect(370, 30, 93, 28))
        self.pbConectarSerial.setObjectName("pbConectarSerial")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_porta_serial.setText(_translate("Dialog", "Selecione a porta serial:"))
        self.pbConectarSerial.setText(_translate("Dialog", "Conectar"))

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
        Dialog.resize(740, 658)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(30, 90, 691, 551))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_coleta = QtWidgets.QWidget()
        self.tab_coleta.setObjectName("tab_coleta")
        self.tabWidget.addTab(self.tab_coleta, "")
        self.tab_teste = QtWidgets.QWidget()
        self.tab_teste.setObjectName("tab_teste")
        self.horizontalSliderX = QtWidgets.QSlider(self.tab_teste)
        self.horizontalSliderX.setGeometry(QtCore.QRect(130, 30, 160, 22))
        self.horizontalSliderX.setMaximum(160)
        self.horizontalSliderX.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderX.setObjectName("horizontalSliderX")
        self.verticalSliderZ = QtWidgets.QSlider(self.tab_teste)
        self.verticalSliderZ.setGeometry(QtCore.QRect(130, 80, 22, 160))
        self.verticalSliderZ.setMaximum(35)
        self.verticalSliderZ.setOrientation(QtCore.Qt.Vertical)
        self.verticalSliderZ.setObjectName("verticalSliderZ")
        self.pbHomeX = QtWidgets.QPushButton(self.tab_teste)
        self.pbHomeX.setGeometry(QtCore.QRect(10, 30, 93, 28))
        self.pbHomeX.setObjectName("pbHomeX")
        self.pbHomeZ = QtWidgets.QPushButton(self.tab_teste)
        self.pbHomeZ.setGeometry(QtCore.QRect(10, 130, 93, 28))
        self.pbHomeZ.setObjectName("pbHomeZ")
        self.frame = QtWidgets.QFrame(self.tab_teste)
        self.frame.setGeometry(QtCore.QRect(250, 70, 141, 141))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbMode = QtWidgets.QLabel(self.frame)
        self.lbMode.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbMode.setAlignment(QtCore.Qt.AlignCenter)
        self.lbMode.setObjectName("lbMode")
        self.verticalLayout.addWidget(self.lbMode)
        self.rbModeIdle = QtWidgets.QRadioButton(self.frame)
        self.rbModeIdle.setChecked(True)
        self.rbModeIdle.setObjectName("rbModeIdle")
        self.verticalLayout.addWidget(self.rbModeIdle)
        self.rbModeReadData = QtWidgets.QRadioButton(self.frame)
        self.rbModeReadData.setObjectName("rbModeReadData")
        self.verticalLayout.addWidget(self.rbModeReadData)
        self.pbSendMode = QtWidgets.QPushButton(self.frame)
        self.pbSendMode.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pbSendMode.setObjectName("pbSendMode")
        self.verticalLayout.addWidget(self.pbSendMode)
        self.frame_2 = QtWidgets.QFrame(self.tab_teste)
        self.frame_2.setGeometry(QtCore.QRect(460, 10, 191, 191))
        self.frame_2.setAutoFillBackground(True)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbEnableVar = QtWidgets.QLabel(self.frame_2)
        self.lbEnableVar.setAlignment(QtCore.Qt.AlignCenter)
        self.lbEnableVar.setObjectName("lbEnableVar")
        self.verticalLayout_2.addWidget(self.lbEnableVar)
        self.checkBoxMPU = QtWidgets.QCheckBox(self.frame_2)
        self.checkBoxMPU.setEnabled(False)
        self.checkBoxMPU.setObjectName("checkBoxMPU")
        self.verticalLayout_2.addWidget(self.checkBoxMPU)
        self.checkBoxPosition = QtWidgets.QCheckBox(self.frame_2)
        self.checkBoxPosition.setChecked(True)
        self.checkBoxPosition.setObjectName("checkBoxPosition")
        self.verticalLayout_2.addWidget(self.checkBoxPosition)
        self.checkBoxFSR = QtWidgets.QCheckBox(self.frame_2)
        self.checkBoxFSR.setChecked(True)
        self.checkBoxFSR.setObjectName("checkBoxFSR")
        self.verticalLayout_2.addWidget(self.checkBoxFSR)
        self.checkBoxVS = QtWidgets.QCheckBox(self.frame_2)
        self.checkBoxVS.setEnabled(False)
        self.checkBoxVS.setObjectName("checkBoxVS")
        self.verticalLayout_2.addWidget(self.checkBoxVS)
        self.pbSendReadVar = QtWidgets.QPushButton(self.frame_2)
        self.pbSendReadVar.setObjectName("pbSendReadVar")
        self.verticalLayout_2.addWidget(self.pbSendReadVar)
        self.frame_3 = QtWidgets.QFrame(self.tab_teste)
        self.frame_3.setGeometry(QtCore.QRect(210, 290, 221, 111))
        self.frame_3.setAutoFillBackground(True)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbReadFreq = QtWidgets.QLabel(self.frame_3)
        self.lbReadFreq.setAlignment(QtCore.Qt.AlignCenter)
        self.lbReadFreq.setObjectName("lbReadFreq")
        self.verticalLayout_3.addWidget(self.lbReadFreq)
        self.spinBoxFreq = QtWidgets.QSpinBox(self.frame_3)
        self.spinBoxFreq.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxFreq.setMinimum(1)
        self.spinBoxFreq.setMaximum(200)
        self.spinBoxFreq.setSingleStep(10)
        self.spinBoxFreq.setProperty("value", 10)
        self.spinBoxFreq.setObjectName("spinBoxFreq")
        self.verticalLayout_3.addWidget(self.spinBoxFreq)
        self.pbSendFreq = QtWidgets.QPushButton(self.frame_3)
        self.pbSendFreq.setObjectName("pbSendFreq")
        self.verticalLayout_3.addWidget(self.pbSendFreq)
        self.frame_4 = QtWidgets.QFrame(self.tab_teste)
        self.frame_4.setGeometry(QtCore.QRect(30, 290, 171, 171))
        self.frame_4.setAutoFillBackground(True)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.spinBoxSpeed = QtWidgets.QSpinBox(self.frame_4)
        self.spinBoxSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxSpeed.setMinimum(5)
        self.spinBoxSpeed.setMaximum(100)
        self.spinBoxSpeed.setSingleStep(5)
        self.spinBoxSpeed.setProperty("value", 60)
        self.spinBoxSpeed.setObjectName("spinBoxSpeed")
        self.verticalLayout_4.addWidget(self.spinBoxSpeed)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rbSpeedX = QtWidgets.QRadioButton(self.frame_5)
        self.rbSpeedX.setChecked(True)
        self.rbSpeedX.setObjectName("rbSpeedX")
        self.horizontalLayout.addWidget(self.rbSpeedX)
        self.rbSpeedZ = QtWidgets.QRadioButton(self.frame_5)
        self.rbSpeedZ.setObjectName("rbSpeedZ")
        self.horizontalLayout.addWidget(self.rbSpeedZ)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.pbSendSpeed = QtWidgets.QPushButton(self.frame_4)
        self.pbSendSpeed.setObjectName("pbSendSpeed")
        self.verticalLayout_4.addWidget(self.pbSendSpeed)
        self.frame_6 = QtWidgets.QFrame(self.tab_teste)
        self.frame_6.setGeometry(QtCore.QRect(440, 220, 231, 261))
        self.frame_6.setAutoFillBackground(True)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lbDataRead = QtWidgets.QLabel(self.frame_6)
        self.lbDataRead.setAlignment(QtCore.Qt.AlignCenter)
        self.lbDataRead.setObjectName("lbDataRead")
        self.verticalLayout_5.addWidget(self.lbDataRead)
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbPosX = QtWidgets.QLabel(self.frame_7)
        self.lbPosX.setObjectName("lbPosX")
        self.horizontalLayout_2.addWidget(self.lbPosX)
        self.lcdPositionX = QtWidgets.QLCDNumber(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lcdPositionX.setFont(font)
        self.lcdPositionX.setDigitCount(7)
        self.lcdPositionX.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdPositionX.setProperty("value", 0.0)
        self.lcdPositionX.setObjectName("lcdPositionX")
        self.horizontalLayout_2.addWidget(self.lcdPositionX)
        self.verticalLayout_5.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbPosZ = QtWidgets.QLabel(self.frame_8)
        self.lbPosZ.setObjectName("lbPosZ")
        self.horizontalLayout_3.addWidget(self.lbPosZ)
        self.lcdPositionZ = QtWidgets.QLCDNumber(self.frame_8)
        self.lcdPositionZ.setDigitCount(7)
        self.lcdPositionZ.setObjectName("lcdPositionZ")
        self.horizontalLayout_3.addWidget(self.lcdPositionZ)
        self.verticalLayout_5.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbFSR = QtWidgets.QLabel(self.frame_9)
        self.lbFSR.setObjectName("lbFSR")
        self.horizontalLayout_4.addWidget(self.lbFSR)
        self.lcdFSR = QtWidgets.QLCDNumber(self.frame_9)
        self.lcdFSR.setObjectName("lcdFSR")
        self.horizontalLayout_4.addWidget(self.lcdFSR)
        self.verticalLayout_5.addWidget(self.frame_9)
        self.lbEndZ = QtWidgets.QLabel(self.frame_6)
        self.lbEndZ.setAlignment(QtCore.Qt.AlignCenter)
        self.lbEndZ.setObjectName("lbEndZ")
        self.verticalLayout_5.addWidget(self.lbEndZ)
        self.lbEndX = QtWidgets.QLabel(self.frame_6)
        self.lbEndX.setAlignment(QtCore.Qt.AlignCenter)
        self.lbEndX.setObjectName("lbEndX")
        self.verticalLayout_5.addWidget(self.lbEndX)
        self.tabWidget.addTab(self.tab_teste, "")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(200, 30, 351, 28))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.lbSerialPort = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbSerialPort.setFont(font)
        self.lbSerialPort.setAlignment(QtCore.Qt.AlignCenter)
        self.lbSerialPort.setObjectName("lbSerialPort")
        self.comboBoxSerialPort = QtWidgets.QComboBox(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxSerialPort.setFont(font)
        self.comboBoxSerialPort.setObjectName("comboBoxSerialPort")
        self.pbConectarSerial = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pbConectarSerial.setFont(font)
        self.pbConectarSerial.setObjectName("pbConectarSerial")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "BIOLAB - Tactile Platform"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_coleta), _translate("Dialog", "Run 1"))
        self.pbHomeX.setText(_translate("Dialog", "Home X"))
        self.pbHomeZ.setText(_translate("Dialog", "Home Z"))
        self.lbMode.setText(_translate("Dialog", "Mode"))
        self.rbModeIdle.setText(_translate("Dialog", "Idle"))
        self.rbModeReadData.setText(_translate("Dialog", "Read Data"))
        self.pbSendMode.setText(_translate("Dialog", "Send"))
        self.lbEnableVar.setText(_translate("Dialog", "Enable Variables"))
        self.checkBoxMPU.setText(_translate("Dialog", "MPU"))
        self.checkBoxPosition.setText(_translate("Dialog", "Position"))
        self.checkBoxFSR.setText(_translate("Dialog", "FSR"))
        self.checkBoxVS.setText(_translate("Dialog", "Voltage Sensor"))
        self.pbSendReadVar.setText(_translate("Dialog", "Send"))
        self.lbReadFreq.setText(_translate("Dialog", "Read Frequency (Hz)"))
        self.pbSendFreq.setText(_translate("Dialog", "Send"))
        self.label_4.setText(_translate("Dialog", "Speed"))
        self.rbSpeedX.setText(_translate("Dialog", "X"))
        self.rbSpeedZ.setText(_translate("Dialog", "Z"))
        self.pbSendSpeed.setText(_translate("Dialog", "Send"))
        self.lbDataRead.setText(_translate("Dialog", "Data Read"))
        self.lbPosX.setText(_translate("Dialog", "Position X"))
        self.lbPosZ.setText(_translate("Dialog", "Position Z"))
        self.lbFSR.setText(_translate("Dialog", "FSR"))
        self.lbEndZ.setText(_translate("Dialog", "End Stop X"))
        self.lbEndX.setText(_translate("Dialog", "End Stop Z"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_teste), _translate("Dialog", "Test"))
        self.lbSerialPort.setText(_translate("Dialog", "Serial Port"))
        self.pbConectarSerial.setText(_translate("Dialog", "Connect"))

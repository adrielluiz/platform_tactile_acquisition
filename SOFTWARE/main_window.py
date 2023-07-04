# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 832)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(100, -1, 100, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_16 = QtWidgets.QFrame(self.centralwidget)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lbSerialPort = QtWidgets.QLabel(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbSerialPort.sizePolicy().hasHeightForWidth())
        self.lbSerialPort.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbSerialPort.setFont(font)
        self.lbSerialPort.setAlignment(QtCore.Qt.AlignCenter)
        self.lbSerialPort.setObjectName("lbSerialPort")
        self.horizontalLayout_11.addWidget(self.lbSerialPort)
        self.comboBoxSerialPort = QtWidgets.QComboBox(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSerialPort.sizePolicy().hasHeightForWidth())
        self.comboBoxSerialPort.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxSerialPort.setFont(font)
        self.comboBoxSerialPort.setObjectName("comboBoxSerialPort")
        self.horizontalLayout_11.addWidget(self.comboBoxSerialPort)
        self.pbConectarSerial = QtWidgets.QPushButton(self.frame_16)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pbConectarSerial.setFont(font)
        self.pbConectarSerial.setObjectName("pbConectarSerial")
        self.horizontalLayout_11.addWidget(self.pbConectarSerial)
        self.verticalLayout_7.addWidget(self.frame_16)
        self.frame_10 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.lineEditFileName = QtWidgets.QLineEdit(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditFileName.setFont(font)
        self.lineEditFileName.setObjectName("lineEditFileName")
        self.horizontalLayout_5.addWidget(self.lineEditFileName)
        self.pbUpdateFileName = QtWidgets.QPushButton(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbUpdateFileName.sizePolicy().hasHeightForWidth())
        self.pbUpdateFileName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pbUpdateFileName.setFont(font)
        self.pbUpdateFileName.setObjectName("pbUpdateFileName")
        self.horizontalLayout_5.addWidget(self.pbUpdateFileName)
        self.verticalLayout_7.addWidget(self.frame_10)
        self.pbSaveExcel = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pbSaveExcel.setFont(font)
        self.pbSaveExcel.setObjectName("pbSaveExcel")
        self.verticalLayout_7.addWidget(self.pbSaveExcel)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_coleta = QtWidgets.QWidget()
        self.tab_coleta.setObjectName("tab_coleta")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_coleta)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_24 = QtWidgets.QFrame(self.tab_coleta)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.frame_15 = QtWidgets.QFrame(self.frame_24)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setAutoFillBackground(True)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_11 = QtWidgets.QFrame(self.frame_15)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.sbXinit = QtWidgets.QSpinBox(self.frame_11)
        self.sbXinit.setAlignment(QtCore.Qt.AlignCenter)
        self.sbXinit.setMaximum(160000)
        self.sbXinit.setSingleStep(100)
        self.sbXinit.setProperty("value", 90000)
        self.sbXinit.setObjectName("sbXinit")
        self.horizontalLayout_6.addWidget(self.sbXinit)
        self.verticalLayout_6.addWidget(self.frame_11)
        self.frame_14 = QtWidgets.QFrame(self.frame_15)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        self.sbZinit = QtWidgets.QSpinBox(self.frame_14)
        self.sbZinit.setAlignment(QtCore.Qt.AlignCenter)
        self.sbZinit.setMaximum(36000)
        self.sbZinit.setSingleStep(100)
        self.sbZinit.setProperty("value", 20000)
        self.sbZinit.setObjectName("sbZinit")
        self.horizontalLayout_9.addWidget(self.sbZinit)
        self.verticalLayout_6.addWidget(self.frame_14)
        self.frame_13 = QtWidgets.QFrame(self.frame_15)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.sbFSR = QtWidgets.QSpinBox(self.frame_13)
        self.sbFSR.setAlignment(QtCore.Qt.AlignCenter)
        self.sbFSR.setMinimum(1)
        self.sbFSR.setMaximum(1023)
        self.sbFSR.setProperty("value", 800)
        self.sbFSR.setObjectName("sbFSR")
        self.horizontalLayout_8.addWidget(self.sbFSR)
        self.verticalLayout_6.addWidget(self.frame_13)
        self.frame_12 = QtWidgets.QFrame(self.frame_15)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.sbNumTests = QtWidgets.QSpinBox(self.frame_12)
        self.sbNumTests.setAlignment(QtCore.Qt.AlignCenter)
        self.sbNumTests.setMaximum(1000)
        self.sbNumTests.setSingleStep(1)
        self.sbNumTests.setProperty("value", 3)
        self.sbNumTests.setObjectName("sbNumTests")
        self.horizontalLayout_7.addWidget(self.sbNumTests)
        self.verticalLayout_6.addWidget(self.frame_12)
        self.horizontalLayout_19.addWidget(self.frame_15)
        self.frame_22 = QtWidgets.QFrame(self.frame_24)
        self.frame_22.setAutoFillBackground(True)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidgetRun1 = QtWidgets.QListWidget(self.frame_22)
        self.listWidgetRun1.setObjectName("listWidgetRun1")
        self.verticalLayout_2.addWidget(self.listWidgetRun1)
        self.frame_21 = QtWidgets.QFrame(self.frame_22)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_7 = QtWidgets.QLabel(self.frame_21)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_15.addWidget(self.label_7)
        self.progressBarRun1 = QtWidgets.QProgressBar(self.frame_21)
        self.progressBarRun1.setProperty("value", 0)
        self.progressBarRun1.setObjectName("progressBarRun1")
        self.horizontalLayout_15.addWidget(self.progressBarRun1)
        self.verticalLayout_2.addWidget(self.frame_21)
        self.horizontalLayout_19.addWidget(self.frame_22)
        self.verticalLayout_10.addWidget(self.frame_24)
        self.frame_23 = QtWidgets.QFrame(self.tab_coleta)
        self.frame_23.setAutoFillBackground(True)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.pbStartRun1 = QtWidgets.QPushButton(self.frame_23)
        self.pbStartRun1.setObjectName("pbStartRun1")
        self.horizontalLayout_16.addWidget(self.pbStartRun1)
        self.pbStopRun1 = QtWidgets.QPushButton(self.frame_23)
        self.pbStopRun1.setObjectName("pbStopRun1")
        self.horizontalLayout_16.addWidget(self.pbStopRun1)
        self.verticalLayout_10.addWidget(self.frame_23)
        self.tabWidget.addTab(self.tab_coleta, "")
        self.tab_teste = QtWidgets.QWidget()
        self.tab_teste.setObjectName("tab_teste")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_teste)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_19 = QtWidgets.QFrame(self.tab_teste)
        self.frame_19.setWhatsThis("")
        self.frame_19.setAutoFillBackground(True)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_17 = QtWidgets.QFrame(self.frame_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pbHomeX = QtWidgets.QPushButton(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbHomeX.sizePolicy().hasHeightForWidth())
        self.pbHomeX.setSizePolicy(sizePolicy)
        self.pbHomeX.setObjectName("pbHomeX")
        self.horizontalLayout_12.addWidget(self.pbHomeX)
        self.horizontalSliderX = QtWidgets.QSlider(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSliderX.sizePolicy().hasHeightForWidth())
        self.horizontalSliderX.setSizePolicy(sizePolicy)
        self.horizontalSliderX.setMaximum(160)
        self.horizontalSliderX.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderX.setObjectName("horizontalSliderX")
        self.horizontalLayout_12.addWidget(self.horizontalSliderX)
        self.verticalLayout_9.addWidget(self.frame_17)
        self.frame_18 = QtWidgets.QFrame(self.frame_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pbHomeZ = QtWidgets.QPushButton(self.frame_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbHomeZ.sizePolicy().hasHeightForWidth())
        self.pbHomeZ.setSizePolicy(sizePolicy)
        self.pbHomeZ.setObjectName("pbHomeZ")
        self.horizontalLayout_13.addWidget(self.pbHomeZ)
        self.verticalSliderZ = QtWidgets.QSlider(self.frame_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalSliderZ.sizePolicy().hasHeightForWidth())
        self.verticalSliderZ.setSizePolicy(sizePolicy)
        self.verticalSliderZ.setMaximum(35)
        self.verticalSliderZ.setOrientation(QtCore.Qt.Vertical)
        self.verticalSliderZ.setObjectName("verticalSliderZ")
        self.horizontalLayout_13.addWidget(self.verticalSliderZ)
        self.verticalLayout_9.addWidget(self.frame_18)
        self.gridLayout_2.addWidget(self.frame_19, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.tab_teste)
        self.frame_2.setAutoFillBackground(True)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lbEnableVar = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbEnableVar.sizePolicy().hasHeightForWidth())
        self.lbEnableVar.setSizePolicy(sizePolicy)
        self.lbEnableVar.setAlignment(QtCore.Qt.AlignCenter)
        self.lbEnableVar.setObjectName("lbEnableVar")
        self.gridLayout_3.addWidget(self.lbEnableVar, 0, 0, 1, 1)
        self.checkBoxMPU = QtWidgets.QCheckBox(self.frame_2)
        self.checkBoxMPU.setEnabled(False)
        self.checkBoxMPU.setObjectName("checkBoxMPU")
        self.gridLayout_3.addWidget(self.checkBoxMPU, 1, 0, 1, 1)
        self.checkBoxPosition = QtWidgets.QCheckBox(self.frame_2)
        self.checkBoxPosition.setChecked(True)
        self.checkBoxPosition.setObjectName("checkBoxPosition")
        self.gridLayout_3.addWidget(self.checkBoxPosition, 2, 0, 1, 1)
        self.checkBoxFSR = QtWidgets.QCheckBox(self.frame_2)
        self.checkBoxFSR.setChecked(True)
        self.checkBoxFSR.setObjectName("checkBoxFSR")
        self.gridLayout_3.addWidget(self.checkBoxFSR, 3, 0, 1, 1)
        self.checkBoxVS = QtWidgets.QCheckBox(self.frame_2)
        self.checkBoxVS.setEnabled(False)
        self.checkBoxVS.setObjectName("checkBoxVS")
        self.gridLayout_3.addWidget(self.checkBoxVS, 4, 0, 1, 1)
        self.pbSendReadVar = QtWidgets.QPushButton(self.frame_2)
        self.pbSendReadVar.setObjectName("pbSendReadVar")
        self.gridLayout_3.addWidget(self.pbSendReadVar, 5, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 1, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.tab_teste)
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
        self.lcdFSR.setDigitCount(7)
        self.lcdFSR.setObjectName("lcdFSR")
        self.horizontalLayout_4.addWidget(self.lcdFSR)
        self.verticalLayout_5.addWidget(self.frame_9)
        self.gridLayout_2.addWidget(self.frame_6, 0, 2, 2, 1)
        self.frame_4 = QtWidgets.QFrame(self.tab_teste)
        self.frame_4.setAutoFillBackground(True)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rbSpeedX = QtWidgets.QRadioButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbSpeedX.sizePolicy().hasHeightForWidth())
        self.rbSpeedX.setSizePolicy(sizePolicy)
        self.rbSpeedX.setChecked(True)
        self.rbSpeedX.setObjectName("rbSpeedX")
        self.horizontalLayout.addWidget(self.rbSpeedX)
        self.rbSpeedZ = QtWidgets.QRadioButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbSpeedZ.sizePolicy().hasHeightForWidth())
        self.rbSpeedZ.setSizePolicy(sizePolicy)
        self.rbSpeedZ.setStatusTip("")
        self.rbSpeedZ.setObjectName("rbSpeedZ")
        self.horizontalLayout.addWidget(self.rbSpeedZ)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.pbSendSpeed = QtWidgets.QPushButton(self.frame_4)
        self.pbSendSpeed.setObjectName("pbSendSpeed")
        self.verticalLayout_4.addWidget(self.pbSendSpeed)
        self.gridLayout_2.addWidget(self.frame_4, 1, 1, 2, 1)
        self.frame = QtWidgets.QFrame(self.tab_teste)
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
        self.frame_20 = QtWidgets.QFrame(self.frame)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.rbModeIdle = QtWidgets.QRadioButton(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbModeIdle.sizePolicy().hasHeightForWidth())
        self.rbModeIdle.setSizePolicy(sizePolicy)
        self.rbModeIdle.setChecked(True)
        self.rbModeIdle.setObjectName("rbModeIdle")
        self.horizontalLayout_14.addWidget(self.rbModeIdle)
        self.rbModeReadData = QtWidgets.QRadioButton(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbModeReadData.sizePolicy().hasHeightForWidth())
        self.rbModeReadData.setSizePolicy(sizePolicy)
        self.rbModeReadData.setStatusTip("")
        self.rbModeReadData.setObjectName("rbModeReadData")
        self.horizontalLayout_14.addWidget(self.rbModeReadData)
        self.verticalLayout.addWidget(self.frame_20)
        self.pbSendMode = QtWidgets.QPushButton(self.frame)
        self.pbSendMode.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pbSendMode.setObjectName("pbSendMode")
        self.verticalLayout.addWidget(self.pbSendMode)
        self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.tab_teste)
        self.frame_3.setAutoFillBackground(True)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbReadFreq = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbReadFreq.sizePolicy().hasHeightForWidth())
        self.lbReadFreq.setSizePolicy(sizePolicy)
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
        self.gridLayout_2.addWidget(self.frame_3, 2, 2, 1, 1)
        self.tabWidget.addTab(self.tab_teste, "")
        self.verticalLayout_8.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1060, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbSerialPort.setText(_translate("MainWindow", "Serial Port"))
        self.pbConectarSerial.setText(_translate("MainWindow", "Connect"))
        self.label.setText(_translate("MainWindow", "File Name"))
        self.lineEditFileName.setText(_translate("MainWindow", "./plataform_data.xlsx"))
        self.pbUpdateFileName.setText(_translate("MainWindow", "Update"))
        self.pbSaveExcel.setText(_translate("MainWindow", "Save Excel"))
        self.label_2.setText(_translate("MainWindow", "X initial position (um)"))
        self.label_3.setText(_translate("MainWindow", "Z initial position (um)"))
        self.label_5.setText(_translate("MainWindow", "FSR target                   "))
        self.label_6.setText(_translate("MainWindow", "Number of tests         "))
        self.label_7.setText(_translate("MainWindow", "Progress"))
        self.pbStartRun1.setText(_translate("MainWindow", "START"))
        self.pbStopRun1.setText(_translate("MainWindow", "STOP"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_coleta), _translate("MainWindow", "Run 1"))
        self.pbHomeX.setText(_translate("MainWindow", "Home X"))
        self.pbHomeZ.setText(_translate("MainWindow", "Home Z"))
        self.lbEnableVar.setText(_translate("MainWindow", "Enable Variables"))
        self.checkBoxMPU.setText(_translate("MainWindow", "MPU"))
        self.checkBoxPosition.setText(_translate("MainWindow", "Position"))
        self.checkBoxFSR.setText(_translate("MainWindow", "FSR"))
        self.checkBoxVS.setText(_translate("MainWindow", "Voltage Sensor"))
        self.pbSendReadVar.setText(_translate("MainWindow", "Send"))
        self.lbDataRead.setText(_translate("MainWindow", "Data Display "))
        self.lbPosX.setText(_translate("MainWindow", "Position X"))
        self.lbPosZ.setText(_translate("MainWindow", "Position Z"))
        self.lbFSR.setText(_translate("MainWindow", "FSR"))
        self.label_4.setText(_translate("MainWindow", "Speed"))
        self.rbSpeedX.setText(_translate("MainWindow", "X"))
        self.rbSpeedZ.setText(_translate("MainWindow", "Z"))
        self.pbSendSpeed.setText(_translate("MainWindow", "Send"))
        self.lbMode.setText(_translate("MainWindow", "Mode"))
        self.rbModeIdle.setText(_translate("MainWindow", "Idle"))
        self.rbModeReadData.setText(_translate("MainWindow", "Read Data", "4"))
        self.pbSendMode.setText(_translate("MainWindow", "Send"))
        self.lbReadFreq.setText(_translate("MainWindow", "Read Frequency (Hz)"))
        self.pbSendFreq.setText(_translate("MainWindow", "Send"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_teste), _translate("MainWindow", "Test"))

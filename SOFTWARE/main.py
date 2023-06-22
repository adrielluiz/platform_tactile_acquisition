from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from main_window import Ui_Dialog
import sys
from serial_port import SerialConn
from serial import *
import log
from threading import Event
from queue import Queue

class MainWin:
    def __init__(self):

        self.main_win = QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.main_win)        

        self.stop = Event()
        self.txq = Queue()
        self.rxq = Queue()
        self.serial_task = SerialConn()

        #self.ui.comboBoxSerialPort. activated[str].connect(self.update_com_ports)
        self.ui.pbConectarSerial.clicked.connect(self.conn_serial)
         
    def show(self):
        self.main_win.show()

    def update_com_ports(self):
        self.ui.comboBoxSerialPort.clear()
        ports = self.serial_task.get_ports_available()
        for port in ports:            
            self.ui.comboBoxSerialPort.addItem(port.device)

    def conn_serial(self):
        print(self.ui.comboBoxSerialPort.currentText())   
        
        try:
            self.serial = Serial(port=self.ui.comboBoxSerialPort.currentText(),timeout=1,baudrate=230400)
        except Exception as e:
            log.logging.error(str(e))
            sys.exit(1)         
        else:
            self.serial_task.set_init_parameters(self.serial,self.rxq, self.txq, self.stop)
            self.serial_task.start()
            self.ui.pbConectarSerial.setStyleSheet("background-color: lime")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWin()
    main_win.update_com_ports()
    main_win.show()
    sys.exit(app.exec_())

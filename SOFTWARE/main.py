from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from main_window import Ui_Dialog
import sys
from serial_port import SerialConn
from serial import *
import log
from threading import Event
from queue import Queue
from serial_cmd import SerialCmd
from threading import *
import time

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

        self.ui.pbSendMode.clicked.connect(self.send_mode)
        self.ui.pbSendFreq.clicked.connect(self.send_freq)
        self.ui.pbSendSpeed.clicked.connect(self.send_speed)
        self.ui.pbSendReadVar.clicked.connect(self.send_flags)
        self.ui.pbHomeX.clicked.connect(self.send_pos_home_x)
        self.ui.pbHomeZ.clicked.connect(self.send_pos_home_z)
        self.ui.horizontalSliderX.sliderReleased.connect(self.send_pos_x)
        self.ui.verticalSliderZ.sliderReleased.connect(self.send_pos_z)        
         
    def show(self):
        self.main_win.show()

    def update_com_ports(self):
        self.ui.comboBoxSerialPort.clear()
        ports = self.serial_task.get_ports_available()
        for port in ports:            
            self.ui.comboBoxSerialPort.addItem(port.device)

    def conn_serial(self):
        print(self.ui.comboBoxSerialPort.currentText())

        if not self.serial_task.is_connected:        
            try:
                self.serial = Serial(port=self.ui.comboBoxSerialPort.currentText(),timeout=1,baudrate=230400)
            except Exception as e:
                log.logging.error(str(e))
                sys.exit(1)         
            else:
                self.serial_task.set_init_parameters(self.serial,self.rxq, self.txq, self.stop)
                self.serial_task.start()
                self.ui.pbConectarSerial.setStyleSheet("background-color: lime")
                self.recv = Thread(target=self.recv_data)
                self.recv.start()
        else:
            log.logging.error("Serial already opened")

    def recv_data(self):
        while not self.stop.is_set():
            new_cmd = False
            try:
                cmd = self.rxq.get(True, 1)
            except Exception as e:
                time.sleep(0.5)
            else:
                new_cmd = True

            if new_cmd:
                self.check_cmd(cmd)

    def check_cmd(self,cmd):
        if 'command' not in cmd:
            return 

        if cmd['command'] == 'position':
            x = cmd['params']['x']
            z = cmd['params']['z']
            log.logging.debug('New position x: {} z: {}'.format(x, z))
            self.ui.lcdPositionX.display(x)
            self.ui.lcdPositionZ.display(z)
            
        elif cmd['command'] == 'fsr':
            fsr = cmd['params']['value']
            log.logging.debug('New fsr fsr: {}'.format(fsr))
            self.ui.lcdFSR.display(fsr)

    def send_mode(self):
        if self.serial_task.is_connected:
            if self.ui.rbModeIdle.isChecked():
                self.txq.put(SerialCmd().set_mode("idle"))
            elif self.ui.rbModeReadData.isChecked():
                self.txq.put(SerialCmd().set_mode("read"))  

    def send_speed(self):
        if self.serial_task.is_connected: 
            speed  = self.ui.spinBoxSpeed.value()
            if self.ui.rbSpeedX.isChecked():
                self.txq.put(SerialCmd().set_speed("x", speed))     
            elif self.ui.rbSpeedZ.isChecked():
                self.txq.put(SerialCmd().set_speed("z", speed))

    def send_freq(self):
        if self.serial_task.is_connected: 
            freq = self.ui.spinBoxFreq.value()
            self.txq.put(SerialCmd().set_freq(freq))
            pass

    def read_checkbox_int(self, value):
        if value == True:
            return 1
        else:
            return 0    

    def send_flags(self):
        if self.serial_task.is_connected: 
            pos = self.read_checkbox_int(self.ui.checkBoxPosition.isChecked())
            mpu = self.read_checkbox_int(self.ui.checkBoxMPU.isChecked())
            fsr = self.read_checkbox_int(self.ui.checkBoxFSR.isChecked())
            vs  = self.read_checkbox_int(self.ui.checkBoxVS.isChecked())
            self.txq.put(SerialCmd().set_flags_read(pos, mpu, fsr, vs))        

    def send_pos_home_x(self):   
        if self.serial_task.is_connected: 
            self.txq.put(SerialCmd().set_pos("x", "home"))     
            self.ui.horizontalSliderX.setValue(0)   
            self.ui.pbHomeX.setEnabled(False)  

    def send_pos_home_z(self):   
        if self.serial_task.is_connected: 
            self.txq.put(SerialCmd().set_pos("z", "home"))  
            self.ui.verticalSliderZ.setValue(0)
            self.ui.pbHomeZ.setEnabled(False)  

    def send_pos_x(self):
        if self.serial_task.is_connected: 
            pos_x = self.ui.horizontalSliderX.value() * 1000
            self.txq.put(SerialCmd().set_pos("x", pos_x))      

    def send_pos_z(self):
        if self.serial_task.is_connected: 
            pos_z = self.ui.verticalSliderZ.value() * 1000
            self.txq.put(SerialCmd().set_pos("z", pos_z))                    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWin()
    main_win.update_com_ports()
    main_win.show()
    sys.exit(app.exec_())

from PyQt5.QtWidgets import QApplication, QMainWindow, QApplication, QMessageBox, QListWidgetItem
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QColor
from main_window import Ui_MainWindow
import sys
from serial_port import SerialConn
from excel import Excel
from serial import *
import log
from threading import Event
from queue import Queue
from serial_cmd import SerialCmd
from threading import *
import time
from exp import RunExperiment

class MainWin(QMainWindow):
    work_requested = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)        

        self.stop = Event()
        self.txq = Queue()
        self.rxq = Queue()
        self.serial_task = SerialConn()

        self.ui.pbConectarSerial.clicked.connect(self.conn_serial)
        self.ui.pbSendMode.clicked.connect(self.send_mode)
        self.ui.pbSendFreq.clicked.connect(self.send_freq)
        self.ui.pbSendSpeed.clicked.connect(self.send_speed)
        self.ui.pbSendReadVar.clicked.connect(self.send_flags)
        self.ui.pbHomeX.clicked.connect(self.send_pos_home_x)
        self.ui.pbHomeZ.clicked.connect(self.send_pos_home_z)
        self.ui.pbSaveExcel.clicked.connect(self.save_excel)
        self.ui.pbStartRun1.clicked.connect(self.run_exp)
        self.ui.pbUpdateFileName.clicked.connect(self.update_file_name)
        self.ui.pbStopRun1.clicked.connect(self.run1_stop)

        self.ui.horizontalSliderX.sliderReleased.connect(self.send_pos_x)
        self.ui.verticalSliderZ.sliderReleased.connect(self.send_pos_z)    

        self.excel = Excel()           

        self.worker_thread = QThread()
        self.exp = RunExperiment(self.txq, 1)
        
        self.exp.progress_bar.connect(self.run1_update_progress)
        self.exp.msg_box.connect(self.run1_append_msg)
        self.work_requested.connect(self.exp.run)

        self.exp.moveToThread(self.worker_thread) 
       
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

                self.txq.put(SerialCmd().set_restart())
                time.sleep(1)
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
        
        tab = self.ui.tabWidget.tabText(self.ui.tabWidget.currentIndex())

        if cmd['command'] == 'position':
            x = cmd['params']['x']
            z = cmd['params']['z']
            log.logging.debug('New position x: {} z: {}'.format(x, z))

            if tab == "Test":
                self.ui.lcdPositionX.display(x)
                self.ui.lcdPositionZ.display(z)

            self.excel.append_pos_x(x)
            self.excel.append_pos_z(z)
            
        elif cmd['command'] == 'fsr':
            fsr = cmd['params']['value']
            log.logging.debug('New fsr: {}'.format(fsr))
            if tab == "Test":
                self.ui.lcdFSR.display(fsr)
            elif tab == "Run 1":    
                self.exp.set_fsr_read(fsr)
            
            self.excel.append_fsr(fsr)

        elif cmd['command'] == 'ok':
            if tab == "Run 1":
                self.exp.read_ok = True    

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

    def save_excel(self):
        self.excel.save_file()        
        self.show_info_messagebox()         
        sys.exit(1)   

    def show_info_messagebox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText( f"Excel file {self.excel.filename} saved!")        
        msg.setWindowTitle("Information")
        msg.exec_()        
  
    def update_file_name(self):
        self.excel.set_file_name(self.ui.lineEditFileName.text())

    def run_exp(self):
        if self.serial_task.is_connected:
            init_x  = self.ui.sbXinit.value()
            init_z  = self.ui.sbZinit.value()
            fsr  = self.ui.sbFSR.value()
            num  = self.ui.sbNumTests.value()

            self.exp.set_all_param(init_x, init_z, fsr, num)    
            self.worker_thread.start()
            self.work_requested.emit()

    def run1_update_progress(self, val):
        self.ui.progressBarRun1.setValue(val)

    def run1_append_msg(self, msg, type):
        item = QListWidgetItem(msg)
        
        if type == 'info':
            item.setForeground(QColor(Qt.darkGreen))
        elif type == 'error':
            item.setForeground(QColor(Qt.red))

        if 'Running New Test' in msg:
            item.setTextAlignment(Qt.AlignCenter)    
        
        self.ui.listWidgetRun1.addItem(item)

    def run1_stop(self):
        self.worker_thread.terminate()
        self.run1_append_msg("Run 1 stopped", "error")

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWin()
    main_win.update_com_ports()
    main_win.show()
    sys.exit(app.exec_())
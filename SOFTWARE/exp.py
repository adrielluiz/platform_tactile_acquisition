from serial_cmd import SerialCmd
from logging import log
import log
import time
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class RunExperiment(QObject):
    progress_bar = pyqtSignal(int)
    msg_box = pyqtSignal(str, str)

    def __init__(self, txq, main_obj):
        super().__init__()
        self.init_pos_x = 0
        self.init_pos_z = 0
        self.final_pos_z = 0
        self.num_test = 0
        self.fsr_read = 0
        self.pos_z_read = 0
        self.steps_z_um = 500
        self.main_obj = main_obj
        self.stop_test = False

        self.txq = txq
        self.read_ok = False

    def set_stop_test(self, v):
        self.stop_test = v
        
    def set_init_pos_x(self, init_pos_x):
        self.init_pos_x = init_pos_x    

    def set_init_pos_z(self, init_pos_z):
        self.init_pos_z = init_pos_z  

    def set_min_fsr(self, min_fsr):
        self.min_fsr = min_fsr  

    def set_num_test(self, num_test):
        self.num_test = num_test             

    def set_fsr_read(self, fsr):    
        self.fsr_read = fsr
        
    def set_pos_z_read(self, pos_z_read):
        self.pos_z_read = pos_z_read    

    def set_steps_z_um(self, steps_z_um):    
        self.steps_z_um = steps_z_um

    def set_all_param(self, init_pos_x, init_pos_z, final_pos_z, num_test):    
        self.init_pos_x = init_pos_x
        self.init_pos_z = init_pos_z
        self.final_pos_z = final_pos_z
        self.num_test = num_test

    def logging_info(self, msg):
        log.logging.info(msg)
        self.msg_box.emit(msg, 'info')

    def logging_error(self, msg):
        log.logging.error(msg)
        self.msg_box.emit(msg, 'error')

    def tx_wait_ok(self, data, timeout_seconds):
        self.txq.put(data)
        
        start_time = time.time()
            
        while self.read_ok == False:
            if time.time() - start_time >= timeout_seconds:
                self.logging_error('Timeout in cmd: {}'.format(data))
                return False
            time.sleep(0.01)  
    
        self.read_ok = False            

    @pyqtSlot()
    def run(self):
        self.logging_info("-------- Running New Test --------")
        self.logging_info(f'Init position X: {self.init_pos_x}')
        self.logging_info(f'Init position Z: {self.init_pos_z}')
        self.logging_info(f'Final position Z: {self.final_pos_z}')
        self.logging_info(f'Number of executions: {self.num_test}\n')

        self.txq.put(SerialCmd().set_restart())
        time.sleep(5)

        self.tx_wait_ok(SerialCmd().set_flags_read(1,0,0,0), 5)  
        self.tx_wait_ok(SerialCmd().set_mode("read"), 5)  

        self.tx_wait_ok(SerialCmd().set_speed("x", 300), 5)  
        self.tx_wait_ok(SerialCmd().set_speed("z", 300), 5)

        self.tx_wait_ok(SerialCmd().set_pos("x", "home"), 20)     
        self.tx_wait_ok(SerialCmd().set_pos("z", "home"), 20)       

        self.tx_wait_ok(SerialCmd().set_pos("x", self.init_pos_x), 20)
        self.tx_wait_ok(SerialCmd().set_pos("z", self.init_pos_z), 20) 
        
        num_exec = 0
        pos_z = self.init_pos_z + self.steps_z_um

        while num_exec < self.num_test:
            self.logging_info(f'Running experiment {num_exec + 1} of {self.num_test}')

            while self.pos_z_read < self.final_pos_z:
                self.logging_info(f'Setting position Z {pos_z}')
                self.logging_info(f'Z target {self.final_pos_z} actual {self.pos_z_read}\n')
                self.tx_wait_ok(SerialCmd().set_pos("z", pos_z), 5) 
                pos_z += self.steps_z_um
            
            num_exec += 1                     
            self.progress_bar.emit(int(num_exec/self.num_test * 100))  
            self.tx_wait_ok(SerialCmd().set_pos("z", self.init_pos_z), 5)
            pos_z = self.init_pos_z + self.steps_z_um    

        self.tx_wait_ok(SerialCmd().set_pos("x", 0), 20)
        self.tx_wait_ok(SerialCmd().set_pos("z", 0), 20)
        self.logging_info('Test Finished!')
        self.txq.put(SerialCmd().set_restart())
from serial_cmd import SerialCmd
from logging import log
import sys

from serial_port import SerialConn
from serial import *
import log
from threading import Event
from queue import Queue
from threading import *
import time

class RunExperiment():
    def __init__(self):
        self.init_pos_x = 0
        self.init_pos_z = 0
        self.min_fsr = 0
        self.num_test = 0
        self.fsr_read = 0
        self.steps_z_um = 500

        self.stop = Event()
        self.txq = Queue()
        self.rxq = Queue()
        self.serial_task = SerialConn()
        self.read_ok = False

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

    def set_steps_z_um(self, steps_z_um):    
        self.steps_z_um = steps_z_um

    def set_all_param(self, init_pos_x, init_pos_z, min_fsr, num_test):    
        self.init_pos_x = init_pos_x
        self.init_pos_z = init_pos_z
        self.min_fsr = min_fsr
        self.num_test = num_test

    def conn_serial(self, _port):
        if not self.serial_task.is_connected:        
            try:
                self.serial = Serial(_port,timeout=1,baudrate=230400)
            except Exception as e:
                log.logging.error(str(e))
                sys.exit(1)         
            else:
                self.serial_task.set_init_parameters(self.serial,self.rxq, self.txq, self.stop)
                self.serial_task.start()
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
                        
        elif cmd['command'] == 'fsr':
            fsr = cmd['params']['value']
            log.logging.debug('New fsr: {}'.format(fsr))
            self.set_fsr_read(fsr)

        elif cmd['command'] == 'ok':
            self.read_ok = True

    def tx_wait_ok(self, data, timeout_seconds):
        self.txq.put(data)
        
        start_time = time.time()
            
        while self.read_ok == False:
            if time.time() - start_time >= timeout_seconds:
                log.logging.error('Timeout in cmd: {}'.format(data))
                return False
            time.sleep(0.01)  
    
        self.read_ok = False            

    def run(self):
        log.logging.info("Running New Test")
        log.logging.info(f'Init position X: {self.init_pos_x}')
        log.logging.info(f'Init position z: {self.init_pos_z}')
        log.logging.info(f'Minimum FSR : {self.min_fsr}')
        log.logging.info(f'Number of executions: {self.num_test}')

        self.txq.put(SerialCmd().set_restart())
        time.sleep(5)

        self.tx_wait_ok(SerialCmd().set_flags_read(1,0,1,1), 5)  
        self.tx_wait_ok(SerialCmd().set_mode("read"), 5)  

        self.tx_wait_ok(SerialCmd().set_speed("x", 70), 5)  
        self.tx_wait_ok(SerialCmd().set_speed("z", 65), 5)

        self.tx_wait_ok(SerialCmd().set_pos("x", "home"), 20)     
        self.tx_wait_ok(SerialCmd().set_pos("z", "home"), 20)       

        self.tx_wait_ok(SerialCmd().set_pos("x", self.init_pos_x), 20)
        self.tx_wait_ok(SerialCmd().set_pos("z", self.init_pos_z), 20) 
        num_exec = 0
        pos_z = self.init_pos_z + self.steps_z_um

        while num_exec < self.num_test:
            log.logging.info(f'Running experiment {num_exec + 1} of {self.num_test}')

            while self.fsr_read >= self.min_fsr:
                log.logging.info(f'Setting position Z {pos_z}')
                log.logging.info(f'FSR target {self.min_fsr} actual {self.fsr_read}\n')
                self.tx_wait_ok(SerialCmd().set_pos("z", pos_z), 5) 
                pos_z += self.steps_z_um
            
            num_exec += 1                       
            self.tx_wait_ok(SerialCmd().set_pos("z", self.init_pos_z), 5)
            pos_z = self.init_pos_z + self.steps_z_um    

        self.tx_wait_ok(SerialCmd().set_pos("x", 0), 20)
        self.tx_wait_ok(SerialCmd().set_pos("z", 0), 20)
        log.logging.info('Test Finished!')
        self.txq.put(SerialCmd().set_restart())

exp = RunExperiment()
exp.set_all_param(90000, 20000, 800, 3)
exp.conn_serial('COM32')
exp.run()
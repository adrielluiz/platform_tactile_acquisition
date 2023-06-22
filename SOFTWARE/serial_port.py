import serial.tools.list_ports
import log
from threading import Event, Thread, Lock
import time

class SerialRx(Thread):
    def __init__(self, serial, rxq, stop):

        Thread.__init__(self)
        self.rxq = rxq
        self.serial = serial
        self.stop = stop

    def run(self):

        log.logging.debug('Serial RX started')

        while not self.stop.is_set():
            try:
                cmdline = self.serial.readline()
            except Exception as e:
                log.logging.error(repr(e))
                time.sleep(0.5)
                continue

            if not cmdline:
                time.sleep(0.25)
                continue

            log.logging.debug('RX: %s' % (cmdline))
            
            if cmdline[-1] == 10: # Termina com char null          
               pass
           
        log.logging.debug('Serial Rx stopped')

class SerialConn(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.is_connected = False

    def set_init_parameters(self, serial, rxq, txq, stop):
        Thread.__init__(self)
        self.txq = txq
        self.rxq = rxq
        self.stop = stop
        self.ser = serial
        self.rx_task = SerialRx(self.ser, self.rxq, self.stop)            
        self.rx_task.start()
        self.is_connected = True

    def close_serial(self):
        self.rx_task.stop
        self.ser.close()    
        log.logging.debug("Serial port closed")

    def get_ports_available(self):
        ports = serial.tools.list_ports.comports()

        if len(ports) == 0:
            log.logging.warning("Nenhuma porta COM encontrada.")
        else:
            log.logging.info("Portas COM disponíveis:")
            for port in ports:
                log.logging.info(port.device)

        return ports

    def tx_buf(self, buf):
        n = 0
        while True:
            try:
                n += self.ser.write(buf[n:])
            except Exception as e:
                log.logging.debug(repr(e))
                raise Exception('Serial TX error')

            if n >= len(buf):
                break

        return n    

    def run(self):
        
        log.logging.debug('Serial TX started')

        while not self.stop.is_set():
            try:
                cmdline = self.txq.get(True, 1)
            except Exception as e:
                continue

            log.logging.debug('TX: %s' % (cmdline))

            self.tx_buf(cmdline)

        self.ser.close()
        log.logging.debug('Serial TX stopped')
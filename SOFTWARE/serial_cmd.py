import log

class SerialCmd():
    def __str2int(self,s):
        try:
            v = int(s)
        except Exception as e:
            log.logging.error(repr(e))
            v = None
        return v
    
    def __str2float(self,s):
        try:
            v = float(s)
        except Exception as e:
            log.logging.error(repr(e))
            v = None
        return v

    def decode(self,cmdline):
        try:
            argv = cmdline.decode('ascii').strip()
            argv = argv.split()
        except Exception as e:
            log.logging.error(repr(e))
            return {}
                
        if not argv:
            return {}
        
        cmd = argv[0]
        params = argv[1:]
        argc = len(params)
        

        if cmd == 'position' and argc == 3:
            x = self.__str2int(params[0])
            z = self.__str2int(params[1])
            ts = self.__str2int(params[2])

            if x == None or z == None:
                return {}
            else:
                return {'command':'position', 'params':{'x':x, 'z':z, 'ts': ts}}
        elif cmd == 'fsr' and argc == 1:    
            v = self.__str2int(params[0])
            if v == None:
                return {}
            else:
                return {'command':'fsr', 'params':{'value':v}}
        elif cmd == 'ok':    
            return {'command':'ok'}    
        elif cmd == '777'and argc == 3:
            return {'command':'mb', 'ts': self.__str2int(params[0]), 'load_cell': self.__str2float(params[1]), 'resistive_sensor': self.__str2int(params[2])}
        return {}

    def __set_encode(self,k,v):
            s = 'set %s %s\n' % (k,v)
            return s.encode('ascii')
    
    def __set_encode2(self,k,v1, v2):
            s = 'set %s %s %s\n' % (k,v1,v2)
            return s.encode('ascii')

    def set_mode(self, mode):
        if mode == "idle":
            return self.__set_encode('mode', 'idle')
        elif mode == "read":
            return self.__set_encode('mode', 'read')

    def set_speed(self, axis, speed):
        if axis == "x":
            return self.__set_encode2('speed', '1', speed)
        elif axis == "z":
            return self.__set_encode2('speed', '2', speed)    
        
    def set_freq(self, delay):
        return self.__set_encode('read_freq', delay)      

    def set_flags_read(self, position, mpu, fsr, vs):
        s = 'set flags %s %s %s %s\n' % (position, mpu, fsr, vs)
        return s.encode('ascii')

    def set_restart(self):
        s = 'restart\n'
        return s.encode('ascii')    
    
    def set_pos(self, motor, pos):
        if motor == "x":
            return self.__set_encode2('position', '1', pos)
        elif motor == "z":
            return self.__set_encode2('position', '2', pos)    

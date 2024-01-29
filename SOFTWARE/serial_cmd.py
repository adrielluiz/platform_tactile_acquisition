import log

class SerialCmd():
    def __str2int(self,s):
        try:
            v = int(s)
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
        elif cmd == 'meas'and argc == 16:
            return {'command':'meas', 'ts': self.__str2int(params[0]),
                    'params':{'x11':self.__str2int(params[1]), 'x12':self.__str2int(params[2]), 'x13':self.__str2int(params[3]), 'x14':self.__str2int(params[4]), 'x15':self.__str2int(params[5]),
                              'x21':self.__str2int(params[6]), 'x22':self.__str2int(params[7]), 'x23':self.__str2int(params[8]), 'x24':self.__str2int(params[9]), 'x25':self.__str2int(params[10]),
                              'x31':self.__str2int(params[11]), 'x32':self.__str2int(params[12]), 'x33':self.__str2int(params[13]), 'x34':self.__str2int(params[14]), 'x35':self.__str2int(params[15])}}
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

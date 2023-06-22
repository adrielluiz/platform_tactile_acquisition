import log

class SerialCmd():
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
            return self.__set_encode2('mode',  '2', speed)    

CHSET = 'qwertyuiopasdf1029384756ghjklzxcvbnmMZNXBCVLAKSJDHFGPQOWIEURYT'

    
class Encoder(object):
    """Permutation example. Key can be used for cryptographic tests."""

    def __init__(self, cs=CHSET):
        self.key = [ord(x) for x in cs]
        
    def __pre_enc(self, m):
        return [ord(x) - 97 for x in m]
        
    def __pre_dec(self, c):
        return [self.key.index(ord(x)) for x in c]
        
    def enc(self, m):
        """Encoding function."""
        
        num = self.__pre_enc(m)
        c = "".join([chr(self.key[x]) for x in num])
        return c
    
    def dec(self, c):
        """Decoding function."""
        
        num = self.__pre_dec(c)
        m = "".join([chr(x + 97) for x in num])
        return m
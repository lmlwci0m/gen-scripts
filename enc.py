
CHSET = 'qwertyuiopasdf1029384756ghjklzxcvbnmMZNXBCVLAKSJDHFGPQOWIEURYT'


def tocharcode(cs):
    """Util for conversion of a string to character code."""
    return [ord(x) for x in cs]
    

class Encoder(object):

    def function_closure(self, function_list, origin):
        destination = origin
        for index, func in enumerate(function_list):
            destination = func(destination)
        return destination
        

    def __init__(self, cs=CHSET):
        """The character set is the seed for the key."""
        
        self.key = tocharcode(cs)
        
        self.enc_steps = [
            ord,
            lambda x: x - 97,
            lambda x: self.key[x],
            chr,
        ]
        self.dec_steps = [
            ord,
            self.key.index,
            lambda x: x + 97,
            chr,
        ]
        
    def enc(self, m):
    
        closure = self.function_closure
        seq = self.enc_steps
    
        return "".join([closure(seq, x) for x in m])
        
    def dec(self, c):
        
        closure = self.function_closure
        seq = self.dec_steps
    
        return "".join([closure(seq, x) for x in c])
        
    def basic_reverse(self, message):
        """Revert a message string."""
    
        #i = len(message) - 1
        tr = ""
        #while i >= 0:
        #    tr += message[i]
        #    i -= 1
        for c in message:
            tr = c + tr
        return tr
    

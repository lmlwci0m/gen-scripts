from functools import reduce
from functools import partial
CHSET = 'qwertyuiopasdf1029384756ghjklzxcvbnmMZNXBCVLAKSJDHFGPQOWIEURYT'


def tocharcode(cs):
    """Util for conversion of a string to character code."""
    return [ord(x) for x in cs]
    
    
def caesar_enc(key):
    return {True: lambda x: x + key, False: lambda x: x - key}
    
    
def define_function_closure(idiom=0):
    """Function generator for """
    
    if idiom == 1:
    
        def function_closure(self, function_list, origin):
            destination = origin
            for index, func in enumerate(function_list):
                destination = func(destination)
        
            return destination
        
        return function_closure
    
    elif idiom == 2:
    
        def function_closure(self, function_list, origin):
            destination = reduce(lambda x, y: y(x), function_list, origin)
            return destination
            
        return function_closure
            
    else:
    
        function_closure = partial(reduce, lambda x, y: y(x))
        
        return function_closure


class Encoder(object):

    def __init__(self, cs=CHSET):
        """The character set is the seed for the key.
        
        x      x
        ord    chr
        -97    +97
        key    key.index
        chr    ord
        y      y
        
        """
        
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
        
        self.closure = define_function_closure()
        
    def enc(self, m):
    
        closure, seq = self.closure, self.enc_steps
    
        return "".join([closure(seq, x) for x in m])
        
    def dec(self, c):
        
        closure, seq = self.closure, self.dec_steps
    
        return "".join([closure(seq, x) for x in c])
        
    def basic_reverse(self, message):
        """Revert a message string."""
    
        tr = ""
    
        for c in message:
            tr = c + tr
        return tr
        
    def caesar(self, message="Secret message", key=13, encrypt=True,
               letters='\|!"£$%&/()=?^\'ì,.-;:_ABCDEFGHIJKLMNOPQRSTUVWXYZ' +
               'abcdefghijklmnopqrstuvwxyz0123456789'):
               
        #message = message.upper()
        
        enc_func = caesar_enc(key)
        
        translated = ''
        
        for symbol in message:
        
            if symbol in letters:
                
                num = letters.find(symbol)
                
                num = enc_func[encrypt](num) % len(letters)
                    
                translated = translated + letters[num]
                
            else:
            
                translated = translated + symbol
                
        return translated
        
    

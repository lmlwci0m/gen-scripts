from functools import reduce
from functools import partial
CHSET = 'qwertyuiopasdf1029384756ghjklzxcvbnmMZNXBCVLAKSJDHFGPQOWIEURYT'

DEF_LETTERS = '\|!"£$%&/()=?^\'ì,.-;:_ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
               'abcdefghijklmnopqrstuvwxyz0123456789'

def tocharcode(cs):
    """Util for conversion of a string to character code."""
    return [ord(x) for x in cs]
    
    
def caesar_enc(key):
    return {True: lambda x: x + key, False: lambda x: x - key}
    
    
def define_function_composition(idiom=0):
    """Function generator for """
    
    if idiom == 1:
    
        def function_composition(self, function_list, origin):
            destination = origin
            for index, func in enumerate(function_list):
                destination = func(destination)
        
            return destination
        
        return function_composition
    
    elif idiom == 2:
    
        def function_composition(self, function_list, origin):
            destination = reduce(lambda x, y: y(x), function_list, origin)
            return destination
            
        return function_composition
            
    else:
    
        function_composition = partial(reduce, lambda x, y: y(x))
        
        return function_composition


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
        
        self.enc_steps = (
            ord,
            lambda x: x - 97,
            lambda x: self.key[x],
            chr,
        )
        self.dec_steps = (
            ord,
            self.key.index,
            lambda x: x + 97,
            chr,
        )
        
        self.transform = define_function_composition()
        
    def enc(self, m):
    
        transform, seq = self.transform, self.enc_steps
    
        return "".join([transform(seq, x) for x in m])
        
    def dec(self, c):
        
        transform, seq = self.transform, self.dec_steps
    
        return "".join([transform(seq, x) for x in c])
        
    def basic_reverse(self, message):
        """Revert a message string."""
    
        tr = ""
    
        for c in message:
            tr = c + tr
        return tr
        
    def caesar(self, message="Secret message", key=13, encrypt=True,
               letters=DEF_LETTERS):
               
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
        
    
def brute_force(ciphertext):
    """Caesar cipher cryptanalysis by brute force."""

    e = Encoder()
    for key in range(len(DEF_LETTERS)):
        print("{} {}".format(key, e.caesar(ciphertext, key, False)))
        
        
def transposition_decryption_algo(idiom=0):
    
    if idiom == 1:
        def algo(c, key):
            m = []
            i = 0
            ik = 0
            inc = 0
            for x in c:
                if len(m) == i:
                    m.append('')
                m[i] += x
                #print(m)
                i += 1
                ik += key
                if ik >= len(c):
                    i = 0
                    inc += 1
                    ik = inc
                    
            return "".join(m)
            
        return algo
            
    elif idiom == 2:
    
        def algo(c, key):
            m = [None] * len(c)
            i, l = 0, 0
            for x in c:
                m[i + key * l] = x
                l += 1
                if i + key * l >= len(c):
                    l = 0
                    i += 1
                
            return "".join(m)
            
        return algo
        
    else:
    
        def algo(c, key):
            
            m = [''] * len(c)
            i = 0
            inc = 0
            for x in c:
                m[i] = x
                i += key
                if i >= len(c):
                    inc += 1
                    i = inc
                    
            return "".join(m)
            
        return algo
        

class Transcipher(object):

    def __init__(self):
    
        self.__decalgo = transposition_decryption_algo()
        
    def decrypt(self, c, key):
    
        return self.__decalgo(c, key)
        
    def encrypt(self, m, key):
    
        e = [''] * key
        
        for i in range(key):
        
            col = i
            
            while col < len(m):
                e[i] += m[col]
                col += key
                
        #for x in e: print(x)
                
        return "".join(e)
        
        


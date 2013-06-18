from algoutils import tocharcode, caesar_enc
from algoutils import define_function_composition, transposition_decryption_algo

CHSET = 'qwertyuiopasdf1029384756ghjklzxcvbnmMZNXBCVLAKSJDHFGPQOWIEURYT'

DEF_LETTERS = '\|!"£$%&/()=?^\'ì,.-;:_ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
               'abcdefghijklmnopqrstuvwxyz0123456789'

    
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

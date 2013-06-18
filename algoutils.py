from functools import reduce
from functools import partial


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
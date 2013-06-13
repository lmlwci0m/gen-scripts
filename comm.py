#! /usr/bin/env python

import sys
from enc import Encoder
    

if __name__ == '__main__':
    
    if len(sys.argv) == 1:
        print("comm: No arguments are defined")
    
    else:
    
        m = sys.argv[1]
        
        e = Encoder()
    
        print("String is: {0:s}".format(m))
        
        c = e.enc(m)
        
        print("Encrypted is: {0:s}".format(c))
        
        m = e.dec(c)
        
        print("Decrypted is: {0:s}".format(m))
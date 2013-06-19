#! /usr/bin/env python3

import sys
from enc import Encoder
from enc import brute_force
from enc import Transcipher

if __name__ == '__main__':
    
    if len(sys.argv) == 1:
        print("comm: No arguments are defined")
    
    else:
    
        m = sys.argv[1]
        
        e = Encoder()
        
        #print("String is: {0:s}".format(m))
        c = e.enc(m)
        #print("Encrypted is: {0:s}".format(c))
        m = e.dec(c)
        #print("Decrypted is: {0:s}".format(m))
        
        #message = """
        #Lorem Ipsum è un testo segnaposto utilizzato nel settore della tipografia 
        #e della stampa. Lorem Ipsum è considerato il testo segnaposto standard sin 
        #dal sedicesimo secolo, quando un anonimo tipografo prese una cassetta di 
        #caratteri e li assemblò per preparare un testo campione. È sopravvissuto 
        #non solo a più di cinque secoli, ma anche al passaggio alla videoimpaginazione, 
        #pervenendoci sostanzialmente inalterato. Fu reso popolare, negli anni ’60, 
        #con la diffusione dei fogli di caratteri trasferibili “Letraset”, 
        #che contenevano passaggi del Lorem Ipsum, e più recentemente da software 
        #di impaginazione come Aldus PageMaker, che includeva versioni del Lorem Ipsum.
        #"""
        c = e.basic_reverse(m)
        m = e.basic_reverse(c)   
        #print(m)
        
        c = e.caesar(m)
        #brute_force(c)
        m = e.caesar(c, encrypt=False)  
        #print(m)
        
        e = Transcipher(3)
        
        #c = Transcipher().encrypt("Common sense is not so common.", 8)
        c = e.encrypt(m, 8)
        m = e.decrypt(c, 8)
        print(m)
        
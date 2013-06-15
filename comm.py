#! /usr/bin/env python3

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
        
        message = """
        Lorem Ipsum è un testo segnaposto utilizzato nel settore della tipografia 
        e della stampa. Lorem Ipsum è considerato il testo segnaposto standard sin 
        dal sedicesimo secolo, quando un anonimo tipografo prese una cassetta di 
        caratteri e li assemblò per preparare un testo campione. È sopravvissuto 
        non solo a più di cinque secoli, ma anche al passaggio alla videoimpaginazione, 
        pervenendoci sostanzialmente inalterato. Fu reso popolare, negli anni ’60, 
        con la diffusione dei fogli di caratteri trasferibili “Letraset”, 
        che contenevano passaggi del Lorem Ipsum, e più recentemente da software 
        di impaginazione come Aldus PageMaker, che includeva versioni del Lorem Ipsum.
        """
        
       
        tr = e.basic_reverse(message)
     
        back = e.basic_reverse(tr)
            
        print(back)
        
        tr = e.caesar(message)
     
        back1 = e.caesar(tr, encrypt=False)
            
        print(back1)
        
        print(back == back1)
        
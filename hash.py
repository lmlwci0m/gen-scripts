#! /usr/bin/env python3

import hashlib

def hash(message):
    m = hashlib.sha512()
    m.update(bytes("".join(message), "utf-8"))
    return m.hexdigest()

def ahead(message, index, chars, selectedchar, messagelen):
    message.append(selectedchar)
    
    index +=1
    #print(index, messagelen)
    if index == messagelen:
        print("".join(message))
        
    else:
        for char in chars:
            ahead(message, index, chars, char, messagelen)
            
    message.pop()

if __name__ == '__main__':

    basechars = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

    maxlen = 16

    for x in range(1, maxlen+1):
        message = []
        
        for char in basechars:
            #print(x)
            ahead(message, 0, basechars, char, x)
        
        

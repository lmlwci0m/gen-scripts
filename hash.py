#! /usr/bin/env python3

import hashlib

def hash(message):
    m = hashlib.sha512()
    m.update(bytes("".join(message), "utf-8"))
    return m.hexdigest()

def ahead(message, index, chars, selectedchar, messagelen, file):

    message.append(selectedchar)
    
    index +=1
    
    if index == messagelen:
        print("".join(message) + " " + hash(message), file=file)
        
        
    else:
        for char in chars:
            ahead(message, index, chars, char, messagelen, file)
            
    message.pop()

if __name__ == '__main__':

    basechars = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

    maxlen = 16

    with open("output.txt", "a") as file:

        for x in range(1, maxlen+1):
            message = []
            for char in basechars:
                ahead(message, 0, basechars, char, x, file)
        
        

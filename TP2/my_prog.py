#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 19:04:50 2019

@author: makhatchabdulvagabov
"""

#ASCII A:65 - Z:90, a:97 - z:122

def coding(message, key, isCoding):
    """code the giving message with the giving key.
    If the bollean isCoding is true we code the message. Otherwise we decode it.
    return the new message (coded or decoded)"""

    liste = list(message)
    if(isCoding == True):
        for k in range(len(liste)):
            if (ord(liste[k]) >= ord('A') and ord(liste[k]) <= ord('Z') - key) or \
               (ord(liste[k]) >= ord('a') and ord(liste[k]) <= ord('z') - key ):
                liste[k] = chr(ord(liste[k]) + key)
                
                
            elif (ord(liste[k]) >= ord('Z') - key + 1 and ord(liste[k]) <= ord('Z')) or \
               (ord(liste[k]) >= ord('z') - key + 1 and ord(liste[k]) <= ord('z') ):
                liste[k] = chr(ord(liste[k]) - (26 - key))

                
    if(isCoding == False):
        for k in range(len(liste)):
            if (ord(liste[k]) >= ord('A') + key and ord(liste[k]) <= ord('Z')) or \
               (ord(liste[k]) >= ord('a') + key and ord(liste[k]) <= ord('z')):
                liste[k] = chr(ord(liste[k]) - key)
                
            elif (ord(liste[k]) <= ord('A') + key - 1 and ord(liste[k]) <= ord('Z') + key) or \
               (ord(liste[k]) <= ord('a') + key - 1 and ord(liste[k]) <= ord('z') + key):
                liste[k] = chr(ord(liste[k]) + (26 - key))
                
    message = ''.join(liste)
    return message
    #print(message)


def interface():
    """
    asks the user to give a message, a key and isCoding (True for coding, False for decoding)
    """
    name = input("Give a file name ")
    key = int(input("Give a key "))
    isCoding = (input("isCoding True ot False ? ") == "True")
    file_A = open(name, "r")
    file_B = open("texte_code.txt","a")
    message = file_A.read()
    file_A.close()
    message = coding(message, key, isCoding)
    file_B.write(message)
    file_B.write('\n\n\n\n\n')
    file_B.close()
    


#calls directly interface() fucntion when you run python my_prog.py
if __name__ == '__main__':
    interface()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 17:06:11 2019

@author: makhatchabdulvagabov
"""

#Exercice 2
#2.
a = 'salut'
b = 102.912
c = 10.318
print(a , "l'ami:",int(round(b,0)),"et",round(c,2)) 

#3.
import string
chaine = string.ascii_lowercase
print (chaine)
print(chaine[3:3])
print(chaine[-6:-3])
print(chaine[-5:-2])
print(chaine[3::2])
print(chaine[-3:0:-3])

#4.
def squared(chaine):
    liste = chaine.split(";")
    liste = ''.join(liste)
    liste = liste.split()
    liste = [int(i) for i in liste]
    liste = [i**2 for i in liste]
    liste = [str(i) for i in liste]
    res = ' :'.join(liste)
    return (res)

print(squared('2 ;1 ;3'))
print(squared('2 ; 5 ;6 ;'))
print(squared('; 12 ; -23 ;\t60 ; 1 \t'))
print(squared('; -12 ; ; -23 ; 1 ; ;\t'))

#5.
s1 = ' elle est pleine de vide '
liste = s1.split()
s2 = ' '.join(liste)
print(s2)

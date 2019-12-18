#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 18:35:10 2019

@author: makhatchabdulvagabov
"""

#Exercice 3
#1.
l = list(range(4))
print(l[3], l[3:4], l[3:3])

#2.a
print('Modification of the list during the loop:')
l = [3,4,2,1]
for item in l:
    print('item {} in list {}'.format(item,l))
    if item > 2:
        l.remove(item)



print('Wihtout modification of the list during the loop:')
l = [3,4,2,1]
k = 0
l2 = l.copy()
while k < len(l):
    print('item {} in list {}'.format(l[k],l2))
    if l[k] > 2:
        l2.remove(l[k])
    k += 1
    
print(80*'*')
#2.b
l = [3,4,2,1]
for item in l:
    #print(item)
    #print("l[0] = ",l[0])
    del l[0]
print(l)


l = [3,4,2,1]
for k in range(len(l)):
    del l[0]
print(l)
#!/bin/python3

r = 1

def SET(s, ind):
    s[ind] = 1

def CLEAR(s, ind):
    s[ind] = 0

def OR(i, j, s):
    s[i] = i | j

def AND(i, j, s):
    s[i] = i & j

while r:
    r = int(input)
    bin_seq = '?'*32
    for i in range(r):

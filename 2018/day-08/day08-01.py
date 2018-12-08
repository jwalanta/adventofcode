#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/8
#

from collections import defaultdict

f = open("day08-input.txt")
num = map(int, f.read().split())

c=0
total=0
def traverse():
    global c
    global total

    nc = num[c]
    nm = num[c+1]

    c=c+2

    for i in range(nc):
        traverse()
    
    for i in range(nm):
        total = total + num[c]
        c=c+1

traverse()

print total
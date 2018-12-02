#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/2
#

f = open("day02-input.txt")
lines = f.read().split()

for x in range(len(lines)):
    for y in range(x+1, len(lines)):
        s1 = lines[x]
        s2 = lines[y]
        
        # check how many are different
        d = 0
        common = ""
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                d = d + 1
            else:
                common = common + s1[i]
        
        # if only one char different, print the common part
        if d == 1:
            print common

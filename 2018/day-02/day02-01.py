#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/2
#

f = open("day02-input.txt")
lines = f.read().split()

def twothree(str):
    two = 0
    three = 0
    for s in str:
        if str.count(s) == 2:
            two = 1
        if str.count(s) == 3:
            three = 1

    return (two, three)


twos = 0
threes = 0
for line in lines:
    a, b = twothree(list(line))
    twos, threes = twos+a, threes +b

print twos*threes



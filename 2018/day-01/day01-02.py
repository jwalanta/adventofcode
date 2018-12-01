#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/1
#

f = open("day01-01.input.txt")
deltas = map(int, f.read().split())

#deltas = [+3, +3, +4, -2, -4]
#deltas = [-6, +3, +8, +5, -6]
#deltas = [+7, +7, -2, -7, -4]

freq = 0
frequencies = [0]
p = 0

print "Please wait, this will take a while.."

while True:

    delta = deltas[p]

    # increment pointer or reset at 0
    p = p+1
    if p == len(deltas):
        p=0

    # new frequency
    freq = freq + delta

    # stop if frequency exists
    if freq in frequencies:
        print freq
        break
    
    frequencies.append(freq)


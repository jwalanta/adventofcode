#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/5
#

f = open("day05-input.txt")
polymer = f.read()

while True:

    replaced = False
    for c in range(ord('a'), ord('z')+1):
        unit = chr(c) + chr(c-32)

        if unit in polymer or unit[::-1] in polymer:
            replaced = True
            polymer = polymer.replace(unit, "").replace(unit[::-1],"")

    if replaced == False:
        break

print len(polymer)

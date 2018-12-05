#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/5
#

f = open("day05-input.txt")
polymer = f.read()

def reduce(polymer):
    while True:
        replaced = False
        for c in range(ord('a'), ord('z')+1):
            unit = chr(c) + chr(c-32)

            if unit in polymer or unit[::-1] in polymer:
                replaced = True
                polymer = polymer.replace(unit, "").replace(unit[::-1],"")

        if replaced == False:
            break
    
    return polymer


# replace each unit and reduce

least = len(polymer)

for c in range(ord('a'), ord('z')+1):

    replaced_polymer = polymer.replace(chr(c),"").replace(chr(c-32),"")
    reduced_polymer = reduce(replaced_polymer)

    if len(reduced_polymer) < least:
        least = len(reduced_polymer)

print least

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/3
#

import re

f = open("day03-input.txt")
lines = f.read().split("\n")

taken = {}

# map all claims
for line in lines:
    id, col, row, width, height = map(int, re.findall(r"#(.*) @ (.*),(.*): (.*)x(.*)", line)[0])

    for r in range(row, row+height):
        for c in range(col, col+width):
            if (r,c) in taken:
                taken[(r,c)].append(id)
            else:
                taken[(r,c)] = [id]

# check for overlaps
for line in lines:
    id, col, row, width, height = map(int, re.findall(r"#(.*) @ (.*),(.*): (.*)x(.*)", line)[0])

    unclaimed = True
    for r in range(row, row+height):
        for c in range(col, col+width):
            if len(taken[(r,c)]) > 1:
                unclaimed = False
    
    if unclaimed == True:
        print id

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/5
#

f = open("day5-input.txt")
#f = open("day5-testinput.txt")

# read instructions
instructions = []
for line in f.readlines():
    instructions.append(int(line))

pos = 0
count = 0
while pos < len(instructions):
    instructions[pos] += 1
    pos = pos + instructions[pos] - 1
    count += 1

print count

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/7
#

import re

f = open("day8-input.txt")
#f = open("day8-testinput.txt")

registers = {}


def modify(r, ins, v):
    if ins == "inc":
        registers[r] += v
    elif ins == "dec":
        registers[r] -= v

max_value = None

for line in f:

    r1, ins, v1, tmp, r2, condition, v2 = re.findall(r'([^ ]+)', line)

    v1 = int(v1)
    v2 = int(v2)

    if r1 not in registers:
        registers[r1] = 0
    if r2 not in registers:
        registers[r2] = 0

    if eval("{}{}{}".format(registers[r2], condition, v2)):
        modify(r1, ins, v1)

    max_value = max(registers.values()) if (max_value == None or max(
        registers.values()) > max_value) else max_value

print "Final highest value =", max(registers.values())
print "Hightst value ever =", max_value

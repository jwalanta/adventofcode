#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2019/day/2
#

def read_input():
    f = open("input.txt")
    return list(map(int, f.read().split(",")))

def execute(op, x, y):
    p = 0
    op[1], op[2] = x, y

    while True:
        if op[p] == 1:
            op[op[p+3]] = op[op[p+1]] + op[op[p+2]]
        elif op[p] == 2:
            op[op[p+3]] = op[op[p+1]] * op[op[p+2]]
        elif op[p] == 99:
            break
        p += 4

    return op[0]

input = read_input()

print("Part 1: %d" % execute(input[:], 12, 2))
print("Part 2: %d" % [100*x+y for x in range(0,100) for y in range(0,100) if execute(input[:], x, y) == 19690720][0])


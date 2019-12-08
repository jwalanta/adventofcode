#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2019/day/7
#

import itertools

op = list(map(int, open("input.txt").read().split(",")))

# get value based on mode


def val(op, p, mode):
    if mode == 0:   # position mode (return the value at position)
        return op[op[p]]
    else:  # intermediate mode (return the value)
        return op[p]

# run the opcodes


def execute(op, n):
    p = 0

    while p < len(op):

        opcode = op[p] % 100  # get opcode (last two digits)
        c = (op[p] // 100) % 10  # mode of 1st parameter (100th digit)
        b = (op[p] // 1000) % 10  # mode of 2nd parameter (1000th digit)
        # no need to calculate mode of 3rd parameter, it's always position mode

        #
        # part 1 mode (1-4)
        if opcode == 1:  # add
            op[op[p+3]] = val(op, p+1, c) + val(op, p+2, b)
            p += 4
        elif opcode == 2:  # multiply
            op[op[p+3]] = val(op, p+1, c) * val(op, p+2, b)
            p += 4
        elif opcode == 3:  # get input
            op[op[p+1]] = n.pop(0)
            p += 2
        elif opcode == 4:  # print input
            return val(op, p+1, c)
            p += 2

        #
        # part 2 additional modes (5-8)
        #
        elif opcode == 5:  # set position if greater than zero
            if val(op, p+1, c) > 0:
                p = val(op, p+2, b)
            else:
                p += 3
        elif opcode == 6:  # set position if equal to zero
            if val(op, p+1, c) == 0:
                p = val(op, p+2, b)
            else:
                p += 3
        elif opcode == 7:  # set 1 if 1st param < 2nd param, else 0
            if val(op, p+1, c) < val(op, p+2, b):
                op[op[p+3]] = 1
            else:
                op[op[p+3]] = 0
            p += 4
        elif opcode == 8:  # set 1 if 1st param = 2nd param, else 0
            if val(op, p+1, c) == val(op, p+2, b):
                op[op[p+3]] = 1
            else:
                op[op[p+3]] = 0
            p += 4

        elif opcode == 99:  # halt
            return None


#op = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
#op = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
#op = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

hi = 0
seq = []

for phases in itertools.permutations(range(0, 5)):
    n = 0
    for ph in phases:
        n = execute(op[:], [ph, n])

    if n > hi:
        hi = n
        seq = phases[:]


print("Part 1: %d" % hi)
# print(seq)

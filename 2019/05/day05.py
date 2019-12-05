#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2019/day/5
#


def read_input():
    f = open("input.txt")
    return [int(n) for n in f.read().split(",")]

# get value based on mode
def val(op, p, mode):
    if mode == 0:   # position mode (return the value at position)
        return op[op[p]]
    else:  # intermediate mode (return the value)
        return op[p]

# run the opcodes
def execute(op, n):
    p = 0

    output = []

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
            op[op[p+1]] = n
            p += 2
        elif opcode == 4:  # print input
            output.append(val(op, p+1, c))
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
            break

    return output


input = read_input()

# part 1
print("Part 1: %d" % execute(input[:], 1)[-1])

# part 2
print("Part 2: %d" % execute(input[:], 5)[-1])

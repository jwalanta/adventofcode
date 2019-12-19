#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Advent of Code 2019 IntCode
#

# run the opcodes
def execute(op):

    # program can have more memory than the code
    op.extend([0]*5000)

    p = 0   # program pointer
    relative_base = 0

    # get value based on mode
    def val(op, p, mode):
        return op[addr(op, p, mode)]

    # get address based on mode
    def addr(op, p, mode):
        if mode == 0:   # position mode (return the value at position)
            return op[p]
        elif mode == 1:  # intermediate mode (return the value)
            return p
        elif mode == 2:  # relative mode
            return op[p] + relative_base
        else:
            print("ERROR")

    # execute the code
    while p < len(op):

        opcode = op[p] % 100  # get opcode (last two digits)
        c = (op[p] // 100) % 10  # mode of 1st parameter (100th digit)
        b = (op[p] // 1000) % 10  # mode of 2nd parameter (1000th digit)
        a = (op[p] // 10000) % 10  # mode of 3nd parameter (1000th digit)

        if opcode == 1:  # add
            op[addr(op, p+3, a)] = val(op, p+1, c) + val(op, p+2, b)
            p += 4
        elif opcode == 2:  # multiply
            op[addr(op, p+3, a)] = val(op, p+1, c) * val(op, p+2, b)
            p += 4
        elif opcode == 3:  # get input
            op[addr(op, p+1, c)] = yield
            p += 2
        elif opcode == 4:  # print output
            yield val(op, p+1, c)
            p += 2
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
                op[addr(op, p+3, a)] = 1
            else:
                op[addr(op, p+3, a)] = 0
            p += 4
        elif opcode == 8:  # set 1 if 1st param = 2nd param, else 0
            if val(op, p+1, c) == val(op, p+2, b):
                op[addr(op, p+3, a)] = 1
            else:
                op[addr(op, p+3, a)] = 0
            p += 4
        elif opcode == 9:   # change relative base
            relative_base += val(op, p+1, c)
            p += 2

        elif opcode == 99:  # halt
            raise Exception("HALT")

    raise Exception("OUT OF ADDRESS")


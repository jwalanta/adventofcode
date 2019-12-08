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


# Rewriting the function to use generators, so that it stops when needing
# input and when yielding output

# run the opcodes
def execute(op):
    p = 0

    while True:

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
            op[op[p+1]] = yield

            p += 2
        elif opcode == 4:  # print input
            yield val(op, p+1, c)
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


# test programs
#op = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
#op = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]


#
# Part 1 (rewrite using generators)
#
hi = 0
seq = []
for phases in itertools.permutations(range(0, 5)):
    n = 0  # input for first amp is 0
    for ph in phases:
        amp = execute(op[:])  # create amp
        next(amp)   # run till it needs input
        amp.send(ph)  # first input is phase setting
        n = amp.send(n)  # second input is output from previous amp

    if n > hi:
        hi = n
        seq = phases[:]

print("Part 1: %d" % hi)
# print(seq)


#
# Part 2
#
hi = 0
seq = []
for phases in itertools.permutations(range(5, 10)):

    # create feedback loop amps with this phase setting
    amps = []

    # first, create amps and provide phase setting as first input value
    for ph in phases:
        # create amps with phase value
        amp = execute(op[:])

        # run and wait till input is required
        next(amp)

        # first input value is phase setting
        amp.send(ph)

        # store this amp
        amps.append(amp)

    # after the first value, i/o is signal from amps
    signal = 0  # signal to amp A for the first time is 0

    # run amps in feedback mode till it breaks
    while True:

        # first round, pass signal through amps
        for amp in amps:
            # provide input (signal from previous amp)
            signal = amp.send(signal)

        # second round, run the program till it needs input or breaks
        try:
            for amp in amps:
                next(amp)
        except StopIteration:
            break

    if signal > hi:
        hi = signal
        seq = phases[:]


print("Part 2: %d" % hi)
# print(seq)

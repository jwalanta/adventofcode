#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2019/day/11
#

import math
from collections import defaultdict

input = list(map(int, open("input.txt").read().strip().split(",")))

# run the opcodes
def execute(op):

    # program can have more memory than the code
    op.extend([0]*5000)

    p = 0   # program pointer
    relative_base = 0

    output = []

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

    return output


def run_robot(init_color):

    deltas = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

    x, y = 0, 0
    current_direction = "U"
    dx, dy = deltas[current_direction]
    panels = defaultdict(int)

    panels[(0, 0)] = init_color

    # create generator
    robot = execute(input)

    try:

        while True:

            # run robot till next input is needed
            next(robot)

            # send current panel color and get first output
            panels[(x, y)] = robot.send(panels[(x, y)])

            # get second output
            direction = next(robot)

            # change direction
            if direction == 0:  # left 90 degrees
                changes = {"R": "U", "L": "D", "U": "L", "D": "R"}
            else:  # right 90 degrees
                changes = {"R": "D", "L": "U", "U": "R", "D": "L"}

            # change direction and delta values
            current_direction = changes[current_direction]
            dx, dy = deltas[current_direction]

            x, y = x + dx, y + dy

    except Exception as err:  # run robot till it halts
        pass

    if init_color == 0:  # part 1
        print("Part 1: %d" % len(panels))
    else:  # part 2
        print("Part 2:")

        rows = [x[0] for x in panels.keys()]
        cols = [x[1] for x in panels.keys()]

        for r in range(min(rows), max(rows)+1):
            for c in range(min(cols), max(cols)+1):
                print("█" if panels[(r, c)] == 1 else " ", end="")
            print()


run_robot(0)  # part 1
run_robot(1)  # part 2

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2019/day/13
#

import os
import curses

opcode = list(map(int, open("input.txt").read().strip().split(",")))

# global joystick value to move the paddle (input to Intcode)
joystick = 0

# run the opcodes
def execute(op):

    global joystick

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
            op[addr(op, p+1, c)] = joystick
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

#
# Part 1
#
def part1():
    arcade = execute(opcode[:])
    block = 0
    try:
        while True:
            x = next(arcade)
            y = next(arcade)
            n = next(arcade)

            if n == 2:
                block = block+1

    except Exception as err:
        pass

    print("Part 1: %d" % block)

#
# Part 2
#
def part2(animate=True):

    global joystick

    opcode[0] = 2 # set memory at 0 to 2 for free plays
    arcade = execute(opcode[:])
    px, bx = 0, 0    # paddle x, ball x
    score = 0

    icons = {0: " ", 1: "█", 2: "■", 3: "=", 4: "⦿"}

    if animate:
        screen = curses.initscr()
        curses.curs_set(0)  # dont display cursor

    # animation pause. initially 0, adjusted after whole grid is drawn
    pause = 0

    try:
        while True:
            x = next(arcade)
            y = next(arcade)
            n = next(arcade)

            if animate and x >= 0 and y >= 0:
                screen.addstr(1, 1, "SCORE=" + str(score))
                screen.addstr(y+2, x+1, icons[n])
                screen.refresh()
                curses.napms(pause)

            # store paddle and ball x coordinates
            px = x if n == 3 else px
            bx = x if n == 4 else bx

            # adjust
            if bx < px:
                joystick = -1
            elif bx > px:
                joystick = 1
            else:
                joystick = 0

            # if x=-1 and y=0, n is score
            if x == -1 and y == 0:
                score = n
                pause = 3  # adjust pause after intcode outputs score first time

    except Exception as err:
        # print(err)
        pass

    if animate:
        curses.napms(1000)
        curses.endwin()

    print("Part 2: %d" % score)


part1()
part2(animate=True)

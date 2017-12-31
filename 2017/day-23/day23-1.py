#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/23
#

instructions = open("day23-input.txt").read().strip().split("\n")

registers = {}

pointer = 0
mulcount = 0

count = 0


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

while True:

    if pointer < 0 or pointer >= len(instructions):
        break

    cmd, x, y = instructions[pointer].split(" ")

    if not is_number(x) and x not in registers:
        registers[x] = 0
    if not is_number(y) and y not in registers:
        registers[y] = 0

    if is_number(y):
        y = int(y)
    else:
        y = registers[y]

    if cmd == "set":
        registers[x] = int(y)
    elif cmd == "sub":
        registers[x] -= y
    elif cmd == "mul":
        registers[x] *= y
        mulcount += 1
    elif cmd == "jnz":
        if is_number(x):
            x = int(x)
        else:
            x = registers[x]

        if x != 0:
            pointer += y
            continue

    pointer += 1

print mulcount

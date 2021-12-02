#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2021/day/2
#

def read_input():
    f = open("input.txt")
    return [(l.split(" ")[0], int(l.split(" ")[1])) for l in f.readlines()]

ins = read_input()

def part1():
    delta = {
        "forward": (0, 1),
        "down": (1, 0),
        "up": (-1, 0),
    }

    x, y = 0, 0
    for (cmd, n) in ins:
        dx, dy = delta[cmd]
        x, y = x + dx * n, y + dy * n

    return x * y


def part2():
    x, y, aim = 0, 0, 0
    for (cmd, n) in ins:
        if cmd == 'down':
            aim = aim + n
        elif cmd == 'up':
            aim = aim - n
        elif cmd == 'forward':
            x = x + n
            y = y + aim * n

    return x * y


print("Part 1: %d" % part1())
print("Part 2: %d" % part2())

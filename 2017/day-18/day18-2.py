#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/18
#


f = open("day18-input.txt")
instructions = f.read().split("\n")

register = [{}, {}]
position = [0, 0]
rcv_queue = [[], []]
lock = [False, False]
count = [0, 0]


def execute(n):

    p = instructions[position[n]].strip().split(" ")

    if (not p[1].isdigit()) and (p[1] not in register[n]):
        register[n][p[1]] = 0

    if (2 in p) and (not p[2].isdigit()) and (p[1] not in register[n]):
        register[n][p[2]] = 0

    if p[0] == "snd":
        r = abs(n - 1)

        if p[1].isdigit():
            rcv_queue[r].append(p[1])
        else:
            rcv_queue[r].append(register[n][p[1]])

        count[n] += 1

    elif p[0] == "set":
        try:
            register[n][p[1]] = int(p[2])
        except ValueError:
            register[n][p[1]] = register[n][p[2]]
    elif p[0] == "add":
        try:
            register[n][p[1]] += int(p[2])
        except ValueError:
            register[n][p[1]] += register[n][p[2]]
    elif p[0] == "mul":
        try:
            register[n][p[1]] *= int(p[2])
        except ValueError:
            register[n][p[1]] *= register[n][p[2]]
    elif p[0] == "mod":
        try:
            register[n][p[1]] %= int(p[2])
        except ValueError:
            register[n][p[1]] %= register[n][p[2]]
    elif p[0] == "rcv":
        if len(rcv_queue[n]) > 0:
            register[n][p[1]] = rcv_queue[n][0]
            rcv_queue[n] = rcv_queue[n][1:]
            lock[n] = False

        else:
            lock[n] = True
            # dont increment position
            return
    elif p[0] == "jgz":
        x = p[1] if p[1].isdigit() else register[n][p[1]]
        if x > 0:
            try:
                position[n] += int(p[2])
            except ValueError:
                position[n] += register[n][p[2]]

            return

    position[n] += 1


# initial values
register[0]["p"] = 0
register[1]["p"] = 1

while not (lock[0] and lock[1]):
    execute(1)
    execute(0)

print count[1]

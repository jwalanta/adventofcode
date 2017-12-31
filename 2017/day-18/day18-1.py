#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/18
#


f = open("day18-input.txt")
instructions = f.read().split("\n")

register = {}
freq = 0

position = 0
while position < len(instructions):
    p = instructions[position].strip().split(" ")

    if p[1] not in register:
        register[p[1]] = 0

    if p[0] == "snd":
        freq = register[p[1]]
        # print p, register[p[1]]
    elif p[0] == "set":
        try:
            register[p[1]] = int(p[2])
        except ValueError:
            register[p[1]] = register[p[2]]
    elif p[0] == "add":
        try:
            register[p[1]] += int(p[2])
        except ValueError:
            register[p[1]] += register[p[2]]
    elif p[0] == "mul":
        try:
            register[p[1]] *= int(p[2])
        except ValueError:
            register[p[1]] *= register[p[2]]
    elif p[0] == "mod":
        try:
            register[p[1]] %= int(p[2])
        except ValueError:
            register[p[1]] %= register[p[2]]
    elif p[0] == "rcv":
        if register[p[1]] != 0:
            # print p, register[p[1]]
            print "last played frequency =", freq
            break
    elif p[0] == "jgz":
        if register[p[1]] != 0:
            position += int(p[2])
            continue

    position += 1

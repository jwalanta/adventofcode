#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/16
#


def program_dance(programs, dance):
    for d in dance:
        if d[0] == "s":
            n = int(d[1:])
            programs = programs[-n:] + programs[:-n]
        elif d[0] == "x":
            n = map(int, d[1:].split("/"))
            programs[n[0]], programs[n[1]] = programs[n[1]], programs[n[0]]
        elif d[0] == "p":
            s = d[1:].split("/")
            n0 = programs.index(s[0])
            n1 = programs.index(s[1])
            programs[n0], programs[n1] = programs[n1], programs[n0]

    return programs

# print program_dance("abcde",["s1","x3/4","pe/b"])

programs = list("abcdefghijklmnop")

f = open("day16-input.txt")
dance = f.read().strip().split(",")

print ''.join(program_dance(programs, dance))

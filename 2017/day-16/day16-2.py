#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/16
#


def program_dance(iteration, programs, dance):

    variations = []
    variations.append(''.join(programs))
    for i in xrange(iteration):
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

        # program variations repeat after a while
        # so gather all of them. once they start repeating,
        # we can get the variation at any iteration
        p = ''.join(programs)
        if p == variations[0]:
            return variations[iteration % len(variations)]
            break

        variations.append(p)

programs = list("abcdefghijklmnop")

f = open("day16-input.txt")
dance = f.read().strip().split(",")

print program_dance(1000000000, programs, dance)

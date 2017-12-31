#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/20
#

import re

# read input
f = open("day20-input.txt")

p = {}
v = {}
a = {}
n = 0
for line in f:
    p[n], v[n], a[n] = map(lambda x: x.split(","), re.findall(
        r"p=<(.*)>, v=<(.*)>, a=<(.*)>", line)[0])
    p[n] = map(int, p[n])
    v[n] = map(int, v[n])
    a[n] = map(int, a[n])
    n += 1


def update():
    for n in range(len(p)):
        for i in range(3):
            v[n][i] += a[n][i]
        for i in range(3):
            p[n][i] += v[n][i]


def get_closest():
    min = abs(p[0][0]) + abs(p[0][1]) + abs(p[0][2])
    index = 0
    for n in range(len(p)):
        d = abs(p[n][0]) + abs(p[n][1]) + abs(p[n][2])
        if d < min:
            index = n
            min = d

    return index

# lets try 1000 runs
for n in range(1000):
    update()

print get_closest()

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
collision = set()
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
        if n in collision:
            continue
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


def mark_collision():
    for n in range(len(p)):
        if n in collision:
            continue
        for m in range(len(p)):
            if n == m:
                continue
            if p[n][0] == p[m][0] and p[n][1] == p[m][1] and p[n][2] == p[m][2]:
                collision.add(n)
                collision.add(m)

for n in range(100):
    update()
    mark_collision()

print len(p) - len(collision)

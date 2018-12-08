#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/8
#

from collections import defaultdict

f = open("day08-input.txt")
num = map(int, f.read().split())

c = 0

def traverse():
    global c

    nc = num[c]
    nm = num[c + 1]

    c = c + 2

    child = []
    meta = []
    for i in range(nc):
        child.append(traverse())

    for i in range(nm):
        meta.append(num[c])
        c = c + 1

    return (child, meta)


def val((child, meta)):
    if len(child) == 0:
        return sum(meta)
    else:
        total = 0
        for m in meta:
            if m > 0 and m <= len(child):
                total = total + val(child[m - 1])
        return total


root = traverse()

print val(root)

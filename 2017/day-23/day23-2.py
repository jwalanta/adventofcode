#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/23
#


def prime(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
    else:
        return False

    return True

b = 109300
c = 126300
h = 0
for b in range(109300, c + 1, 17):
    if not prime(b):
        h += 1

print h

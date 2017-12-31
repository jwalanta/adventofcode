#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/17
#

buffer = [0]
position = 0

steps = 344

n = 1

while n <= 2017:
    # step

    position += steps
    position %= len(buffer)

    # insert
    buffer = buffer[:position + 1] + [n] + buffer[position + 1:]
    position += 1
    n += 1


print buffer[buffer.index(2017) + 1]

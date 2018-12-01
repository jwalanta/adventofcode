#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/1
#

f = open("day01-01.input.txt")
deltas = map(int, f.read().split())

freq = 0

for delta in deltas:
    freq = freq + delta

print freq
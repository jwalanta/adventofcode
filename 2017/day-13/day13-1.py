#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/13
#

f = open("day13-input.txt")

layers = {}

# create layers
for line in f:
    s = line.split(": ")
    n = int(s[1])
    layers[int(s[0])] = range(0, n) + range(n - 2, 0, -1)

# create empty layers missing in input
for l in range(max(layers)):
    if l not in layers:
        layers[l] = []


sum = 0
for l in range(max(layers) + 1):
    if len(layers[l]) == 0:
        continue

    pos = layers[l][l % len(layers[l])]

    if pos == 0:
        sum += (l * (len(layers[l]) + 2) / 2)

print sum

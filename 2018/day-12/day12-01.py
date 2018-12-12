#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/12
#

from collections import defaultdict

f = open("day12-input.txt")
lines = f.read().split("\n")

state = ""
changes = {}

# parse input
for line in lines:
    if "initial state" in line:
        state = line.split(" ")[2]
    elif "=>" in line:
        changes[line.split()[0]] = line.split()[2]

pos = 0
for _ in range(20):
    newstate = ""
    for i in range(-5, len(state) + 5):
        match = ""
        for j in range(i - 2, i + 3):
            if j < 0 or j >= len(state):
                match = match + "."
            else:
                match = match + state[j]

        if match in changes:
            newstate = newstate + changes[match]
        else:
            newstate = newstate + "."

    state = newstate
    pos = pos - 5

total = 0
for i in range(len(state)):
    if state[i] == "#":
        total = total + pos

    pos = pos + 1

print total

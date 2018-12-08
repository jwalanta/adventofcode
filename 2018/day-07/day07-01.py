#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/7
#

from collections import defaultdict

f = open("day07-input.txt")
lines = f.read().split("\n")

dep = defaultdict(list)
letters = set([])

for l in lines:
    p = l.split(" ")
    dep[p[7]].append(p[1])
    letters.add(p[1])
    letters.add(p[7])

sequence = []

# check if l is valid as next item in sequence
def valid(l):
    if l not in dep.keys():
        return True

    for d in dep[l]:
        if d not in sequence:
            return False

    return True


# loop till letters[] is empty
while letters:

    # loop through available letters and see if they can be the next
    for l in sorted(letters):

        if valid(l):
            sequence.append(l)
            letters.remove(l)
            break

print "".join(sequence)


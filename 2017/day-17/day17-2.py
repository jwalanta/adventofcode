#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/17
#


# we dont need to compute the whole buffer,
# just the number at position #1 (after #0)

position = 0
steps = 344
n = 1  # assuming 0 as initial item

# number at position #1
pos1 = 0

# this takes a while
print "Please wait.."
while n < 50000000:
    # step

    position += steps
    position %= n

    # after insert
    position += 1

    if position == 1:
        # new number at position #1
        pos1 = n

    n += 1


print pos1

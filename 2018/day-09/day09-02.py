#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/9
#

# implementation using list is too slow for part 2,
# so reimplementing this using collections.deque
# (hints from reddit)

from collections import deque

def play(num_elves, num_marbles):

    scores = [0 for _ in range(num_elves)]
    marbles = deque([0])

    # current  elf turn
    elf = 0

    for marble in range(1, num_marbles+1):
        if marble % 23 == 0:
            marbles.rotate(7)
            scores[elf] = scores[elf] + marble + marbles.pop()
            marbles.rotate(-1)

        else:
            marbles.rotate(-1)
            marbles.append(marble)

        elf = (elf + 1) % num_elves

    return max(scores)


# 459 players; last marble is worth 72103 points x 100
print play(459,7210300)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/9
#


def play(num_elves, num_marbles):

    pos = 0
    c = 1
    elves = [0 for i in range(num_elves)]
    player = 0
    marbles = [0]

    while c <= num_marbles:

        if c % 23 == 0:
            pos = (pos - 7) % len(marbles)
            elves[player] = elves[player] + c + marbles[pos]
            marbles = marbles[0:pos] + marbles[pos + 1:]
        else:
            # place marble between 1 and 2 clockwise
            split = (pos + 1) % len(marbles)
            marbles = marbles[0:split + 1] + [c] + marbles[split + 1:]
            pos = split + 1

        c = c + 1
        player = player + 1
        if player == num_elves:
            player = 0

    return max(elves)


# 459 players; last marble is worth 72103 points
print play(459, 72103)

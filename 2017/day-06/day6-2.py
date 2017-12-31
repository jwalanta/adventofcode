#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/6
#


input = "11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11"
#input = "0 2 7 0"
banks = map(int, input.split())

states = {}


def check_and_save_state():
    state = tuple(banks)
    if state in states:
        print "Last seen before", len(states) - states[state] + 1, "steps"
        return False
    else:
        states[state] = len(states) + 1
        return True


def find_max_index():
    max = banks[0]
    index = 0

    for i in xrange(len(banks)):
        if banks[i] > max:
            max = banks[i]
            index = i

    return index


def redistribute(i):

    value = banks[i]
    banks[i] = 0

    d = int(round(float(value) / len(banks)))

    while value > 0:
        i += 1
        banks[i % len(banks)] += d if d < value else value
        value -= d

count = 0
while check_and_save_state():
    redistribute(find_max_index())
    count += 1

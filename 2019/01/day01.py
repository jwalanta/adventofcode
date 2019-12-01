#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2019/day/1
#

def parse_line(line):
    return int(line)

def read_input():
    f = open("input.txt")
    return [parse_line(l) for l in f.readlines()]

def calculate_fuel(n):
    sum = 0
    while n > 0:
        n = n//3-2
        if n < 0:
            break
        sum += n

    return sum

input = read_input()

print("Part 1: %d" % sum(map(lambda x: x//3-2, input)))
print("Part 2: %d" % sum(map(calculate_fuel, input)))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2021/day/1
#

def read_input():
    f = open("input.txt")
    return [int(l) for l in f.readlines()]

n = read_input()

# part 1
print("Part 1: %d" % len([i for i in range(0, len(n)-1) if n[i+1] > n[i]]))

# part 2
# index 1 + 2 + 3 > 0 + 1 + 2 
# => index 3 > 0
print("Part 2: %d" % len([i for i in range(0, len(n)-3) if n[i+3] > n[i]]))

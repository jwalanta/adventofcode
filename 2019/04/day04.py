#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2019/day/4
#

# input
min, max = 109165, 576723

# part 1. find if number contains adjacent digits
def adjacent(n_str):
    for s in ["00", "11", "22", "33", "44", "55", "66", "77", "88", "99"]:
        if n_str.find(s) > -1:
            return True
    return False

# part 2. find if number contains adjacent digits not part of bigger group
def adjacent2(n_str):
    prev = ''
    count = 0
    adjacent_count = 0
    for s in n_str:
        if prev == s:
            count = count + 1
        else:
            # adjacent digits with length > 2 are part of big group. ignore
            if count == 2:
                adjacent_count = adjacent_count + 1

            prev = s
            count = 1

    # count adjacent digits at the end
    if count == 2:
        adjacent_count = adjacent_count + 1

    return adjacent_count > 0

# find if number has digits in increasing order
def increasing(n_str):
    for i in range(1, len(n_str)):
        if n_str[i] < n_str[i-1]:
            return False
    return True


print("Part 1: %d" % len([i for i in range(min, max)
                          if adjacent(str(i)) and increasing(str(i))]))
print("Part 2: %d" % len([i for i in range(min, max)
                          if adjacent2(str(i)) and increasing(str(i))]))

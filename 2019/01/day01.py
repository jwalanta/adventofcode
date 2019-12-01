#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2019/day/1
#

import math

def calculateFuel(n):
    sum = 0
    while n > 0:
        n = math.floor(n / 3) - 2
        if n < 0:
            break
        sum += n

    return int(sum)


f = open("input.txt")

sum1 = 0
sum2 = 0
for line in f.readlines():
    sum1 += int(math.floor(int(line) / 3) - 2)
    sum2 += calculateFuel(int(line))


print("Part 1: %d" % sum1)
print("Part 2: %d" % sum2)
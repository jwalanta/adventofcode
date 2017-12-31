#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/2
#

#f = open("day2-testinput.txt")
f = open("day2-input.txt")

checksum = 0


def find_evenly_divisible(numbers):
    for x in xrange(len(numbers) - 1):
        for y in xrange(x + 1, len(numbers)):
            if numbers[y] % numbers[x] == 0:
                return numbers[y] / numbers[x]

for line in f.readlines():
    numbers = map(int, line.split())
    numbers.sort()
    checksum = checksum + find_evenly_divisible(numbers)

print checksum

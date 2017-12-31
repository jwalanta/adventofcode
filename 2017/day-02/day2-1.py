#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/2
#

f = open("day2-input.txt")

checksum = 0

for line in f.readlines():
    numbers = map(int, line.split())
    numbers.sort()
    checksum = checksum + (numbers[-1] - numbers[0])

print checksum

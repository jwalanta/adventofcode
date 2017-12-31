#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/15
#


# test
# a=65
# b=8921

# input
a = 699
b = 124

fa = 16807
fb = 48271

d = 2147483647

count = 0
for i in range(40000000):
    a = (a * fa) % d
    b = (b * fb) % d

    # print a,b

    if (a & 65535 == b & 65535):
        count += 1
        # print "match"

print count

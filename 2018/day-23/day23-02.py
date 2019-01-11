#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/23
#

# Suggestion from reddit (https://www.reddit.com/comments/a8s17l) was to view
# this as optimization problem and use the z3 library.

# we have a list of "bots" with points and radius:
# x, y1, z1, r1
# x2, y2, z2, r2
# ..
# ..
# x<n>, y<n>, z<n>, r<n>
#
# the point (x,y,z) is within the radius of the bot if manhattan distance from
# (x,y,z) to the bot is less than or equal to the radius. We can create an
# expression using Z3 which returns 1 if it's within radius, or 0 if not. We can
# then maximize this expression to get the values of x,y,z which is within the
# range of most of the bots

import re
from z3 import *


# z3 version of abs, since n can be unknown z3 variable
def z3abs(n):
    return If(n >= 0, n, -n)


# z3 version of manhattan distance
def z3mdist(x1, y1, z1, x2, y2, z2):
    return z3abs(x1 - x2) + z3abs(y1 - y2) + z3abs(z1 - z2)


# read input
f = open("day23-input.txt")
lines = f.read().split("\n")

# define variables
x, y, z = Ints('x y z')
total_within_range = Int('total_within_range')
expr = 0

# we now create the expression with all the bot points. each will return 1 if
# (x,y,z) is within bot's range, or 0 otherwise
for line in lines:
    px, py, pz, pr = map(int,
                         re.findall("pos=<(.*),(.*),(.*)>, r=(.*)", line)[0])
    # 1 if (x,y,z) is within bot's range, 0 otherwise
    expr += If(z3mdist(x, y, z, px, py, pz) <= pr, 1, 0)

# now optimize the expression.
# maximize it for total bots within range
# and minimize for distance from origin
o = Optimize()

o.add(total_within_range == expr)

o.maximize(total_within_range)
o.minimize(z3mdist(0, 0, 0, x, y, z))

# check for answers
o.check()

# answer
m = o.model()

#print m
print abs(m[x].as_long()) + abs(m[y].as_long()) + abs(m[z].as_long())

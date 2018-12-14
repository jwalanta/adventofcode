#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/14
#

import sys

input = 505961

recipes = [3, 7]
e1 = 0
e2 = 1

while len(recipes) < (input + 10):

    total = recipes[e1] + recipes[e2]

    if total < 10:
        recipes.append(total)
    else:
        recipes.append(int(total / 10))
        recipes.append(total % 10)

    # pick a new current recipe
    e1 = (e1 + 1 + recipes[e1]) % len(recipes)
    e2 = (e2 + 1 + recipes[e2]) % len(recipes)

    # # print recipes
    # for i in range(len(recipes)):
    #     if i == e1:
    #         print "(%d)" % recipes[i],
    #     elif i == e2:
    #         print "[%d]" % recipes[i],
    #     else:
    #         print "",recipes[i],"",
    # print

print "".join(map(str, recipes[input:input + 10]))

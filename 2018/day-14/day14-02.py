#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/14
#

import sys

input = 505961
len_input = len(str(input))

recipes = [3, 7]

e1 = 0
e2 = 1


def check():
    if str(input) == "".join(map(str, recipes[-len_input:])):
        print len(recipes) - len_input
        sys.exit()


while True:

    total = recipes[e1] + recipes[e2]

    if total < 10:
        recipes.append(total)
        check()
    else:
        recipes.append(int(total / 10))
        check()

        recipes.append(total % 10)
        check()

    # pick a new current recipe
    e1 = (e1 + 1 + recipes[e1]) % len(recipes)
    e2 = (e2 + 1 + recipes[e2]) % len(recipes)

    # for i in range(len(recipes)):
    #     if i == elf1:
    #         print "(%d)" % recipes[i],
    #     elif i == elf2:
    #         print "[%d]" % recipes[i],
    #     else:
    #         print "",recipes[i],"",
    # print

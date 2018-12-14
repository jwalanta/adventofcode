#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/14
#

import sys

input = 505961

recipes = [3,7]
e1 = 0
e2 = 1

while len(recipes) < (input + 10):

    if len(recipes) % 100 == 0:
        print len(recipes)

    total = recipes[e1] + recipes[e2]

    if total < 10:
        recipes.append(total)
    else:
        recipes.append(int(total/10))
        recipes.append(total%10)

    #recipes = recipes + map(int, list(str(total)))

    # pick a new current recipe
    etotal = 1 + recipes[e1]
    while etotal:
        e1 = (e1 + 1) % len(recipes)
        etotal = etotal -1

    # elf 1
    etotal = 1 + recipes[e2]
    while etotal:
        e2 = (e2 + 1) % len(recipes)
        etotal = etotal -1

    # # print recipes
    # for i in range(len(recipes)):
    #     if i == e1:
    #         print "(%d)" % recipes[i],
    #     elif i == e2:
    #         print "[%d]" % recipes[i],
    #     else:
    #         print "",recipes[i],"",
    # print


print "".join(map(str,recipes[input:input+10]))
        

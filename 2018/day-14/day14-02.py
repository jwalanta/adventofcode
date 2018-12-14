#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/14
#

import sys

input = 505961
len_input = len(str(input))

recipes = [3,7]

e1 = 0
e2 = 1

def check():
    if input == "".join(map(str, recipes[-len_input:])):
        print len(recipes) - len_input
        sys.exit()


while True:

    if len(recipes) % 10000 == 0:
        print len(recipes)

    total = recipes[e1] + recipes[e2]

    #recipes = recipes + map(int, list(str(total)))

    if total < 10:
        recipes.append(total)
        check()
    else:
        recipes.append(int(total/10))
        check()

        recipes.append(total%10)
        check()

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


    # for i in range(len(recipes)):
    #     if i == elf1:
    #         print "(%d)" % recipes[i],
    #     elif i == elf2:
    #         print "[%d]" % recipes[i],
    #     else:
    #         print "",recipes[i],"",
    # print

    if str(input) in "".join(map(str, recipes[-10:])):
        #print recipes
        print len(recipes) - 6
        break
        

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/25
#

f = open("day25-input.txt")
lines = f.read().split("\n")

P = []  # points
C = []  # constellations

# read input points
for line in lines:
    P.append(tuple(map(int, line.split(","))))

# manhattan distance
def mdist((a1,b1,c1,d1), (a2,b2,c2,d2)):
    return abs(a1-a2) + abs(b1-b2) + abs(c1-c2) + abs(d1-d2)

# check if p is part of constellation C[n] 
# insert into C[n] if it is
def check_constellation(p, n): 
    for cp in C[n]:
        if mdist(p, cp) <= 3:
            C[n].append(p)
            return True

    return False


for p in P:

    # check if point belongs to any constellation
    clist = []
    for i in range(len(C)):
        if check_constellation(p, i):
            clist.append(i)
    
    # if not, create a new constellation and add the point
    if len(clist) == 0:
        C.append([])
        C[len(C)-1].append(p)


    # if point is part of multiple constellations, merge them
    if len(clist) > 1:

        # merge constellations
        ll = []
        for cl in clist:
            ll = ll + C[cl]

        # remove merged constellations
        n=0
        for cl in clist:
            del C[cl-n]
            n+=1 # increase n because removing will decrease the index

        # new merged constellation
        C.append(ll)

        
print len(C)

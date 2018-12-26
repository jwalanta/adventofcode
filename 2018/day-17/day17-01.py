#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/17
#

import re
import sys

f = open("day17-input.txt")
lines = f.read().split("\n")

D = {}  # clay
water = {}  # water
source = [] # source of water, used as stack
visited = []    # visited source of water (to avoid duplication)

# read the clay map
for line in lines:
    if line[0] == "x":
        x, y1, y2 = map(int, re.findall("x=(.*), y=(.*)\.\.(.*)", line)[0])
        for y in range(y1, y2+1):
            D[(x,y)] = "#"

    elif line[0] == "y":
        y, x1, x2 = map(int, re.findall("y=(.*), x=(.*)\.\.(.*)", line)[0])
        for x in range(x1, x2+1):
            D[(x,y)] = "#"

# bounds for the map
minx = min([x for x,y in D])
maxx = max([x for x,y in D])
miny = min([y for x,y in D])
maxy = max([y for x,y in D])

# print to file
def print_underground_to_file():
    f = open("/tmp/day17.txt","w")

    for y in range(miny-5,maxy+5):
        lnum = "%4d " % y
        f.write(lnum)
        for x in range(minx-5, maxx+5):
            if (x,y) in water:
                f.write(water[(x,y)])
            elif (x,y) in D:
                f.write("█")
            else:
                f.write(" ")

        f.write("\n")

    f.close()

# print on screen
def print_underground():
    BLUE = '\033[34m'
    GREEN = '\33[32m'
    ENDC = '\033[0m'

    for y in range(miny-1,maxy+1):
        lnum = "%4d " % y
        sys.stdout.write(lnum)
        for x in range(minx-1, maxx+1):
            if (x,y) in water and water[(x,y)] == "|":
                sys.stdout.write(BLUE + "|" + ENDC)
            elif (x,y) in water and water[(x,y)] == "~":
                sys.stdout.write(GREEN + "~" + ENDC)
            elif (x,y) in D:
                sys.stdout.write("█")
            else:            
                sys.stdout.write(" ")

        sys.stdout.write("\n")



# scan left and right for wall or overflow
# return: (left_x, left_overflow:bool, right_x, right_overflow:bool)
def scan(xx,y):
    leftx = 0
    rightx = 0
    left_overflow = False
    right_overflow = False

    # scan left
    for x in range(xx,0, -1):
        if (x,y) in D:
            leftx = x + 1
            left_overflow = False
            break
        if (x,y+1) not in D and ((x,y+1) not in water or water[(x,y+1)]=="|"):
            leftx = x
            left_overflow = True
            break

    # scan right
    for x in range(xx,maxx+1):
        if (x,y) in D:
            rightx = x - 1
            right_overflow = False
            break
        if (x,y+1) not in D and ((x,y+1) not in water or water[(x,y+1)]=="|"):
            rightx = x
            right_overflow = True
            break

    return (leftx, left_overflow, rightx, right_overflow)


# starts from 500,0
source.append((500,0))

while True:

    # stop if we're done processing all the water sources
    if len(source) == 0:
        break

    # start the flow
    x,y = source.pop()
    visited.append((x,y))

    # go down till it finds water or clay
    while (x,y+1) not in D and (x,y+1) not in water and y<=maxy:
        water[(x,y)] = "|"
        y += 1
    
    # if water goes out of bound, continue with next water source
    if y>maxy:
        continue

    # go up and scan till overflow
    while True:
        leftx, left_overflow, rightx, right_overflow = scan(x,y)
        
        if left_overflow or right_overflow:
            for xx in range(leftx, rightx+1):
                water[(xx,y)] = "|"

            if left_overflow and (leftx, y) not in visited:
                source.append((leftx, y))
            
            if right_overflow and (rightx, y) not in visited:
                source.append((rightx, y))

            break
        else:
            for xx in range(leftx, rightx+1):
                water[(xx,y)] = "~"
            
            y -= 1


#print_underground_to_file()
#print_underground()

# this is why you read the question properly. you're only supposed to count the
# tiles which are within the bounds. there are some tiles below 500,0 which
# could be out of data bounds

print "all =", len([w for w in water if w[1]>=miny])
print "flowing =", len([w for w in water if w[1]>=miny and water[w] == "~"])
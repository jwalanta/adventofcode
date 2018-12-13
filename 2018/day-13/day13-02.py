#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/13
#

import sys

f = open("day13-input.txt")
lines = f.read().split("\n")

field = {}  # field elements for direction change (r,c):"+"
carts = []  # carts ((r,c), (dr, dc), intersection_count)

# movement delta
delta = {
    ">" : ( 0, 1), 
    "<" : ( 0,-1),
    "^" : (-1, 0),
    "v" : ( 1, 0)
}

# mapping for left turn deltas
leftturn = {
    (-1, 0) : ( 0,-1), # up -> left
    ( 1, 0) : ( 0, 1), # down -> right
    ( 0,-1) : ( 1, 0), # left -> down
    ( 0, 1) : (-1, 0), # right -> up
}

# mapping for right turn deltas
rightturn = {
    (-1, 0) : ( 0, 1), # up -> right
    ( 1, 0) : ( 0,-1), # down -> left
    ( 0,-1) : (-1, 0), # left -> up
    ( 0, 1) : ( 1, 0), # right -> down
}

# read input
for r in range(len(lines)):
    for c in range(len(lines[r])):
        if lines[r][c] in "/+\\":
            field[(r, c)] = lines[r][c]
        elif lines[r][c] in "<>^v":
            carts.append(((r, c), delta[lines[r][c]], 0))
            # ^ ((r,c),(dr,dc), intersection_count)


# print the track
def print_track():

    cartmap = {}
    cartdirection = {v: k for k, v in delta.iteritems()}

    for f in field:
        cartmap[f] = field[f]

    for cart in carts:
        cartmap[cart[0]] = cartdirection[cart[1]]

    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if (x, y) in cartmap:
                print cartmap[(x, y)],
            else:
                if lines[x][y] in "-|":
                    print lines[x][y],
                else:
                    print " ",
        print

    print


crashed_carts = []
while True:

    # carts are read top to bottom, left to right
    carts = sorted(carts, key=lambda x: (x[0][0], x[0][1]))

    #print_track()

    # advance all carts
    for i in range(len(carts)):

        r, c = carts[i][0]
        dx, dy = carts[i][1]
        i_count = carts[i][2]

        carts[i] = ((r + dx, c + dy), (dx, dy), i_count)

        # check for crash
        for ii in range(len(carts)):
            for jj in range(len(carts)):
                if ii == jj or ii in crashed_carts or jj in crashed_carts:
                    continue
                if (carts[ii][0][0], carts[ii][0][1]) == (carts[jj][0][0],
                                                          carts[jj][0][1]):
                    print "crash at %d,%d" % (carts[ii][0][1], carts[ii][0][0])

                    # mark for removal
                    crashed_carts.append(ii)
                    crashed_carts.append(jj)

    # remove carts which have crashed
    carts = [carts[i] for i in range(len(carts)) if i not in crashed_carts]
    crashed_carts = []

    if len(carts) == 1:
        print "remaining cart at %d,%d" % (carts[0][0][1], carts[0][0][0])
        break

    # check for change in direction
    for i in range(len(carts)):

        if carts[i][0] in field:
            symbol = field[carts[i][0]]
            x, y = carts[i][0]
            dx, dy = carts[i][1]
            i_count = carts[i][2]

            # if it's intersection, depends on previous crossings
            if symbol == "+":
                turn = i_count % 3
                if turn == 0:
                    newdx, newdy = leftturn[(dx, dy)]
                elif turn == 1:
                    newdx, newdy = dx, dy
                elif turn == 2:
                    newdx, newdy = rightturn[(dx, dy)]

                i_count = i_count + 1

            elif symbol == "/":
                newdx, newdy = -dy, -dx
            elif symbol == "\\":
                newdx, newdy = dy, dx

            carts[i] = ((x, y), (newdx, newdy), i_count)

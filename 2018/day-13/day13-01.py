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


while True:

    # carts are read top to bottom, left to right
    carts = sorted(carts, key=lambda x: (x[0][0], x[0][1]))

    #print_track()

    # advance all carts
    for i in range(len(carts)):
        r, c = carts[i][0]
        dr, dc = carts[i][1]
        i_count = carts[i][2]

        carts[i] = ((r + dr, c + dc), (dr, dc), i_count)

        # check for crash
        for i in range(len(carts)):
            for j in range(len(carts)):
                if i == j:
                    continue
                if (carts[i][0][0], carts[i][0][1]) == (carts[j][0][0],
                                                        carts[j][0][1]):
                    print "crash at %d,%d" % (carts[i][0][1], carts[i][0][0])
                    sys.exit()

    # check for change in direction
    for i in range(len(carts)):
        if carts[i][0] in field:
            symbol = field[carts[i][0]]
            x, y = carts[i][0]
            dr, dc = carts[i][1]
            i_count = carts[i][2]

            # if it's intersection, depends on previous crossings
            if symbol == "+":
                turn = i_count % 3
                if turn == 0:
                    newdr, newdc = leftturn[(dr, dc)]
                elif turn == 1:
                    newdr, newdc = dr, dc
                elif turn == 2:
                    newdr, newdc = rightturn[(dr, dc)]

                i_count = i_count + 1

            elif symbol == "/":
                newdr, newdc = -dc, -dr
            elif symbol == "\\":
                newdr, newdc = dc, dr

            carts[i] = ((x, y), (newdr, newdc), i_count)

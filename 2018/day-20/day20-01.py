#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/20
#

import sys

# set a large enough recursion depth limit (finding the shortest path takes
# more than default value)
sys.setrecursionlimit(5000)

f = open("day20-input.txt")
input = f.read()

#input = "^ENWWW(NEEE|SSE(EE|N))$"
#input = "^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"
#input = "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"
#input = "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"

D = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1),
}

V = {}  # contains (r1,c1,r2,c2) if there's a door between (r1,c1) and (r2,c2)
Q = []  # queue to store the coordinates while parsing input

# starting point
r, c = 0, 0

# parse input
for s in input:

    if s in D:

        dr, dc = D[s]
        nr, nc = r + dr, c + dc

        # door between (r,c) and (nr, nc)
        V[(r, c, nr, nc)] = 1
        V[(nr, nc, r, c)] = 1

        r, c = nr, nc

    elif s == "(":
        Q.append((r, c))
    elif s == "|":  # starts from last stored coordinates
        r, c = Q[-1]
    elif s == ")":
        Q.pop()


# print map
def print_map():

    minr = min([r for r, c, _, _ in V.keys()])
    maxr = max([r for r, c, _, _ in V.keys()])
    minc = min([c for r, c, _, _ in V.keys()])
    maxc = max([c for r, c, _, _ in V.keys()])

    # top wall
    for c in range(minc, maxc + 1):
        sys.stdout.write("##")
    print "#"

    # rest of the map
    for r in range(minr, maxr + 1):
        sys.stdout.write("#")
        for c in range(minc, maxc + 1):
            if r == 0 and c == 0:
                sys.stdout.write("X")
            else:
                if (r, c) in dist:
                    sys.stdout.write(str(dist[(r, c)]))
                else:
                    sys.stdout.write(".")

            if (r, c, r, c + 1) in V:
                sys.stdout.write("|")
            else:
                sys.stdout.write("#")
        print

        for c in range(minc, maxc + 1):
            sys.stdout.write("#")
            if (r, c, r + 1, c) in V:
                sys.stdout.write("-")
            else:
                sys.stdout.write("#")
        print "#"


# (r,c): distance from origin (0,0)
dist = {}

# starting from origin, recurse to find the shortest distance to rooms
def mark_distance(r, c, n):

    for d in D:
        dr, dc = D[d]
        nr, nc = r + dr, c + dc

        if (r, c, nr, nc) in V:
            if (nr, nc) not in dist:
                # room not visited yet
                dist[(nr, nc)] = n + 1
                mark_distance(nr, nc, n + 1)
            else:
                # if the room is already visited, visit again if the new
                # distance is shorter than existing
                if dist[(nr, nc)] > n + 1:
                    dist[(nr, nc)] = n + 1
                    mark_distance(nr, nc, n + 1)


# find shortest distance from origin to rooms
mark_distance(0, 0, 0)

print_map()

print "part 1 =", max(dist.values())
print "part 2 =", len([d for d in dist if dist[d] >= 1000])

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2019/day/6
#

f = open("input.txt")
#f = open("testinput1.txt")
#f = open("testinput2.txt")

# make a dict of parents (parents[child] = parent)
parents = {}

for line in f.readlines():
    p, c = map(lambda x: x.strip(), line.split(")"))
    parents[c] = p

#
# Part 1
#

# count direct / indirect orbits for each node and sum them
total = 0
for node in parents:
    sum = 0
    child = node
    # traverse through parents tree and count
    while child in parents:
        sum += 1
        child = parents[child]

    total += sum

print("Part 1: %d" % total)


#
# Part 2
#

# compute orbit path for both YOU and SAN
you_orbit = ["YOU"]
san_orbit = ["SAN"]

while you_orbit[-1] in parents:
    you_orbit.append(parents[you_orbit[-1]])

while san_orbit[-1] in parents:
    san_orbit.append(parents[san_orbit[-1]])

# remove common portions of the path
while True:
    if you_orbit[-1] == san_orbit[-1]:
        you_orbit.pop()
        san_orbit.pop()
    else:
        break

# the total transfer length is what's left of the tree
# minus YOU and SAN themselves
print("Part 2: %d" % (len(you_orbit) + len(san_orbit) - 2))

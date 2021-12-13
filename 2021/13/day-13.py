#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2021/day/13
#


def read_input():
    co = []
    fo = []
    f = open("input.txt")
    for l in f.readlines():
        if "," in l:
            co.append(tuple(map(int, l.strip().split(","))))
        if "x=" in l:
            fo.append(("x", int(l.strip().split("=")[1])))
        if "y=" in l:
            fo.append(("y", int(l.strip().split("=")[1])))

    return co, fo


def fold_y(c, fold_y):
    cc = []
    for x, y in c:
        if y < fold_y:
            cc.append((x, y))
        else:
            nx, ny = x, fold_y - (y - fold_y)
            if (nx, ny) not in cc:
                cc.append((nx, ny))

    return cc


def fold_x(c, fold_x):
    cc = []
    for x, y in c:
        if x < fold_x:
            cc.append((x, y))
        else:
            nx, ny = fold_x - (x - fold_x), y
            if (nx, ny) not in cc:
                cc.append((nx, ny))
    return cc


def print_grid(cc):
    max_x = max([x for x, _ in cc])
    max_y = max([y for _, y in cc])

    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x, y) in cc:
                print("█", end="")
            else:
                print(" ", end="")
        print()


coord, folds = read_input()

part1 = True
for f, n in folds:
    if f == "x":
        coord = fold_x(coord, n)
    if f == "y":
        coord = fold_y(coord, n)

    if part1:
        print("Part 1: %d" % len(set(coord)))
        part1 = False

print("Part 2:")
print_grid(coord)

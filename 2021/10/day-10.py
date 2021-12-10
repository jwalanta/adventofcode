#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2021/day/10
#


def read_input():
    f = open("input.txt")
    return [l.strip() for l in f.readlines()]


pairs = {"(": ")", "{": "}", "[": "]", "<": ">"}


def parse1(l):

    costs = {")": 3, "]": 57, "}": 1197, ">": 25137}

    s = []
    for c in l:
        if c in pairs:
            s.append(c)
        else:
            if pairs[s[-1]] == c:
                s = s[0:-1]
            else:
                # print("Expected", pairs[s[-1]], "found", c)
                return costs[c]
    return 0


def part1():
    sum = 0
    for l in input:
        sum = sum + parse1(l)
    return sum


def parse2(l):

    costs = {"(": 1, "[": 2, "{": 3, "<": 4}

    s = []
    for c in l:
        if c in pairs:
            s.append(c)
        else:
            if pairs[s[-1]] == c:
                s = s[0:-1]
            else:
                # corrupted
                return 0

    sum = 0
    for c in reversed(s):
        sum = sum * 5 + costs[c]

    return sum


def part1():
    sum = 0
    for l in input:
        sum = sum + parse1(l)
    return sum


def part2():
    scores = []
    for l in input:
        score = parse2(l)
        if score > 0:
            scores.append(score)

    scores = sorted(scores)
    return scores[int(len(scores) / 2)]


input = read_input()
print("Part 1: %d" % part1())
print("Part 2: %d" % part2())

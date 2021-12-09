#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2021/day/8
#

from collections import Counter

segment_number = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def read_input():
    f = open("input.txt")
    return [tuple(l.strip().split(" | ")) for l in f.readlines()]


def part1():
    count = 0
    for _, o in input:
        for d in o.split(" "):
            if len(d) in (2, 3, 4, 7):
                count = count + 1
    return count


def deduce(line):

    #  aaaa
    # b    c
    # b    c
    #  dddd
    # e    f
    # e    f
    #  gggg

    #
    # possible values initially
    bars = {
        "a": set("abcdefg"),
        "b": set("abcdefg"),
        "c": set("abcdefg"),
        "d": set("abcdefg"),
        "e": set("abcdefg"),
        "f": set("abcdefg"),
        "g": set("abcdefg"),
    }

    signals = line.split(" ")

    # 1 has c and f turned on
    b1 = [set(s) for s in signals if len(s) == 2][0]

    # remove possible values for c & f from the rest
    for k in bars:
        bars[k] = bars[k] - b1

    # possible values for c & f
    bars["c"] = b1
    bars["f"] = b1

    # 7 has a, c & f turned on
    b7 = [set(s) for s in signals if len(s) == 3][0]
    pos_a = b7 - bars["c"]  # only one possible value for a
    for k in bars:
        bars[k] = bars[k] - pos_a
    bars["a"] = pos_a

    # 4 has b, c, d & f turned on
    b4 = [set(s) for s in signals if len(s) == 4][0]
    pos_bd = (b4 - bars["c"])
    for k in bars:
        bars[k] = bars[k] - pos_bd
    bars["b"] = pos_bd
    bars["d"] = pos_bd

    # 0 6 9 have six segments
    # 2 3 5 have five segments

    # >>> Counter(list("acdeg"+"acdfg"+"abdfg"))
    # Counter({'a': 3, 'd': 3, 'g': 3, 'c': 2, 'f': 2, 'e': 1, 'b': 1})
    # >>> Counter(list("abcefg"+"abdefg"+"abcdfg"))
    # Counter({'a': 3, 'b': 3, 'f': 3, 'g': 3, 'c': 2, 'e': 2, 'd': 2})

    #
    five = "".join([s for s in signals if len(s) == 5])
    five_count = Counter(list(five))

    six = "".join([s for s in signals if len(s) == 6])
    six_count = Counter(list(six))

    # a and g are 3 in both
    g = ""
    for k1 in five_count:
        for k2 in six_count:
            if k1 == k2 and five_count[k1] == six_count[k2] and five_count[k1] == 3 and set(k1) != bars["a"]:
                g = k1
    for k in bars:
        bars[k] = bars[k] - set(g)
    bars["g"] = set(g)

    # c and f are 2 in both
    c = ""
    for k1 in five_count:
        for k2 in six_count:
            if k1 == k2 and five_count[k1] == six_count[k2] and five_count[k1] == 2:
                c = k1
    for k in bars:
        bars[k] = bars[k] - set(c)
    bars["c"] = set(c)

    # b is 1 in five bars, 3 in six bars
    # d is 3 in five bars, 2 in six bars
    x, y = bars["b"]
    if five_count[x] == 1:
        b = x
        d = y
    else:
        b = y
        d = x

    bars["b"] = set(b)
    bars["d"] = set(d)

    return {''.join(bars[k]): k for k in bars}


def convert(m, num):
    number = ""
    for n in num:
        number = number + m[n]

    number = ''.join(sorted(number))
    return segment_number[number]


def part2():
    sum = 0
    for i in input:
        signals, nums = i
        m = deduce(signals)

        number = 0
        for num in nums.split(" "):
            number = number * 10 + convert(m, num)

        sum = sum + number

    return sum


input = read_input()

print("Part 1: %d" % part1())
print("Part 2: %d" % part2())

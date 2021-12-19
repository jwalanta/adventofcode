#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2021/day/18
#

def read_input():
    f = open("input.txt")
    return list([line_to_list(l.strip()) for l in f.readlines()])


def line_to_list(line):
    l = []
    for c in line:
        l.append(int(c) if c >= "0" and c <= "9" else c)
    return l


def list_to_line(l):
    return "".join(map(str, l))


def add_pairs(p1, p2):
    sum = ["["] + p1 + [","] + p2 + ["]"]
    return sum


def explode(p):
    b = {"[": 1, "]": -1}
    n = 0

    for i in range(len(p)):
        n += b[p[i]] if p[i] in b else 0

        if n == 5:  # nested 4 deep
            # check if exact number pair exists
            left, comma, right = p[i+1], p[i+2], p[i+3]

            if isinstance(left, int) and comma == "," and isinstance(right, int):
                newp = p[0:i] + [0] + p[i+5:]
                # add left
                for j in range(i-1, 0, -1):
                    if isinstance(newp[j], int):
                        newp[j] += left
                        break

                # add right
                for j in range(i+1, len(newp)):
                    if isinstance(newp[j], int):
                        newp[j] += right
                        break

                return newp, True

    return p, False


def split(p):
    for i in range(len(p)):
        if isinstance(p[i], int) and p[i] > 9:
            left = p[i] // 2
            right = p[i] - left
            return p[0:i] + ["[", left, ",", right, "]"] + p[i+1:], True
    return p, False


def explode_and_split(l):
    while True:
        e, eb = explode(l)
        # print("After explode: ", "".join(map(str, e)))
        if eb:
            l = e
            continue

        s, sb = split(e)
        # print("After split: ", "".join(map(str, s)))
        l = s
        if eb == False and sb == False:
            break

    return l


def find_magnitude(l):
    if len(l) == 1:
        return l[0]

    b = {"[": 1, "]": -1}

    # find center comma
    n = 0
    for i in range(1, len(l)):
        n += b[l[i]] if l[i] in b else 0
        if n == 0 and l[i] == ",":
            return 3 * find_magnitude(l[1:i]) + 2 * find_magnitude(l[i+1:len(l)-1])


# read input
snailfish_numbers = read_input()


#
# part 1
#
snailfish_number = snailfish_numbers[0]
for i in range(1, len(snailfish_numbers)):
    # print("   ", list_to_line(snailfish_number))
    # print(" + ", list_to_line(snailfish_numbers[i]))

    snailfish_number = add_pairs(snailfish_number, snailfish_numbers[i])
    snailfish_number = explode_and_split(snailfish_number)

    # print(" = ", list_to_line(snailfish_number))
    # print()


print("Part 1: %d" % find_magnitude(snailfish_number))


# 
# part 2
#
max = 0
for i in range(len(snailfish_numbers)):
    for j in range(len(snailfish_numbers)):
        if i == j:
            continue

        snailfish_number = add_pairs(
            snailfish_numbers[i], snailfish_numbers[j])
        snailfish_number = explode_and_split(snailfish_number)
        sum = find_magnitude(snailfish_number)

        max = sum if sum > max else max

print("Part 2: %d" % max)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/9
#


def score(s):

    i = 0
    level = 0
    sum = 0
    while i < len(s):
        if s[i] == "{":
            level += 1
            sum += level
        elif s[i] == "}":
            level -= 1
        elif s[i] == "!":
            i += 1  # ignore next
        elif s[i] == "<":
            while s[i] != ">":
                if s[i] == "!":
                    i += 1  # ignore next
                i += 1
        i += 1

    return sum

assert score("{}") == 1
assert score("{{{}}}") == 6
assert score("{{},{}}") == 5
assert score("{{{},{},{{}}}}") == 16
assert score("{<a>,<a>,<a>,<a>}") == 1
assert score("{{<ab>},{<ab>},{<ab>},{<ab>}}") == 9
assert score("{{<!!>},{<!!>},{<!!>},{<!!>}}") == 9
assert score("{{<a!>},{<a!>},{<a!>},{<ab>}}") == 3

f = open("day9-input.txt")
s = f.read()
print score(s)

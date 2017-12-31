#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/9
#


def score(s):

    i = 0
    level = 0
    sum = 0
    garbage = 0

    while i < len(s):
        if s[i] == "{":
            level += 1
            sum += level
        elif s[i] == "}":
            level -= 1
        elif s[i] == "!":
            i += 1  # ignore next
        elif s[i] == "<":
            i += 1
            while s[i] != ">":
                if s[i] == "!":
                    i += 1  # ignore next
                    garbage -= 1  # ignore "!" from garbage count
                i += 1
                garbage += 1
        i += 1

    return (sum, garbage)

assert score("{}") == (1, 0)
assert score("{{{}}}") == (6, 0)
assert score("{{},{}}") == (5, 0)
assert score("{{{},{},{{}}}}") == (16, 0)
assert score("{<a>,<a>,<a>,<a>}") == (1, 4)
assert score("{{<ab>},{<ab>},{<ab>},{<ab>}}") == (9, 8)
assert score("{{<!!>},{<!!>},{<!!>},{<!!>}}") == (9, 0)
assert score("{{<a!>},{<a!>},{<a!>},{<ab>}}") == (3, 17)

f = open("day9-input.txt")
s = f.read()
print "Total, Garbage =", score(s)

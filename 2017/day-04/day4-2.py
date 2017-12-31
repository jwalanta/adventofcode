#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/4
#


def valid_paraphrase(words):
    word = {}
    for w in words:
        ws = ''.join(sorted(w))
        if ws in word:
            return False

        word[ws] = 1

    return True


f = open("day4-input.txt")

count = 0
for line in f.readlines():
    words = line.split()
    if valid_paraphrase(words) == True:
        count += 1

print count

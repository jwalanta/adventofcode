#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/4
#

import re

f = open("day04-input.txt")
lines = sorted(f.read().split("\n")) # sorted by time

# format: {id: [array of len 60, total sleeps each minute for the id]}
sleepy_time = {}

for line in lines:
    day, hr, mn, txt = re.findall("\[(.*) (.*):(.*)\] (.*)", line)[0]

    mn = int(mn)
    if "falls asleep" in txt:
        sleep_min = mn
    elif "wakes up" in txt:
        # sum up sleep status for each minute
        for m in range(sleep_min, mn):
            sleepy_time[id][m] = sleepy_time[id][m] + 1
    else:
        id = int(re.findall("Guard #([0-9]+) ", txt)[0])
        if id not in sleepy_time:
            sleepy_time[id] = [0 for i in range(60)]


# find guard who slept the most
# (sum the minutes, return the key with highest sum)
id = max(sleepy_time, key=lambda k: sum(sleepy_time[k]))

# minute when the guard slept the most
max_min = sleepy_time[id].index(max(sleepy_time[id]))

print id * max_min


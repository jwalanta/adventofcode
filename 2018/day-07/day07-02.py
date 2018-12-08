#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/7
#

from collections import defaultdict

f = open("day07-input.txt")
lines = f.read().split("\n")

dep = defaultdict(list)
letters = set([])

for l in lines:
    p = l.split(" ")
    dep[p[7]].append(p[1])
    letters.add(p[1])
    letters.add(p[7])


total_workers = 5
workers = [("",0) for i in range(total_workers)]
completed = []
total_time = 0

# can t be done next (based on completed tasks)
def can_be_done_next(t):

    # if t has no dependency
    if t not in dep:
        return True

    # check if all dependency completed
    for d in dep[t]:
        if d not in completed:
            return False

    return True


# find next availble slot in workers
def find_available_slot():
    for i in range(len(workers)):
        if workers[i][1] == 0:
            return i
    
    return None

# fill worker slots with next available task
def fill_workers():

    # find tasks that be done next
    for s in sorted(letters):

        slot = find_available_slot()
        if slot == None:
            break
        
        # find next available task and put in worker slot
        if can_be_done_next(s):
            workers[slot] = (s, 60+ord(s)-64)
            letters.remove(s)


# remove the quickest task and add time to total
def do_task():
    global total_time
    
    # find the task taking least time
    running_works = [(k,v) for k,v in workers if v!=0]
    running_works = sorted(running_works, key=lambda l: l[1])

    least = running_works[0]
    total_time = total_time + least[1]

    for i in range(len(workers)):
        if workers[i][1] > 0:
            workers[i] = (workers[i][0], workers[i][1] - least[1])
            if workers[i][1] == 0:
                completed.append(workers[i][0])


while letters:
    fill_workers()
    do_task()

print total_time




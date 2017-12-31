#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/24
#

components = open("day24-input.txt").read().strip().split("\n")
max_length = 0
max_sum = 0


def get_components_with(x, exclude_list):
    matches = []
    for c in components:
        if c in exclude_list:
            continue
        a, b = c.split("/")
        if a == x or b == x:
            matches.append(c)
    return matches


def find_end_port(bridge):
    ports = {"0": 1}

    # go through all ports in components
    # create if doesnt, delete if exists
    # at the end, the port without connection remains
    for c in bridge:
        a, b = c.split("/")
        if a in ports:
            del ports[a]
        else:
            ports[a] = 1

        if b in ports:
            del ports[b]
        else:
            ports[b] = 1

    return ports.keys()[0]


def next_possible_components(current_list):
    if len(current_list) == 0:
        return get_components_with("0", current_list)
    else:
        return get_components_with(find_end_port(current_list), current_list)


def bridge_compute_strength(bridge):
    global max_sum
    global max_length

    sum = 0
    for c in bridge:
        a, b = c.split("/")
        sum += int(a)
        sum += int(b)

    # print len(bridge) , sum

    if len(bridge) > max_length:
        max_length = len(bridge)
        max_sum = sum
    elif len(bridge) == max_length:
        if sum > max_sum:
            max_length = len(bridge)
            max_sum = sum


def find_valid_bridges(bridge):

    if len(bridge):
        bridge_compute_strength(bridge)

    next_components = next_possible_components(bridge)
    if len(next_components) == 0:
        return

    for c in next_components:
        bridge.append(c)
        find_valid_bridges(bridge)
        bridge.pop()


print "Computing.."

find_valid_bridges([])

print "Strength of longest bridge:", max_sum

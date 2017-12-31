#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/7
#

import re

f = open("day7-input.txt")
#f = open("day7-testinput.txt")

node_weight = {}
node_parent = {}
node_children = {}

# create tree
for line in f:
    name, weight, children_str = re.findall(r'(\w+) \((\d+)\)(.*)', line)[0]
    children = re.findall(r'([a-z]+)', children_str)

    node_weight[name] = int(weight)
    node_children[name] = children

    for c in children:
        node_parent[c] = name

# find root
root = ""
for n in node_weight:
    if n not in node_parent:
        root = n
        break

print "Root:", root

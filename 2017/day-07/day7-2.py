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


def find_weight(n):
    sum = node_weight[n]
    for c in node_children[n]:
        sum += find_weight(c)
    return sum


def find_unbalanced_node(node, weight_difference=0):
    weight = {}
    for n in node_children[node]:
        w = find_weight(n)

        if w not in weight:
            weight[w] = [n]
        else:
            weight[w].append(n)

    print weight, len(weight)

    if len(weight) == 1:
        print "\nUnbalanced node =", node
        print "Final weight =", node_weight[node] - weight_difference
        return

    # find unbalanced weight and dig in
    for w in weight:
        if len(weight[w]) == 1:
            print "Digging into", weight[w][0], "(", node_weight[weight[w][0]], ")"
            find_unbalanced_node(weight[w][0], abs(
                weight.keys()[0] - weight.keys()[1]))


print "\nFinding unbalanced nodes"
find_unbalanced_node(root)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2019/day/8
#

input = open("input.txt").read().strip()

# 25 pixels wide and 6 pixels tall
layer_length = 25 * 6

#
# Part 1
#
min_zero = len(input)
min_layer = ""
for st in range(0, len(input), layer_length):
    layer = input[st:st+layer_length]
    count = layer.count("0")
    if count < min_zero:
        min_zero = count
        min_layer = layer

print("Part 1: %d" % (min_layer.count("1") * min_layer.count("2")))


#
# Part 2
#
def merge(top, bottom):
    result = ""
    for i in range(0, len(top)):
        result += top[i] if top[i] == "0" or top[i] == "1" else bottom[i]
    return result


# merge layers
merged_layer = "2" * layer_length  # all transparent initial layer
for st in range(0, len(input), layer_length):
    merged_layer = merge(merged_layer, input[st:st+layer_length])

# print
print("Part 2:")
merged_layer = merged_layer.replace("0", " ").replace("1", "#")
for l in range(0, 6):
    print(merged_layer[l*25:(l+1)*25])

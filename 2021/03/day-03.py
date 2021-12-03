#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2021/day/3
#

def read_input():
    f = open("input.txt")
    return [l.strip() for l in f.readlines()]

lines = read_input()

def part1():
    l = len(lines[0])
    count = [0] * l

    for n in lines:
        for i in range(l):
            count[i] = count[i] + (1 if n[i] == '1' else -1)

    gamma = ''.join(['1' if c > 0 else '0' for c in count])
    epsilon = ''.join(['0' if c == '1' else '1' for c in gamma])

    return int(gamma, 2) * int(epsilon, 2)


def part2():

    # oxygen
    nums = lines.copy()
    for i in range(len(nums[0])):
        ones, zeroes = count_at_pos(nums, i)
        most_common_bit = '1' if ones >= zeroes else '0'
        keep = []
        for n in range(len(nums)):
            if nums[n][i] == most_common_bit:
                keep.append(nums[n])
        
        # remaining
        nums = keep

        if len(nums) == 1:
            break

    o2_rating = int(nums[0], 2)

    # co2
    nums = lines.copy()
    for i in range(len(nums[0])):
        ones, zeroes = count_at_pos(nums, i)
        most_common_bit = '0' if zeroes <= ones else '1'
        keep = []
        for n in range(len(nums)):
            if nums[n][i] == most_common_bit:
                keep.append(nums[n])
        
        # remaining
        nums = keep

        if len(nums) == 1:
            break

    co2_rating = int(nums[0], 2)

    return o2_rating * co2_rating


def count_at_pos(nums, pos):
    ones, zeroes = 0, 0
    for i in range(len(nums)):
        ones = ones + (1 if nums[i][pos] == '1' else 0)
        zeroes = zeroes + (1 if nums[i][pos] == '0' else 0)

    return (ones, zeroes)


print("Part 1: %d" % part1())
print("Part 2: %d" % part2())
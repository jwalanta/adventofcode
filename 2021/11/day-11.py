#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2021/day/11
#

import time
from os import system

def read_input():
    f = open("input.txt")
    return [list(map(int, list(l.strip()))) for l in f.readlines()]


def print_levels(step, levels):
    system('clear')
    print("Step: ", step)
    print()
    for x in range(len(levels[0])):
        for y in range(len(levels)):
            if levels[x][y] == 0:
                print("\x1b[1m"+str(levels[x][y])+"\x1b[0m", end=" ")
            else:
                print(levels[x][y], end=" ")
        print()
    print()
    time.sleep(0.05)


def run():
    total_flash = 0
    total_flashes_at_100 = 0
    simultaneous_flash_at = 0
    step = 0

    while True:
        step = step + 1

        # increase by 1
        for x in range(len(levels[0])):
            for y in range(len(levels)):
                levels[x][y] = levels[x][y] + 1

        # flash
        flashed = []
        to_flash = [(x, y) for x in range(len(levels[0]))
                    for y in range(len(levels)) if levels[x][y] > 9]

        while len(to_flash) > 0:
            x, y = to_flash.pop()
            if (x, y) in flashed:
                continue

            flashed.append((x, y))
            levels[x][y] = 0

            # increase surroundings
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= len(levels[0]) or ny >= len(levels):
                    continue
                levels[nx][ny] = levels[nx][ny] + 1
                if levels[nx][ny] > 9:
                    to_flash.append((nx, ny))

        for x, y in flashed:
            levels[x][y] = 0

        total_flash = total_flash + len(flashed)

        # print_levels(step, levels)

        if step == 100:
            total_flashes_at_100 = total_flash

        if len(flashed) == 100:
            simultaneous_flash_at = step
            break

    return (total_flashes_at_100, simultaneous_flash_at)


levels = read_input()

total_flash, simultaneous_flash_at = run()

print("Part 1: %d" % total_flash)
print("Part 2: %d" % simultaneous_flash_at)

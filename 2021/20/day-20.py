#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2021/day/20
#


from collections import defaultdict


def read_input():
    f = open("input.txt")

    algorithm_lines, imgage_lines = f.read().split("\n\n")
    algorithm = "".join([a.strip() for a in algorithm_lines])

    img = imgage_lines.split("\n")
    image = defaultdict(int)
    for y in range(len(img)):
        for x in range(len(img[0])):
            image[(y, x)] = 1 if img[x][y] == "#" else 0

    return algorithm, image


def min_max(image):
    minx = min([x for x, _ in image])
    maxx = max([x for x, _ in image])
    miny = min([y for _, y in image])
    maxy = max([y for _, y in image])
    return minx, maxx, miny, maxy


def print_image(image):
    minx, maxx, miny, maxy = min_max(image)
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            print("#" if image[(x, y)] == 1 else ".", end="")
        print()


def enhance(algorithm, image, step):
    minx, maxx, miny, maxy = min_max(image)
    enhanced_image = defaultdict(int)
    delta = [(-1, -1), (0, -1), (1, -1), (-1, 0),
             (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    for y in range(miny-1, maxy+2):
        for x in range(minx-1, maxx+2):
            enhancement_str = ""
            for dx, dy in delta:
                nx, ny = x+dx, y+dy

                if (nx, ny) in image:
                    enhancement_str += str(image[(nx, ny)])
                else:
                    enhancement_str += "1" if step % 2 == 1 else "0"

                i = int(enhancement_str, 2)
                enhanced_image[(x, y)] = 1 if algorithm[i] == "#" else 0

    return enhanced_image


algorithm, image = read_input()

for i in range(50):
    image = enhance(algorithm, image, i)
    # print_image(image)
    if i == 1:
        print("Part 1: %d" % sum(image.values()))


print("Part 2: %d" % sum(image.values()))

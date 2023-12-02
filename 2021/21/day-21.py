#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2021/day/21
#

def read_input():
    f = open("input.txt")
    return int(f.readline().split(" ")[-1]) - 1, int(f.readline().split(" ")[-1]) - 1

player_position = list(read_input())
player_score = [0, 0]
die = 0
die_rolls = 0

def roll_dice():
    global die, die_rolls
    a, b, c = (die + 0) % 100, (die + 1) % 100, (die + 2) % 100
    die = (die + 3) % 100
    die_rolls += 3
    return a + b + c

player_turn = 0

while True:
    n = roll_dice() + 3
    player_position[player_turn] = (player_position[player_turn] + n) % 10
    player_score[player_turn] += (player_position[player_turn] + 1)

    #print(player_turn + 1, player_position[player_turn], player_score[player_turn])

    if player_score[player_turn] >= 1000:
        player_turn = 1 if player_turn == 0 else 0
        break

    player_turn = 1 if player_turn == 0 else 0


print("Part 1: %d" % (player_score[player_turn] *  die_rolls))








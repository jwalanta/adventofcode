#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2021/day/3
#

nums = []
boards = []

def read_input():
    f = open("input.txt")
    for n in f.readline().split(","):
        nums.append(int(n))

    board = []
    for l in f.readlines():
        if l.strip() == "":
            continue

        board = board + [(int(n), False) for n in l.split(" ") if n != '']

        if len(board) == 25:
            boards.append(board)
            board = []

def mark_match(board, n):
    for i in range(len(board)):
        v, _ = board[i]
        if v == n:
            board[i] = (v, True)

def check_winner(board):
    # horizontal
    for i in range(0,25,5):
        if sum([1 for j in range(i, i+5) if board[j][1]]) == 5:
            return True

    # vertical
    for i in range(5):
        if sum([1 for j in range(i, 25, 5) if board[j][1]]) == 5:
            return True

    return False

def part1():
    for n in nums:
        for board in boards:
            mark_match(board, n)
            if check_winner(board):
                return n * sum([b[0] for b in board if b[1] == False])

def part2():
    # reset board
    for board in boards:
        for b in board:
            b = (b[0], False)

    winning_boards = []
    for n in nums:
        for i in range(len(boards)):
            board = boards[i]
            mark_match(board, n)
            if check_winner(board):
                if i not in winning_boards:
                    winning_boards.append(i)

                if len(winning_boards) == len(boards):
                    return n * sum([b[0] for b in board if b[1] == False])


read_input()

print("Part 1: %d" % part1())
print("Part 2: %d" % part2())
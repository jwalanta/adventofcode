#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/19
#

f = open("day19-input.txt")
lines = f.read().split("\n")

instructions = []
ip = 0

for line in lines:
    if "#ip" in line:
        ip = int(line.split()[1])
    else:
        i = line.split()
        instructions.append((i[0], int(i[1]), int(i[2]), int(i[3])))


# execute instruction on register, return changed register
def execute(register, instruction):
    r = register[:]
    op, a, b, c = instruction

    if op == "addr":
        r[c] = r[a] + r[b]
    elif op == "addi":
        r[c] = r[a] + b

    elif op == "mulr":
        r[c] = r[a] * r[b]
    elif op == "muli":
        r[c] = r[a] * b

    elif op == "banr":
        r[c] = r[a] & r[b]
    elif op == "bani":
        r[c] = r[a] & b

    elif op == "borr":
        r[c] = r[a] | r[b]
    elif op == "bori":
        r[c] = r[a] | b

    elif op == "setr":
        r[c] = r[a]
    elif op == "seti":
        r[c] = a

    elif op == "gtir":
        r[c] = 1 if a > r[b] else 0
    elif op == "gtri":
        r[c] = 1 if r[a] > b else 0
    elif op == "gtrr":
        r[c] = 1 if r[a] > r[b] else 0

    elif op == "eqir":
        r[c] = 1 if a == r[b] else 0
    elif op == "eqri":
        r[c] = 1 if r[a] == b else 0
    elif op == "eqrr":
        r[c] = 1 if r[a] == r[b] else 0
    else:
        print "INVALID OPCODE"

    return r


r = [0,0,0,0,0,0]   # six registers

while r[ip] < len(instructions):

    output = execute(r, instructions[r[ip]])

    # print r[ip], r, instructions[r[ip]], output

    r = output

    # increment instruction pointer
    r[ip] += 1

print r[0]

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/16
#

f = open("day16-input1.txt")
lines = f.read().split("\n")

opcodes = "addr addi mulr muli banr bani borr bori setr seti gtir gtri gtrr eqir eqri eqrr".split()

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


c = 0 # line counter
match_count = 0 # match 
while c < len(lines):
    line = lines[c]
    if "Before" in line:
        register = map(int, line[9:19].split(", "))
        instruction = map(int, lines[c + 1].split())
        output = map(int, lines[c + 2][9:19].split(", "))

        match = 0
        for op in opcodes:
            ins = instruction[:]
            ins[0] = op

            if output == execute(register, ins):
                match = match + 1

        if match >= 3:
            match_count = match_count + 1

        c = c + 3
    else:
        c = c + 1

print match_count

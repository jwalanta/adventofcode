#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/19
#

'''
this will take a long time to solve if the instructions are executed the usual
way. upon inspection of the register and instruction state, it loops from
instruction 3 to 11. upon further inspection of the instructions, there's a
loop between instruction 1 and 15.

 1 seti 1 2 5
 2 seti 1 3 2
 3 mulr 5 2 1
 4 eqrr 1 4 1
 5 addr 1 3 3
 6 addi 3 1 3
 7 addr 5 0 0
 8 addi 2 1 2
 9 gtrr 2 4 1
10 addr 3 1 3
11 seti 2 5 3
12 addi 5 1 5
13 gtrr 5 4 1
14 addr 1 3 3
15 seti 1 2 3

indenting the loop:

01: r5 = 1
    02: r2 = 1
        03: r1 = r5 * r2
        04: r1 = 1 if r1==r4 else 0
        05: r3 = r3 + r1
        06: r3++
        07: r0 = r5 + r0
        08: r2++
        09: r1 = 1 if r2 > r4 else 0
        10: r3 = r3 + r1
        11: jump to 2+1=3
    12: r5++
    13: r1 = 1 if r5 > r4 else 0
    14: r3 = r3 + r1
    15: jump 1+1 = 2

converting this to C-like syntax:

r5 = 1
do {
    r2 = 1
    do {
        if (r2 * r5 == r4){
            r0 += r5
        }
        r2++
    } while (r2 <= r4)
    r5++
} while (r5 <= r4)

what this is doing is finding the factors of the number stored in register 4.
r2 and r5 loop for range 1 to r4, and the check r2 * r5 == r4 is to see if r5
is the factor. if it's a factor, the number is stored in r0. so at the end of
the loop, r0 will contain the sum of factors of number in r4.

we can rewrite this (sum of factors) as:

for n in range(1, r[4]+1):
    if r[4] % n == 0:
        r[0] += n

'''

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


r = [1,0,0,0,0,0]   # six registers

while r[ip] < len(instructions):

    if r[ip] == 1:

        # re-written optimized version of the loop
        # finds sum of factors of value in r[4]
        for n in range(1, r[4]+1):
            if r[4] % n == 0:
                r[0] += n
                # print n, r

        r[ip]  = 15

    else:

        output = execute(r, instructions[r[ip]])

        # print r[ip], r, instructions[r[ip]], output

        r = output

    # increment instruction pointer
    r[ip] += 1

print r[0]
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/25
#

# "STATE": [(value, delta, next_state),(value, delta, next_state)]
states = {
    "A": [(1, 1, "B"), (0, -1, "C")],
    "B": [(1, -1, "A"), (1, 1, "D")],
    "C": [(1, 1, "A"), (0, -1, "E")],
    "D": [(1, 1, "A"), (0, 1, "B")],
    "E": [(1, -1, "F"), (1, -1, "C")],
    "F": [(1, 1, "D"), (1, 1, "A")]
}

state = "A"
pointer = 0
tape = {}

steps = 12173597

for x in xrange(steps):
    if pointer not in tape:
        tape[pointer] = 0

    value, delta, next_state = states[state][tape[pointer]]

    tape[pointer] = value
    pointer += delta
    state = next_state

# checksum
checksum = 0
for k in tape:
    checksum += tape[k]

print checksum

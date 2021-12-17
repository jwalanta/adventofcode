#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2021/day/16
#

import math


def read_input():
    f = open("input.txt")
    return f.readline()


def hex2bin(s):
    return "".join(bin(int(c, 16))[2:].zfill(4) for c in s)


def bin2dec(s):
    return int(s, 2)


class BITS:

    def __init__(self, hex_input):
        self.pointer = 0
        self.packet = hex2bin(hex_input)
        self.version_total = 0

    def read_header(self):
        version = bin2dec(self.packet[self.pointer:self.pointer+3])
        type_id = bin2dec(self.packet[self.pointer+3:self.pointer+6])

        self.pointer += 6
        self.version_total += version

        return version, type_id

    def parse_literal(self):
        bin_value, prefix = "", ""
        while prefix != "0":
            prefix = self.packet[self.pointer]
            bin_value += self.packet[self.pointer+1:self.pointer+5]
            self.pointer += 5

        return bin2dec(bin_value)

    def calculate(self, type_id, values):
        if type_id == 0:
            return sum(values)
        elif type_id == 1:
            return math.prod(values)
        elif type_id == 2:
            return min(values)
        elif type_id == 3:
            return max(values)
        elif type_id == 5:
            return 1 if values[0] > values[1] else 0
        elif type_id == 6:
            return 1 if values[0] < values[1] else 0
        elif type_id == 7:
            return 1 if values[0] == values[1] else 0

    def parse(self):
        if self.pointer + 6 >= len(self.packet):
            return

        version, type_id = self.read_header()

        if type_id == 4:
            return self.parse_literal()
        else:
            i = self.packet[self.pointer]
            self.pointer += 1
            values = []
            if i == "0":
                total_length = bin2dec(
                    self.packet[self.pointer:self.pointer+15])
                self.pointer += 15
                en = self.pointer + total_length
                while self.pointer < en:
                    v = self.parse()
                    if v is not None:
                        values.append(v)

            else:
                total_sub_packets = bin2dec(
                    self.packet[self.pointer:self.pointer + 11])
                self.pointer += 11
                for _ in range(total_sub_packets):
                    v = self.parse()
                    if v is not None:
                        values.append(v)

            return self.calculate(type_id, values)

    def get_version_total(self):
        return self.version_total


input = read_input()

bits = BITS(input)
value = bits.parse()
print("Part 1: %d" % bits.get_version_total())
print("Part 2: %d" % value)

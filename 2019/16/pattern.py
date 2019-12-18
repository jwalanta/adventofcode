#!/usr/bin/env python3
# -*- coding: utf-8 -*-

base = ["  ","+ ","  ","- "]

print("  ", end="")
for n in range(35):
    print("%2d" % ((n+1)%10), end = "")
print()
for n in range(35):
    print("%2d " % (n+1), end = "")
    for o in range(35):
        m = base[((o+1)//(n+1)) % 4]
        print(m, end="")
    print()
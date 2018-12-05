#!/usr/bin/python

import sys

l = list()
with open('../adventofcode/problems/problem1.input') as f:
    l = map(int, f.readlines())

seen = set()
seen.add(0)
s = 0
i = 0
length = len(l)
while True:
    if i >= length:
        i = 0

    s += l[i]
    i += 1
    print(s)
    if s in seen:
        print(s)
        sys.exit(1)
    seen.add(s)

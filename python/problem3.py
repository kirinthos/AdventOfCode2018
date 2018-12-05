#!/usr/bin/python

from itertools import combinations, islice

from lib import flatten, take, rowprint, readProblem

l = readProblem('../adventofcode/problems/problem3.input')

def parse(s):
    n = s.split('@')
    p = n[1].strip().split(':')
    l = map(int, flatten([p[0].split(','), p[1].split('x')]))
    return [l[0], l[1], l[2] + l[0], l[3] + l[1]]

rects = map(parse, l)

# go through each pair of rectangles
# calculate overlapping rectangle
# sum area of all of these rects
# calcaulate overlapping area of each of these rects and subtract it

# failed
def intersects(rs):
    (r1, r2) = rs
    return not (r1[0] > r2[2] or r1[2] < r2[0] or r1[1] > r2[3] or r1[3] < r2[1])

def overlap(rs):
    z = zip(*rs)
    return [max(*z[0]), max(*z[1]), min(*z[2]), min(*z[3])]

def area(r):
    return (r[2] - r[0]) * (r[3] - r[1])

def mapoverlaps(rs):
    return map(overlap, filter(intersects, combinations(rs, 2)))

os = mapoverlaps(rects)
total = sum(map(area, os))

osoverlaps = mapoverlaps(os)
ostotal = sum(map(area, osoverlaps))
#print(total, ostotal, total - ostotal)

#end failed

print('new section')
(maxX, maxY) = reduce(lambda acc, x: (max(x[2], acc[0]), max(x[3], acc[1])), rects, (0, 0))
grid = [ ['.'] * (maxX + 1) for i in range(maxY + 10) ]

print('grid size', maxX, maxY)

def fill(g, r):
    for y in range(r[1], r[3]):
        for x in range(r[0], r[2]):
            g[y][x] = '-' if g[y][x] == '.' else 'x'

for r in rects:
    fill(grid, r)

#rowprint(grid)
print(len(filter(lambda x: x == 'x', flatten(grid))))

# part 2
def check(rs, j):
    for i in range(len(rs)):
        if i == j:
            continue
        if intersects((rs[i], rs[j])):
            return False
    return True
for i in range(len(rects)):
    if check(rects, i):
        print(rects[i], i+1)
        break

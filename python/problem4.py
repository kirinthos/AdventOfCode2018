#!/usr/bin/python

import itertools, re, sys

from lib import readProblem, take, rowprint, partitionP, flatMap, flatten, group, writeFile, rowstr, groupP, partition

lines = readProblem('../adventofcode/problems/problem4.input')

extractorPattern = re.compile(r'\[....-(..)-(..) (..):(..)\] (.*)')
guardBeginPattern = re.compile(r'.*Guard #(\d+) begins.*')
guardEndTag = 'AAAAA'
guardEndPattern = re.compile(guardEndTag)

# creates (monthday, minute, 'status')
def assemble(l):
    m = extractorPattern.match(l)
    g = m.groups()
    hour = int(g[2] + g[3]) if g[2] == '00' else 0
    l = [(int(g[0] + g[1]), hour, g[4])]
    if guardBeginPattern.match(g[4]):
        l.append((int(g[0] + g[1]), hour, g[4].replace('begins', guardEndTag)))
    return l

# creates (guard number, [shift...])
def splitNumber(r):
    g = guardBeginPattern.match(r[0][2])
    n = int(g.groups()[0])
    return (n, r)

# assmelbe the lines, then group them into shifts
shifts = map(splitNumber, partitionP(lambda x: guardBeginPattern.match(x[2]), sorted(flatMap(assemble, lines))))

# group shift into times when the fall asleep
def translateShift(s):
    return partitionP(lambda x: x[2].find('asleep') > -1, s)

# extract the guard number and group the shift into lists where a[0] is the asleep start
translatedShifts = filter(lambda x: x[1], map(lambda x: (x[0], translateShift(x[1])), shifts))

# take a[0] and a[1] elements and turn them into a range, multiple if spans over a day
def rangify(r):
    def internal(a):
        if a[0][0] == a[1][0]: # same day
            return [ range(a[0][1], a[1][1]) ]
        else:
            print('overday', r)
            return [ range(a[0][1], 60), range(0, a[1][1]) ]
    return flatMap(internal, r)

# expand all shift items into ranges describing each minute
ranges = groupP(lambda p, n: p[0] == n[0], 
    sorted(
        map(lambda x: (x[0], flatten(rangify(x[1]))),
            translatedShifts),
        key=lambda x: x[0]
    )
)

# merges [ (id, [range]), ... ] collections into (id, [range1, range2, ...])
def merge(r):
    def internal(acc, n):
        return (n[0], acc[1] + n[1])
    return reduce(internal, r, (0, []))

mergedRanges = map(lambda x: (x[0], sorted(x[1])), map(merge, ranges))

lenRanges = map(lambda x: (x[0], len(x[1])), mergedRanges)

sleeper = max(mergedRanges, key=lambda x: len(x[1]))
#print('longest sleeper', sleeper)

longestSlept = max(group(sleeper[1]), key=len)[0]
#print('longest minute slept', longestSlept)

#print('answer', int(sleeper[0]) * longestSlept)


# yeah apparently i read too much into this
# .... fuck...alright read the file, sort the lines
sortedLines = sorted(lines)
partitionLines = partitionP(lambda x: guardBeginPattern.match(x), sortedLines)

# create a list of (id, [ asleep, wakes, asleep, wakes ])
def convert(r):
    def internal(e):
        m = extractorPattern.match(e)
        return int(m.groups()[3])
    print(r)
    i = int(guardBeginPattern.match(r[0]).groups()[0])
    print(r[1:])
    l = map(internal, r[1:])
    return (i, flatten(map(lambda x: range(x[0], x[1]), partition(2, l))))

converted = sorted(map(convert, partitionLines))

grouped = groupP(lambda p, n: p[0] == n[0], converted)

merged = map(merge, grouped)

sleeper = max(merged, key=lambda x: len(x[1]))
print(sleeper)

slept = max(group(sorted(sleeper[1])), key=len)
print(slept)

# part 2, highest frequency minute slept, per guard

mergedClean = filter(lambda x: x[1], merged)
longestSleptMinutes = map(lambda x: (x[0], max(group(sorted(x[1])), key=len)), mergedClean)

print('frequent sleeper', max(longestSleptMinutes, key=lambda x: len(x[1])))

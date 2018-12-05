
from itertools import islice

def rowstr(t):
    s = '[\n'
    for i in t:
        s += '\t' + str(i) + '\n'
    s += ']\n'
    return s

def rowprint(t, n=0):
    print
    if n > 0:
        t = take(n, t)
    print(rowstr(t))
    print

def readProblem(name):
    l = None
    with open(name, 'r') as f:
        l = f.readlines()
    return l

def writeFile(name, txt):
    with open(name, 'w') as f:
        f.writelines(txt)

def take(n, i):
    return list(islice(i, n))

def flatten(l):
    return [item for sl in l for item in sl]

def group(ls):
    def internal(acc, n):
        if acc and acc[-1][0] == n:
            acc[-1].append(n)
        else:
            acc.append([n])
        return acc
    return reduce(internal, ls, [])

def groupP(pred, ls):
    def internal(acc, n):
        if acc and pred(acc[-1][0], n):
            acc[-1].append(n)
        else:
            acc.append([n])
        return acc
    return reduce(internal, ls, [])

def partitionP(pred, ls):
    def internal(acc, n):
        if pred(n):
            acc.append([n])
        elif len(acc) > 0:
            acc[-1].append(n)
        return acc
    return reduce(internal, ls, [])

def partition(s, ls):
    def internal(acc, n):
        if acc and len(acc[-1]) < s:
            acc[-1].append(n)
        else:
            acc.append([n])
        return acc
    return reduce(internal, ls, [])

def flatMap(f, ls):
    return flatten(map(f, ls))



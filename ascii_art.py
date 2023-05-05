import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
n = list()
f = "abcdefghijklmnopqrstuvwxyz?"
t = input().lower()
for i in range(h):
    row = input()
    q = list()
    for r in range(0,len(row),l):
        q.append(row[r:r+l])
    n.append(q)
    u = list()
    for j in range(len(t)):
        k = 0
        for y in range(len(f)):
            if t[j] == f[y]:
                k = 1
                u.append(n[i][y])
        if k == 0:
            u.append(n[i][len(n[0]) - 1])
    print(''.join(u))

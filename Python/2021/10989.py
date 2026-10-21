'''
x = []

for i in range(int(input())):
    x.append(int(input()))

x.sort()

for i in range(len(x)):
    print(x[i])
'''

import sys

x = [0]*10001

for i in range(int(input())):
    x[int(sys.stdin.readline())] += 1

for i in range(10001):
    for j in range(x[i]):
        print(i)

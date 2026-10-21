import sys

x = []
t = 0 

for i in range(int(input())):
    x.append(int(sys.stdin.readline()))

x.sort()

for i in range(len(x)):
    t += abs(x[i] - (i+1))

print(t)

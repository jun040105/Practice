x = int(input())
d = list(map(int, input().split()))

c = [0]*(len(d))

c[0] = d[0]
c[1] = max(d[0], d[1])

for i in range (2, x):

    c[i] = c[i-2] + d[i]

    c[i] = max(c[i], c[i-1])

print(c[-1])
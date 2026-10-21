n, x = map(int, input().split())
c = []
a = 0

for i in range(n):
    c.append(int(input()))

for i in range(len(c)-1, -1, -1):
    if x >= c[i]:
        a += x // c[i]
        x = x % c[i]

print(a)

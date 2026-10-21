a, x = map(int, input().split())

b = []
for i in range(a):
    b.append(int(input()))

# --------------------------------

c = [10001]*(x+1)
c[0] = 0

for i in range(a): 
    for j in range(b[i], x+1):
        c[j] = min(c[j-b[i]] + 1, c[j])

if c[x] == 10001:
    print(-1)
else: print(c[x])
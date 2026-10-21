x = int(input())
y = list(map(int, input().split()))
y.sort()

t = 0

for i in range(len(y)):
    t += (y[i])*(x-i)

print(t)
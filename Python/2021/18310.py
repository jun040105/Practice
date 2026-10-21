n = int(input())
x = list(map(int, input().split()))
x.sort()

if len(x) % 2 != 0:
    z = (len(x) + 1)//2
else:
    z = len(x)//2

print(x[z-1])



ans = 0

x = int(input())

a = list(map(int, input().split(" ")))
a.sort()
b = list(map(int, input().split(" ")))
b.sort(reverse = True)

for i in range(x):
    ans += a[i]*b[i]

print(ans)

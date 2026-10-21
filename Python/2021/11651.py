a = []

for i in range(int(input())):
    x, y = map(int, input().split())
    arr = [y, x]
    a.append(arr)

a.sort()

for i in range (len(a)):
    print(a[i][1], a[i][0])

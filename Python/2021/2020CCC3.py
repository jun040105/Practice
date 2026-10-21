x =[]
y =[]
for i in range(int(input())):
    a, b = map(int, input().split(","))
    x.append(a)
    y.append(b)

x.sort()
y.sort()

print(str(x[0]-1) + ",", str(y[0] -1))
print(str(x[-1]+1) + ",", str(y[-1] +1))

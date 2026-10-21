x = []

for i in range(int(input())):
    x.append(input().split(" "))

# x = sorted(x, lambda a: a[0], reverse=True)
x = sorted(x,key = lambda x: int(x[0]))
for i in range (len(x)):
    print(x[i][0], x[i][1])
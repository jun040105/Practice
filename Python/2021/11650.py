x = []

for i in range(int(input())):
    x.append(list(map(int, input().split())))

x = sorted(x, key = lambda x : (x[0], x[1]))

for i in range(len(x)):
    print(x[i][0], x[i][1])
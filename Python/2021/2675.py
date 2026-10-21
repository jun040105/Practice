for i in range(int(input())):
    x, y = map(str, input().split(" "))
    x = int(x)
    for i in range(len(y)):
        for j in range(x):
            print(y[i], end="")
    print("")
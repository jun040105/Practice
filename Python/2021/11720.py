a = input()
x = list(map(int, input().strip()))
t = 0
for i in range(len(x)):
    t += x[i]
    if i == len(x) -1:
        print(t)

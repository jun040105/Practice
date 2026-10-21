x = []
t = 0

for i in range(int(input())):
    a = int(input())
    if a == 0:
        del(x[-1])
    else: x.append(a)

for i in range(len(x)):
    t += x[i]

print(t)

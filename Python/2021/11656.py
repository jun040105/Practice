x = input()
a = []

for i in range(len(x)):
    a.append(x[i:])

a = sorted(a)

for i in range(len(a)):
    print(a[i])